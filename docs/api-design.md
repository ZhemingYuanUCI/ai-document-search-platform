# API Design

## 1. Authentication APIs

### POST /auth/register

Creates a new user account.

#### Request

```json
{
    "email": "user@example.com",
    "username": "Alice",
    "password": "your_password"
}
```

#### Response

```json
{
    "id": "uuid",
    "email": "user@example.com",
    "username": "Alice"
}