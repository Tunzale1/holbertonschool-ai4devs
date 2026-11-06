# Bug Reports – AI-Assisted Debugging Project

## Bug Report 1 – bug1.py

- **File Name**: `bug1.py`
- **Bug Summary**: The program failed to calculate the average of a list because of a syntax error in the `for` loop.
- **Root Cause**: The colon (`:`) was missing after the loop declaration `for number in numbers`. Python requires a colon to define the beginning of a loop body.
- **Resolution**:
  - **AI-Generated Fix**: Added the missing colon to the `for` loop.
  - **Manual Edits**: Added validation for empty lists to prevent division by zero and introduced assertion tests.
  - **Result**: The program successfully calculates averages for valid lists.
- **Lessons Learned**: Small syntax mistakes can prevent an entire program from running. Syntax validation and basic test cases are important during development.

---

## Bug Report 2 – bug2.py

- **File Name**: `bug2.py`
- **Bug Summary**: The program incorrectly classified negative numbers as zero.
- **Root Cause**: The second conditional statement used `number > 0` instead of `number < 0`, repeating the positive-number condition.
- **Resolution**:
  - **AI-Generated Fix**: Changed the second condition to `number < 0`.
  - **Manual Edits**: Added assertion tests for positive numbers, negative numbers, and zero.
  - **Result**: All three number categories are now identified correctly.
- **Lessons Learned**: Logical errors may not cause program crashes but can produce incorrect results. Testing different input conditions helps identify these problems.

---

## Bug Report 3 – bug3.js

- **File Name**: `bug3.js`
- **Bug Summary**: The shopping cart calculation produced a runtime exception when accessing an invalid array element.
- **Root Cause**: The loop condition used `i <= cart.length`, allowing the program to access an index beyond the last valid array element.
- **Resolution**:
  - **AI-Generated Fix**: Changed the loop condition to `i < cart.length`.
  - **Manual Edits**: Added assertions to test both a populated shopping cart and an empty cart.
  - **Result**: The program correctly calculates the total price without accessing invalid array positions.
- **Lessons Learned**: Array indexes must remain within valid boundaries. Empty arrays and the final array element should always be included in testing.

---

## Bug Report 4 – bug4.js

- **File Name**: `bug4.js`
- **Bug Summary**: The number-generation function excluded the final number from its output.
- **Root Cause**: The loop condition used `i < limit`, which stopped the loop before reaching the specified limit.
- **Resolution**:
  - **AI-Generated Fix**: Changed the condition to `i <= limit`.
  - **Manual Edits**: Added assertions to verify the first number, last number, and total number of elements.
  - **Result**: The function now correctly generates all integers from 1 to the specified limit, including the limit.
- **Lessons Learned**: Loop boundaries require careful attention. Testing the first and last expected elements helps prevent off-by-one errors.

---

## Bug Report 5 – bug5.java

- **File Name**: `bug5.java`
- **Bug Summary**: The program returned an inaccurate exam average because decimal values were lost during division.
- **Root Cause**: The average variable was declared as an integer, causing integer division to discard the fractional part.
- **Resolution**:
  - **AI-Generated Fix**: Changed the average calculation to use the `double` data type and cast the total before division.
  - **Manual Edits**: Added assertions using `Math.abs()` to verify decimal precision and included validation for empty score arrays.
  - **Result**: The program now calculates and displays accurate averages with decimal precision.
- **Lessons Learned**: Choosing appropriate data types is essential for mathematical accuracy. Integer division should be avoided when decimal results are required.

---

## Bug Report 6 – bug6.py

- **File Name**: `bug6.py`
- **Bug Summary**: The original task description incorrectly identified the JSON-reading code as containing a library misuse.
- **Root Cause**: The original implementation already used `json.load(file)`, which is the correct method for reading JSON directly from a file object. The earlier debugging suggestion incorrectly proposed replacing it with `json.loads(file)`.
- **Resolution**:
  - **AI-Generated Analysis**: Identified that `json.load(file)` was already correct and that `json.loads()` expects a string.
  - **Manual Edits**: Kept the correct `json.load(file)` implementation, created a separate `user.json` test file, and added an assertion to verify the extracted name.
  - **Result**: The program successfully reads the JSON file and converts the user's name to uppercase.
- **Lessons Learned**: AI-generated debugging suggestions must be reviewed critically. Not every reported bug is a real bug, and understanding the difference between `json.load()` and `json.loads()` is important.

---

# Overall Project Summary

This project involved identifying, debugging, fixing, and validating six intentionally flawed code samples written in Python, JavaScript, and Java.

The debugging exercises covered:

1. Syntax errors.
2. Logical errors.
3. Runtime exceptions.
4. Off-by-one errors.
5. Incorrect data type usage.
6. JSON library usage.

## Key Lessons Learned

- AI tools can help identify programming errors and suggest possible solutions.
- AI-generated fixes should always be reviewed and tested before implementation.
- Manual improvements, such as input validation and additional assertions, can make programs more reliable.
- Testing normal inputs, edge cases, and unexpected inputs is essential.
- Understanding the root cause of a bug is more valuable than simply copying a suggested fix.

## Final Conclusion

The project demonstrated how AI-assisted debugging can support software development by making error identification and correction more efficient. It also highlighted the importance of human verification, critical thinking, and systematic testing.

All six corrected programs have documented fixes and validation cases. The project provides practical experience in debugging and improving code quality across multiple programming languages.