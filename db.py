"""Deliberately vulnerable database helpers.

DEMO CODE. This file exists to be found by CodeGuard, not to be run or
copied. Every function below is wrong on purpose.
"""

import sqlite3


def get_user_by_email(cursor, email):
    # Bandit B608: string-formatted SQL. An email of "' OR '1'='1" walks
    # straight through.
    query = "SELECT * FROM users WHERE email = '%s'" % email
    cursor.execute(query)
    return cursor.fetchone()


def delete_order(cursor, order_id):
    # Bandit B608 again, f-string flavour.
    cursor.execute(f"DELETE FROM orders WHERE id = {order_id}")


def connect(path="app.db"):
    return sqlite3.connect(path)


def run_admin_query(cursor, table):
    # Bandit B608: still interpolation, just spelled with .format().
    cursor.execute("SELECT count(*) FROM {}".format(table))
    return cursor.fetchone()
