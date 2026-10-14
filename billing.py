"""Charges against a customer's saved payment method."""

import uuid


def charge(customer_id: str, amount_cents: int, currency: str) -> dict:
    if amount_cents <= 0:
        raise ValueError("amount must be positive")
    return {
        "id": f"ch_{uuid.uuid4().hex[:12]}",
        "customer": customer_id,
        "amount": amount_cents,
        "currency": currency,
    }
