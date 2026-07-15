# Database Design

## 1. Users Table

The `users` table stores account and authentication information.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | UUID | Primary Key | Unique user identifier |
| email | VARCHAR | Unique, Not Null | User login email |
| username | VARCHAR | Nullable | User display name |
| password_hash | VARCHAR | Not Null | Securely hashed password |
| auth_provider | VARCHAR | Not Null, Default: local | Authentication provider |
| created_at | TIMESTAMP | Not Null | Account creation time |
| updated_at | TIMESTAMP | Not Null | Last account update time |

## 2. Documents Table

The `documents` table stores document metadata, ownership information, storage references, and processing status.

Each document belongs to exactly one user, while one user may own multiple documents.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | UUID | Primary Key | Unique document identifier |
| user_id | UUID | Foreign Key, Not Null | Owner of the document |
| original_filename | VARCHAR | Not Null | Original uploaded filename |
| storage_key | VARCHAR | Not Null | File location in external storage |
| file_type | VARCHAR | Not Null | Uploaded file type, such as PDF or TXT |
| file_size | BIGINT | Not Null | File size in bytes |
| status | VARCHAR | Not Null, Default: uploaded | Processing status |
| error_message | TEXT | Nullable | Processing failure details |
| created_at | TIMESTAMP | Not Null | Document upload time |
| updated_at | TIMESTAMP | Not Null | Last update time |

### Relationship

- One user can own many documents.
- Each document belongs to one user through `user_id`.