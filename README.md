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

### 6. Run database migrations

```bash
alembic upgrade head
```

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

## 🧪 Example Users

Use the `/auth/register` and `/auth/login` endpoints to register and get a token.  
All protected routes require `Authorization: Bearer <token>` header.

---


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