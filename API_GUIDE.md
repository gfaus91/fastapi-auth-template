# 📚 FastAPI Auth Template - API Guide

Complete guide for using the JWT authentication API through Swagger UI and programmatically.

## 🚀 Quick Access

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI JSON**: [http://localhost:8000/api/v1/openapi.json](http://localhost:8000/api/v1/openapi.json)

---

## 🔐 Authentication Flow Overview

This API implements **JWT (JSON Web Token)** authentication with **access** and **refresh** tokens:

1. **Register** → Create a new user account
2. **Login** → Get access_token + refresh_token
3. **Authorize** → Use access_token for protected endpoints
4. **Refresh** → Get new tokens when access_token expires

---

## 📋 Complete API Reference

### 🆕 Auth Endpoints

#### 1. POST `/api/v1/auth/register` - Register New User

**Purpose**: Create a new user account in the system.

**How to test in Swagger UI**:
1. Navigate to `POST /api/v1/auth/register`
2. Click **"Try it out"**
3. Replace the example JSON with your data:

```json
{
  "email": "your.email@example.com",
  "password": "your_secure_password",
  "is_active": true,
  "is_superuser": false
}
```

4. Click **"Execute"**

**Expected Response (200)**:
```json
{
  "email": "your.email@example.com",
  "is_active": true,
  "is_superuser": false,
  "id": 1,
  "created_at": "2025-06-25T07:13:54.287884Z",
  "updated_at": null
}
```

**cURL Example**:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "your.email@example.com",
  "password": "your_secure_password",
  "is_active": true,
  "is_superuser": false
}'
```

**Common Errors**:
- `400`: User already exists
- `422`: Invalid email format or missing fields

---

#### 2. POST `/api/v1/auth/login` - Login User

**Purpose**: Authenticate user and receive JWT tokens for API access.

**How to test in Swagger UI**:
1. Navigate to `POST /api/v1/auth/login`
2. Click **"Try it out"**
3. **Important**: Use Form Data (not JSON). Fill only:
   - **username**: `your.email@example.com` (yes, use email as username)
   - **password**: `your_secure_password`
   - **Leave all other fields empty** (grant_type, scope, client_id, client_secret)

4. Click **"Execute"**

**Expected Response (200)**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**cURL Example**:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=your.email@example.com&password=your_secure_password'
```

**Important Notes**:
- **Access Token**: Short-lived (30 minutes by default)
- **Refresh Token**: Long-lived (7 days by default)
- Save both tokens securely in your application

**Common Errors**:
- `400`: Incorrect email or password
- `422`: Missing username or password

---

#### 3. POST `/api/v1/auth/refresh` - Refresh Access Token

**Purpose**: Get new access and refresh tokens using a valid refresh token.

**How to test in Swagger UI**:
1. Navigate to `POST /api/v1/auth/refresh`
2. Click **"Try it out"**
3. In the JSON body, paste your refresh_token:

```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

4. Click **"Execute"**

**Expected Response (200)**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**cURL Example**:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/auth/refresh' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "refresh_token": "your_refresh_token_here"
}'
```

**Important Notes**:
- Both tokens are refreshed (you get new access + refresh tokens)
- Use this when your access_token expires
- Store the new tokens and discard the old ones

**Common Errors**:
- `403`: Invalid or expired refresh token

---

#### 4. POST `/api/v1/auth/test-token` - Test Access Token

**Purpose**: Verify that your access token is valid and get current user info.

**Prerequisites**: You must be **authorized** first (see Authorization section below).

**How to test in Swagger UI**:
1. **First, authorize** (see Authorization section)
2. Navigate to `POST /api/v1/auth/test-token`
3. Click **"Try it out"**
4. **No parameters needed**
5. Click **"Execute"**

**Expected Response (200)**:
```json
{
  "email": "your.email@example.com",
  "is_active": true,
  "is_superuser": false,
  "id": 1,
  "created_at": "2025-06-25T07:13:54.287884Z",
  "updated_at": null
}
```

**cURL Example**:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/auth/test-token' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer your_access_token_here'
```

**Common Errors**:
- `401`: Invalid or expired access token
- `403`: Token valid but user inactive

---

### 👤 User Management Endpoints

#### 5. GET `/api/v1/users/me` - Get Current User

**Purpose**: Get current authenticated user's profile information.

**Prerequisites**: You must be **authorized** first.

**How to test in Swagger UI**:
1. **First, authorize** with your access_token
2. Navigate to `GET /api/v1/users/me`
3. Click **"Try it out"**
4. Click **"Execute"**

**Expected Response (200)**:
```json
{
  "email": "your.email@example.com",
  "is_active": true,
  "is_superuser": false,
  "id": 1,
  "created_at": "2025-06-25T07:13:54.287884Z",
  "updated_at": null
}
```

---

#### 6. PUT `/api/v1/users/me` - Update Current User

**Purpose**: Update current user's email and/or password.

**Prerequisites**: You must be **authorized** first.

**How to test in Swagger UI**:
1. **First, authorize** with your access_token
2. Navigate to `PUT /api/v1/users/me`
3. Click **"Try it out"**
4. Fill the query parameters you want to update:
   - **password**: `new_password` (optional)
   - **email**: `new.email@example.com` (optional)
5. Click **"Execute"**

**Expected Response (200)**:
```json
{
  "email": "new.email@example.com",
  "is_active": true,
  "is_superuser": false,
  "id": 1,
  "created_at": "2025-06-25T07:13:54.287884Z",
  "updated_at": "2025-06-25T07:28:49.228418Z"
}
```

**cURL Example**:
```bash
curl -X 'PUT' \
  'http://localhost:8000/api/v1/users/me?email=new.email@example.com' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer your_access_token_here'
