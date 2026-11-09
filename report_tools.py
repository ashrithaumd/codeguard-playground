import subprocess

import anthropic

client = anthropic.Anthropic()


def evaluate(user_expression):
    return eval(user_expression)


def run_job(user_cmd):
    return subprocess.run(user_cmd, shell=True, capture_output=True, text=True).stdout


def summarize(user_text):
    prompt = "Summarize this report: " + user_text
    response = client.messages.create(
        model="claude-3-5-sonnet-latest",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def ratio(a, b):
    return a / b
