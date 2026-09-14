import anthropic

client = anthropic.Anthropic()


def chat(message):
    # Phase 6 live verification: exactly 3 planted weaknesses on this
    # one call — a floating model alias, no max_tokens, and no system
    # prompt — for CodeGuard's AI-aware agent to catch and interpret.
    return client.messages.create(model="claude-3-5-sonnet-latest", messages=[{"role": "user", "content": message}], timeout=5)
