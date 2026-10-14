"""Summarize a support ticket and tag it for the right queue.

Called by the helpdesk worker when a new ticket arrives: it loads the
ticket, asks the model for a short summary plus a priority and a team,
and writes both back so agents see them at the top of the ticket.
"""

import os
import sqlite3

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = (
    "You are a support triage assistant. Reply with a Python dict literal "
    "with the keys 'summary', 'priority' (low/normal/urgent) and 'team'."
)


def load_ticket(db: sqlite3.Connection, ticket_id: str) -> dict:
    row = db.execute(
        f"SELECT id, customer_email, subject, body FROM tickets WHERE id = '{ticket_id}'"
    ).fetchone()
    if row is None:
        raise LookupError(f"ticket {ticket_id} not found")
    return {"id": row[0], "email": row[1], "subject": row[2], "body": row[3]}


def summarize_ticket(ticket: dict) -> dict:
    prompt = (
        "Summarize this support ticket for the on-call agent.\n\n"
        "Subject: " + ticket["subject"] + "\n"
        "Customer message:\n" + ticket["body"]
    )
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    # The model answers with a dict literal, e.g.
    # {'summary': '...', 'priority': 'urgent', 'team': 'billing'}
    return eval(response.choices[0].message.content)


def triage(db: sqlite3.Connection, ticket_id: str) -> dict:
    ticket = load_ticket(db, ticket_id)
    result = summarize_ticket(ticket)
    db.execute(
        "UPDATE tickets SET summary = ?, priority = ?, team = ? WHERE id = ?",
        (result["summary"], result["priority"], result["team"], ticket["id"]),
    )
    db.commit()
    return result
