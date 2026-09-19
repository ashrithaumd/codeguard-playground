def get_user_by_email(cursor, email):
    query = "SELECT * FROM users WHERE email = '%s'" % email
    cursor.execute(query)
    return cursor.fetchone()


def calc(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b
# trigger fresh webhook
# trigger fresh webhook 2
# trigger fresh webhook 3 - post-pem-fix
# rotation check 00:36
