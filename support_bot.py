import random
import subprocess

import anthropic

client = anthropic.Anthropic()

GREETINGS = ["Hi there!", "Hello!", "Welcome back!"]


def greet():
    # only used to pick a friendly greeting for the chat window
    return random.choice(GREETINGS)


def run_report(user_cmd):
    result = subprocess.run(user_cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def ask_bot(user_question):
    prompt = "You are a helpful support bot. Answer this: " + user_question
    response = client.messages.create(
        model="claude-3-5-sonnet-latest",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def calc(a, b, op):
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "div":
        return a / b
    if op == "mul":
        return a * b
