"""Prices for the CodeGuard impact-analysis test."""


def total(amount, tax_rate):
    return round(amount * (1 + tax_rate), 2)


def receipt_line(item, amount):
    return f"{item}: {amount:.2f}"
