# AI Debug Log – Smart Bug Bounty

## Overview

This document records the results of AI-assisted debugging for five intentionally flawed code snippets written in Python, JavaScript, and Java.

Each snippet was analyzed to identify its programming error, explain the root cause, recommend a solution, and assign a confidence level to the analysis.

---

## 1. bug1.py – Incorrect Average Calculation

**Language:** Python

**AI Explanation:**

The function `calculate_average()` calculates the sum of all numbers correctly, but divides the total by `len(numbers) - 1` instead of `len(numbers)`. This produces an incorrect average because the divisor is one less than the actual number of elements. For example, a list containing four numbers will be divided by three instead of four. Additionally, an empty list causes a division-by-zero error.

**Suggested Fix:**

Use `len(numbers)` as the divisor and check whether the list is empty before performing the calculation.

```python
def calculate_average(numbers):
    if not numbers:
        return 0

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    return average
```

**Confidence:** High

**Bug Category:** Logic Error

---

## 2. bug2.py – Off-by-One Error in List Slicing

**Language:** Python

**AI Explanation:**

The function `get_last_items()` is intended to return the last `n` elements of a list. However, the slicing expression `items[-n:-1]` excludes the final element because the ending index of a Python slice is not included. As a result, the function returns fewer elements than expected. Another edge case occurs when `n` is zero, because `-0` is equivalent to zero in Python.

**Suggested Fix:**

Use `items[-n:]` to include the final element. Handle zero and negative values separately.

```python
def get_last_items(items, n):
    if n <= 0:
        return []

    return items[-n:]
```

**Confidence:** High

**Bug Category:** Off-by-One Error

---

## 3. bug3.js – Incorrect Username Validation

**Language:** JavaScript

**AI Explanation:**

The function `registerUser()` uses the assignment operator (`=`) instead of a comparison operator in the username validation condition. Although JavaScript permits assignment in an `if` condition, this changes the username parameter to an empty string instead of checking whether it is empty. Consequently, the validation does not work correctly and may allow invalid usernames. The function also does not validate whether the age is a valid number.

**Suggested Fix:**

Use strict equality (`===`) or validate the username with `trim()`. Also check that age is a valid number and that the user is at least 18 years old.

```javascript
function registerUser(username, age) {
    if (typeof username !== "string" || username.trim() === "") {
        return "Username is required";
    }

    if (!Number.isInteger(age) || age < 18) {
        return "User must be at least 18";
    }

    return "Registration successful";
}

console.log(registerUser("", 25));
console.log(registerUser("Alex", 15));
console.log(registerUser("Sarah", 25));
```

**Confidence:** High

**Bug Category:** Input Validation Error

---

## 4. bug4.java – Null Pointer Exception

**Language:** Java

**AI Explanation:**

The method `getUserName()` retrieves a name from an array and checks whether it is empty using `name.equals("")`. However, the array contains a null value. When the method attempts to call `.equals()` on that null value, Java throws a `NullPointerException`. The method also does not check whether the requested index is within the valid array boundaries.

**Suggested Fix:**

Check whether the index is valid and use a null-safe comparison with `name == null` or `name.isEmpty()` after the null check.

```java
public class Bug4 {
    public static String getUserName(String[] users, int index) {
        if (index < 0 || index >= users.length) {
            return "Unknown User";
        }

        String name = users[index];

        if (name == null || name.isEmpty()) {
            return "Unknown User";
        }

        return name;
    }

    public static void main(String[] args) {
        String[] users = {"Alex", null, "Sarah"};

        System.out.println(getUserName(users, 0));
        System.out.println(getUserName(users, 1));
    }
}
```

**Confidence:** High

**Bug Category:** Null Pointer Exception and Input Validation

---

## 5. bug5.py – SQL Injection Vulnerability

**Language:** Python

**AI Explanation:**

The function `get_user_by_name()` constructs an SQL query by directly inserting the supplied username into the query string using string formatting. This creates an SQL injection vulnerability because malicious input could change the structure or behavior of the SQL query. The function also relies on `database_cursor`, which is not defined in the provided code. Calling `main()` without configuring a database connection would therefore cause a `NameError`.

**Suggested Fix:**

Use parameterized SQL queries instead of directly inserting user input into the query. This separates SQL instructions from user-provided values and helps prevent SQL injection. Also, pass a properly configured database cursor to the function.

```python
def get_user_by_name(cursor, username):
    query = "SELECT * FROM users WHERE username = %s"

    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result:
        return result

    return None


def main(database_cursor):
    username = input("Enter username: ")
    user = get_user_by_name(database_cursor, username)

    if user:
        print("User found:", user)
    else:
        print("User not found")


# Example usage requires a configured database connection.
```

**Note:** The `%s` placeholder is suitable for database drivers such as psycopg and MySQL Connector/Python. SQLite uses `?` instead.

**Confidence:** High

**Bug Category:** Security Vulnerability – SQL Injection

---

## Conclusion

AI-assisted debugging successfully identified five different programming issues across Python, JavaScript, and Java.

The analysis covered logic errors, off-by-one errors, incorrect input validation, null pointer exceptions, and SQL injection vulnerabilities.

For each snippet, AI provided an explanation of the root cause and a suggested correction. The proposed fixes demonstrate how AI tools can help developers understand programming errors, improve code quality, and identify potential security weaknesses.

Overall, the debugging exercise showed that AI can be a useful assistant in software development by making error analysis faster and providing practical solutions. However, suggested fixes should still be reviewed and tested before being used in production.
