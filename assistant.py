"""Deliberately bad LLM integration code.

DEMO CODE. This file exists to be found by CodeGuard's llm-security
ruleset, not to be run or copied. The credentials below are obviously
fake placeholders, not real keys.

Each function is annotated with the rule it is meant to trip, so a reader
comparing the audit report against this file can tell a real hit from a
coincidence.
"""

import openai
from openai import OpenAI

import anthropic


# llm-hardcoded-api-key — bare-name constructor. This is the exact shape
# that matched nothing until the langflow scan found the false negative:
# every pattern used to require the `openai.` module prefix.
client = OpenAI(api_key="sk-placeholder-not-a-real-key-000000000000")

# llm-hardcoded-api-key — module-prefixed form, and the assignment regex.
legacy_client = openai.OpenAI(api_key="sk-placeholder-not-a-real-key-111111111111")
ANTHROPIC_API_KEY = "placeholder-not-a-real-key-2222222222222222"


def summarize(text):
    """llm-call-missing-timeout — no timeout on the call.
    llm-call-missing-max-tokens — no ceiling on the response.
    llm-missing-system-user-separation — no system turn.
    """
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )


def classify(user_input):
    """llm-prompt-injection-concatenation — untrusted input concatenated
    straight into the prompt.
    llm-unpinned-model-alias — "-latest" floats.
    """
    prompt = "Classify the following support ticket:\n" + user_input
    c = anthropic.Anthropic(api_key="placeholder-not-a-real-key-3333333333")
    return c.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )


def run_untrusted(code_from_model):
    """llm-output-to-dangerous-sink — model output into eval()."""
    completion = client.chat.completions.create(
        model="gpt-4o",
        timeout=30,
        max_tokens=256,
        messages=[
            {"role": "system", "content": "Return a Python expression."},
            {"role": "user", "content": code_from_model},
        ],
    )
    return eval(completion.choices[0].message.content)


def log_everything(text):
    """llm-logging-full-prompt-or-response — the whole response in a log
    line, prompts and all."""
    import logging

    resp = client.chat.completions.create(
        model="gpt-4o",
        timeout=30,
        max_tokens=256,
        messages=[
            {"role": "system", "content": "Be brief."},
            {"role": "user", "content": text},
        ],
    )
    logging.info("model response: %s", resp.choices[0].message.content)
    return resp
