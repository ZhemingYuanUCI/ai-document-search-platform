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
```

### POST /auth/login

Authenticates a user and returns an access token.

#### Request

```json
{
    "email": "user@example.com",
    "password": "your_password"
}
```

#### Response

```json
{
    "access_token": "jwt_token",
    "token_type": "bearer"
}
```