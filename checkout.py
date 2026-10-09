"""Checkout: calls pricing.total and is not changed by the test PRs."""

from pricing import total


def checkout(cart):
    subtotal = sum(cart.values())
    return total(subtotal, 0.08)
