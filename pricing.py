"""Prices for the CodeGuard impact-analysis test."""


def total(amount, tax_rate, *, currency):
    return {"amount": round(amount * (1 + tax_rate), 2), "currency": currency}


def receipt_line(item, amount):
    return f"{item}: {amount:.2f}"
