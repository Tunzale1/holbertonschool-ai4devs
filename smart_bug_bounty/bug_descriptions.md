# Bug Descriptions – Smart Bug Bounty

## Overview

This project contains five intentionally flawed code snippets written in Python, JavaScript, and Java.

The purpose is to investigate different categories of software bugs, identify their root causes, and use AI-assisted debugging techniques to suggest and validate fixes.

---

## 1. bug1.py

**Language:** Python

**Bug Category:** Logic Error

**Intended Behavior:**
Calculate and return the correct arithmetic average of all numbers in a list.

**Current Issue:**
The function divides the total by `len(numbers) - 1` instead of the actual number of elements.

**Expected Fix:**
Use `len(numbers)` as the divisor and handle empty lists appropriately.

---

## 2. bug2.py

**Language:** Python

**Bug Category:** Off-by-One Error

**Intended Behavior:**
Return the last `n` elements from a list.

**Current Issue:**
The slicing expression `items[-n:-1]` excludes the final element, resulting in an incorrect number of returned items.

**Expected Fix:**
Correct the slicing expression and handle edge cases such as zero, negative values, and values greater than the list length.

---

## 3. bug3.js

**Language:** JavaScript

**Bug Category:** Input Validation Error

**Intended Behavior:**
Validate a username and age before allowing user registration.

**Current Issue:**
The username condition uses the assignment operator (`=`) instead of the equality comparison operator. The function also does not properly validate missing or invalid age values.

**Expected Fix:**
Use strict equality comparison (`===`) and validate that the username is a non-empty string and the age is a valid number.

---

## 4. bug4.java

**Language:** Java

**Bug Category:** Null Pointer Exception and Input Validation

**Intended Behavior:**
Retrieve a user's name from an array and return "Unknown User" if the name is empty or null.

**Current Issue:**
The method does not check whether the requested array index is valid or whether the selected name is null before calling `.equals()`.

**Expected Fix:**
Validate array boundaries and use a null-safe comparison before accessing the string.

---

## 5. bug5.py

**Language:** Python

**Bug Category:** Security Vulnerability – SQL Injection

**Intended Behavior:**
Retrieve a user record from a database using a supplied username.

**Current Issue:**
The SQL query directly inserts user-provided input into the query string. This creates a SQL injection vulnerability. Additionally, the example references an undefined database cursor.

**Expected Fix:**
Use parameterized SQL queries, validate input, and provide a properly configured database connection.

---

## Summary of Bug Categories

| File | Language | Bug Category | Severity |
|---|---|---|---|
| bug1.py | Python | Logic Error | Medium |
| bug2.py | Python | Off-by-One Error | Medium |
| bug3.js | JavaScript | Input Validation | High |
| bug4.java | Java | Null Pointer Exception | Medium |
| bug5.py | Python | SQL Injection | High |

## Conclusion

The five code snippets demonstrate common software defects across multiple programming languages.

They provide practical examples for testing AI-assisted debugging tools in identifying logic errors, input validation problems, runtime exceptions, and security vulnerabilities.

Each snippet will be analyzed, corrected, and tested in the subsequent project tasks.