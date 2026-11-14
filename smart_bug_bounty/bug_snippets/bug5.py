def get_user_by_name(cursor, username):
    query = "SELECT * FROM users WHERE username = '%s'" % username

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return result

    return None


def main():
    username = input("Enter username: ")
    user = get_user_by_name(database_cursor, username)

    if user:
        print("User found:", user)
    else:
        print("User not found")


# Example usage (requires a configured database connection)
# main()