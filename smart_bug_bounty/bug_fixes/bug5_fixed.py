
def get_user_by_name(cursor, username):
    query = "SELECT * FROM users WHERE username = ?"

    cursor.execute(query, (username,))
    result = cursor.fetchone()

    return result


if __name__ == "__main__":
    import sqlite3

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)"
    )
    cursor.execute(
        "INSERT INTO users (username) VALUES (?)",
        ("alice",)
    )

    username = "alice"
    user = get_user_by_name(cursor, username)

    if user:
        print("User found:", user)
    else:
        print("User not found")

    connection.close()