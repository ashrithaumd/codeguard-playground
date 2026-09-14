import sqlite3

# Deliberate issue: hardcoded credential
DB_PASSWORD = "admin123"


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Deliberate issue: SQL injection via string concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Deliberate issue: SQL injection via f-string, plus no error handling
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
# trigger phase 4 tooling run
# trigger phase 4.1 timing measurement
# trigger phase 5 pipeline verification
# Phase 7 verification: 5-file PR trigger
