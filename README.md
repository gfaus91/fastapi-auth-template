# fastapi-auth-template

🚀 **Production-ready FastAPI template** with:

- ✅ JWT authentication (access & refresh tokens)
- ✅ PostgreSQL integration via SQLAlchemy
- ✅ Alembic migrations
- ✅ Environment-based config management
- ✅ Modular architecture for easy scaling
- ✅ Docker-ready (optional)

## 📦 Tech Stack

- **FastAPI** — high-performance Python web framework
- **PostgreSQL** — relational database
- **SQLAlchemy** — ORM for database interactions
- **Alembic** — for database migrations
- **PyJWT** — secure token generation
- **Passlib** — password hashing (bcrypt)
- **Pydantic** — data validation and settings

---

## ⚙️ Features

- 🔒 User registration & login with hashed passwords  
- 🔁 Token-based auth with **access** and **refresh** tokens  
- 🧩 Scalable, clean project structure  
- 🔧 Environment variables with `.env` support  
- 🧪 Basic testing setup (optional extension)

---

## 📂 Project Structure

```
app/
├── api/             # Routes and request handling
├── core/            # Settings, security, token logic
├── db/              # DB sessions and base model
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas
├── services/        # Business logic
└── main.py          # App entrypoint
alembic/             # Migrations
.env.example         # Environment config template
requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Docker & Docker Compose

### 1. Clone the repo

```bash
git clone https://github.com/gfaus91/fastapi-auth-template.git
cd fastapi-auth-template
```

### 2. Create virtual environment

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create `.env` file:

```bash
# Windows:
copy .env.example .env
# macOS/Linux:
cp .env.example .env
```

**Important**: Edit `.env` and update the `SECRET_KEY` with a secure key.

### 5. Start PostgreSQL

```bash
docker-compose up -d db
```

### 6. Setup Database

```bash
# Apply database migrations
alembic upgrade head
```

> 💡 **Note**: For new projects using this as a template, consider generating fresh migrations with `alembic revision --autogenerate -m "Initial migration"` after removing existing ones.

### 7. Start the application

```bash
uvicorn app.main:app --reload
```

### 8. Test the API

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Full Docker Setup (Alternative)

If you prefer to run everything in Docker:

```bash
docker-compose up --build
```

---

## 📚 Documentation

- **📖 API Guide**: See [API_GUIDE.md](./API_GUIDE.md) for complete API documentation and testing guide
- **🧠 Theory & Architecture**: See [THEORY.md](./THEORY.md) for understanding how JWT authentication works
- **🔗 Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs) - Interactive API documentation
- **📋 ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc) - Alternative API documentation

## 🧪 Quick Test

1. **Register**: `POST /api/v1/auth/register` with your email/password
2. **Login**: `POST /api/v1/auth/login` to get JWT tokens
3. **Authorize**: Use access_token in Swagger UI 🔒 button
4. **Test**: Try protected endpoints like `GET /api/v1/users/me`

> **Detailed testing guide**: See [API_GUIDE.md](./API_GUIDE.md)

---

## 📌 Roadmap

- [ ] OAuth (Google/GitHub) login
- [ ] Role-based access control (RBAC)
- [ ] Admin panel (optional)

---

## 👤 Author

**Guillermo Faus Roche**  
Full-Stack Developer | Python · FastAPI · DevOps · AI  
[LinkedIn](https://www.linkedin.com/in/guillermofausroche) · [GitHub](https://github.com/gfaus91)

---

## 🤖 Development Process

This project was developed using **modern AI-assisted development** practices, leveraging:

- **🧠 Claude Sonnet 4** - Architecture design and code generation
- **💻 Cursor IDE** - AI-powered code completion and editing
- **🔧 Industry Standards** - Following FastAPI, SQLAlchemy, and JWT best practices

**Why AI-Assisted Development?**
- ✅ **Higher code quality** through automated best practices
- ✅ **Faster development cycles** with intelligent code generation  
- ✅ **Comprehensive documentation** automatically generated
- ✅ **Modern patterns** implemented from day one
- ✅ **Reduced bugs** through AI-powered code review

This approach demonstrates **efficiency in modern software development** while maintaining **full understanding** of the underlying architecture and design decisions.

> 💡 **Transparency Note**: While AI tools accelerated development, all architectural decisions, security implementations, and code organization reflect solid software engineering principles and thorough understanding of the technologies used.

---

## 📝 License

MIT License. Feel free to use and modify.

## 🛠️ Common Issues

### "Arguments missing for parameters" Error
Make sure you created the `.env` file with all required variables.

### "Connection refused" Error
PostgreSQL is not running. Start it with:
```bash
docker-compose up -d db
```

### UTF-8 Encoding Error
Recreate your `.env` file with UTF-8 encoding (no BOM).

## 🔄 Database Migrations Workflow

When you modify your models:

```bash
# 1. Generate migration
alembic revision --autogenerate -m "Add new field to users"

# 2. Review the generated migration file in alembic/versions/

# 3. Apply the migration
alembic upgrade head
```