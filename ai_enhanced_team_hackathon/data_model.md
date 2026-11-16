# Data Model – AI-Powered Study Assistant

## 1. Overview

This document defines the database structure for the AI-Powered Study Assistant. The data model describes the main entities, their attributes, primary keys, foreign keys, and relationships.

The database will store user information, submitted educational materials, generated quizzes, personalized study plans, and learning progress.

## 2. Database Entities

### Entity 1: User

Stores information about registered students.

| Attribute | Data Type | Description |
|---|---|---|
| user_id | INTEGER (PK) | Unique user identifier |
| full_name | VARCHAR(100) | Student's full name |
| email | VARCHAR(150) | Unique email address |
| password_hash | VARCHAR(255) | Hashed account password |
| created_at | TIMESTAMP | Account creation date |

### Entity 2: StudyMaterial

Stores educational materials submitted by users.

| Attribute | Data Type | Description |
|---|---|---|
| material_id | INTEGER (PK) | Unique material identifier |
| user_id | INTEGER (FK) | Owner of the material |
| title | VARCHAR(200) | Material title |
| content | TEXT | Submitted educational text |
| summary | TEXT | AI-generated summary |
| created_at | TIMESTAMP | Submission date |

### Entity 3: Quiz

Stores AI-generated quizzes and their results.

| Attribute | Data Type | Description |
|---|---|---|
| quiz_id | INTEGER (PK) | Unique quiz identifier |
| user_id | INTEGER (FK) | User who created the quiz |
| material_id | INTEGER (FK) | Related study material |
| questions | JSON | Generated quiz questions |
| answers | JSON | User-submitted answers |
| score | DECIMAL(5,2) | Quiz score |
| created_at | TIMESTAMP | Quiz creation date |

### Entity 4: StudyPlan

Stores personalized learning schedules.

| Attribute | Data Type | Description |
|---|---|---|
| plan_id | INTEGER (PK) | Unique study plan identifier |
| user_id | INTEGER (FK) | Owner of the plan |
| goal | VARCHAR(255) | Learning objective |
| daily_study_hours | DECIMAL(4,2) | Available daily study time |
| exam_date | DATE | Target examination date |
| schedule | JSON | AI-generated study schedule |
| status | VARCHAR(30) | Current plan status |
| created_at | TIMESTAMP | Plan creation date |

### Entity 5: Progress

Tracks student learning activities and achievements.

| Attribute | Data Type | Description |
|---|---|---|
| progress_id | INTEGER (PK) | Unique progress record identifier |
| user_id | INTEGER (FK) | Related student |
| plan_id | INTEGER (FK, nullable) | Related study plan |
| activity_name | VARCHAR(200) | Completed learning activity |
| completion_status | VARCHAR(30) | Pending or completed |
| completion_date | TIMESTAMP | Activity completion date |
| notes | TEXT | Additional progress information |

## 3. Entity Relationships

The database uses the following relationships:

1. **User → StudyMaterial:** One user can submit multiple study materials. Each material belongs to one user (one-to-many).
2. **User → Quiz:** One user can generate multiple quizzes. Each quiz belongs to one user (one-to-many).
3. **StudyMaterial → Quiz:** One study material can be used to generate multiple quizzes (one-to-many).
4. **User → StudyPlan:** One user can create multiple study plans (one-to-many).
5. **User → Progress:** One user can have multiple progress records (one-to-many).
6. **StudyPlan → Progress:** One study plan can have multiple progress records (one-to-many).

## 4. Data Integrity and Constraints

- Each entity has a unique primary key.
- Foreign keys maintain relationships between records.
- User email addresses must be unique.
- Passwords must be stored as secure hashes, never as plain text.
- Required fields cannot be empty.
- Quiz scores must be within the valid range of 0 to 100.
- User records should be protected so that students can access only their own information.

## 5. Conclusion

The proposed data model contains five main entities that support the core functionality of the AI-Powered Study Assistant.

The structure provides a foundation for managing student accounts, educational materials, quizzes, personalized study schedules, and learning progress.

The database can be extended in future versions to support additional features such as notifications, flashcards, and collaborative learning.