```

---

#### 7. GET `/api/v1/users/{user_id}` - Get User by ID

**Purpose**: Get any user's information by their ID (admin/superuser functionality).

**Prerequisites**: 
- You must be **authorized**
- You must be a **superuser** OR requesting your own user ID

**How to test in Swagger UI**:
1. **First, authorize** with your access_token
2. Navigate to `GET /api/v1/users/{user_id}`
3. Click **"Try it out"**
4. Enter a **user_id** (e.g., `1`)
5. Click **"Execute"**

**Expected Responses**:
- **200**: Returns user data (if you're superuser or it's your own ID)
- **400**: "The user doesn't have enough privileges" (if you're not superuser)

---

### 🏠 General Endpoints

#### 8. GET `/` - Root Endpoint

**Purpose**: Basic API welcome message.

**Response**:
```json
{
  "message": "Welcome to FastAPI Auth Template"
}
```

#### 9. GET `/health` - Health Check

**Purpose**: Check if the API is running properly.

**Response**:
```json
{
  "status": "healthy"
}
```

---

## 🔑 Authorization in Swagger UI

To access protected endpoints, you need to authorize first:

### Step-by-Step Authorization:

1. **Get your access_token** from the login response
2. **Copy the access_token** (without quotes)
3. **Click the 🔒 "Authorize" button** (top right in Swagger UI)
4. **Paste in the field**: `your_access_token_here`
   - ✅ Correct: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
   - ❌ Wrong: `"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."`
5. **Click "Authorize"**
6. **You're now authenticated** ✅

> **📝 Note**: Swagger UI automatically adds the "Bearer " prefix when you use the 🔒 Authorize button. You only need to paste the token itself, not "Bearer token".

### Visual Confirmation:
- The 🔒 icon will appear **closed** on protected endpoints
- You'll see `Authorization: Bearer ...` in the cURL examples

---

## 🔄 Complete Testing Workflow

### 1. First Time Setup:
```bash
# Register a new user
POST /api/v1/auth/register
{
  "email": "test@example.com",
  "password": "testpass123",
  "is_active": true,
  "is_superuser": false
}
```

### 2. Login and Get Tokens:
```bash
# Login (use Form Data)
POST /api/v1/auth/login
username: test@example.com
password: testpass123
```

### 3. Authorize in Swagger:
```
🔒 Authorize → Bearer your_access_token_here
```

### 4. Test Protected Endpoints:
```bash
# Test your token
POST /api/v1/auth/test-token

# Get your profile
GET /api/v1/users/me

# Update your profile
PUT /api/v1/users/me?email=newemail@example.com
```

### 5. Refresh When Needed:
```bash
# When access_token expires
POST /api/v1/auth/refresh
{
  "refresh_token": "your_refresh_token_here"
}
```

---

## ⚠️ Common Issues & Solutions

### "Arguments missing for parameters" Error
- **Cause**: `.env` file missing or incorrectly configured
- **Solution**: Create `.env` file with all required variables

### "Connection refused" Error  
- **Cause**: PostgreSQL not running
- **Solution**: `docker-compose up -d db`

### "403 Forbidden" on refresh
- **Cause**: Using access_token instead of refresh_token
- **Solution**: Use the longer refresh_token in the refresh endpoint

### "401 Unauthorized" on protected endpoints
- **Cause**: Not authorized or expired token
- **Solution**: 
  1. Get new access_token via login
  2. Authorize in Swagger UI with `Bearer token`

### "422 Validation Error"
- **Cause**: Invalid data format or missing required fields
- **Solution**: Check the request body format and required fields

---

## 🚀 Next Steps

Once you've tested the API manually:

1. **Build a frontend** that consumes this API
2. **Implement token storage** (localStorage, httpOnly cookies, etc.)
3. **Handle token expiration** with automatic refresh
4. **Add role-based access control** for different user types
5. **Implement OAuth providers** (Google, GitHub, etc.)

---

## 📖 Related Documentation

- **Setup Guide**: [README.md](./README.md)
- **Theory & Architecture**: [THEORY.md](./THEORY.md) *(coming soon)*
- **FastAPI Documentation**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **JWT Standard**: [https://jwt.io](https://jwt.io) 