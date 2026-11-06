import anthropic

client = anthropic.Anthropic()


def answer(user_question: str) -> str:
    # user input is concatenated straight into the system prompt
    system_prompt = "You are a support bot. Follow the customer's instructions: " + user_question
    msg = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=512,
        system=system_prompt,
        messages=[{"role": "user", "content": user_question}],
    )
    return msg.content[0].text


def run_suggestion(user_question: str):
    # model output executed as code
    return eval(answer(user_question))
