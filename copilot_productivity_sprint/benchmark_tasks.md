
# Coding Benchmark Tasks

## Task 1 - To-Do List API

**Estimated Time:** 20-30 minutes

**Requirements:**
Implement a simple API endpoint that allows users to create and retrieve to-do tasks. Each task should have an ID, title, and completion status.

**Inputs:**
- JSON object containing a task title.
- Example: `{"title": "Complete coding assignment"}`

**Outputs:**
- A JSON response containing the task ID, title, and completion status.

**Acceptance Criteria:**
- Returns HTTP 201 when a task is successfully created.
- Returns HTTP 400 if the task title is missing or empty.
- Each task receives a unique ID.
- Users can retrieve the list of created tasks.

---

## Task 2 - Text Analyzer

**Estimated Time:** 15-20 minutes

**Requirements:**
Create a function that analyzes a text string and calculates the total number of words, characters, and sentences.

**Inputs:**
- A text string.
- Example: `"Artificial intelligence is changing the world. Technology is evolving."`

**Outputs:**
- Total number of words.
- Total number of characters.
- Total number of sentences.

**Acceptance Criteria:**
- Correctly counts words separated by whitespace.
- Correctly counts all characters, including spaces and punctuation.
- Correctly identifies sentences ending with periods, question marks, or exclamation marks.
- Returns zero counts for an empty string.

---

## Task 3 - Password Validator

**Estimated Time:** 15-20 minutes

**Requirements:**
Implement a function that checks whether a password meets basic security requirements.

**Inputs:**
- A password string.
- Example: `"SecurePass123!"`

**Outputs:**
- A validation result (valid or invalid).
- A list of requirements that the password does not satisfy.

**Acceptance Criteria:**
- Password must contain at least 8 characters.
- Password must contain at least one uppercase letter.
- Password must contain at least one lowercase letter.
- Password must contain at least one number.
- Password must contain at least one special character.
- Returns a valid result when all requirements are satisfied.
