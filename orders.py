"""Order checkout: charges the customer for the order total."""

from billing import charge


def checkout(order: dict) -> dict:
    receipt = charge(order["customer_id"], order["total_cents"])
    return {"order": order["id"], "charge": receipt["id"]}
