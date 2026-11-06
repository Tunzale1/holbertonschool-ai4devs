# Bug Snippets – Intended Behavior and Descriptions

## Bug 1 – bug1.py

**Intended Behavior**: Calculate and return the average of a list of numbers.

**Issue Type**: Syntax error.

**Notes**: The `for` loop is missing a colon after the `numbers` statement. Python cannot execute the code until the syntax is corrected.

## Bug 2 – bug2.py

**Intended Behavior**: Identify whether a given number is positive, negative, or zero.

**Issue Type**: Logical error.

**Notes**: The second condition incorrectly checks whether the number is greater than zero instead of less than zero. Negative numbers are therefore classified as zero.

## Bug 3 – bug3.js

**Intended Behavior**: Calculate the total price of all products in a shopping cart.

**Issue Type**: Runtime exception and loop boundary error.

**Notes**: The loop uses `i <= cart.length`, causing it to access an array element that does not exist. This results in a TypeError when trying to read the price property.

## Bug 4 – bug4.js

**Intended Behavior**: Generate and return all integers from 1 to the specified limit, including the limit.

**Issue Type**: Off-by-one error.

**Notes**: The loop condition uses `i < limit` instead of `i <= limit`. As a result, the final number is excluded from the output.

## Bug 5 – bug5.java

**Intended Behavior**: Calculate and display the average exam score with decimal precision.

**Issue Type**: Incorrect data type usage.

**Notes**: The average variable is declared as an integer. Integer division removes the decimal portion of the result, producing an inaccurate average.

## Bug 6 – bug6.py

**Intended Behavior**: Read a JSON file, extract the user's name, convert it to uppercase, and return it.

**Issue Type**: Misuse of a library.

**Notes**: The `json.loads()` function expects a JSON string, but the code passes a file object instead. This causes a TypeError. The correct function for reading JSON directly from a file object is `json.load()`.

