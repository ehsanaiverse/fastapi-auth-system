# FastAPI Authentication System

A complete authentication system built with FastAPI, featuring user registration, JWT-based login, password management, and OTP-based password recovery.

## 🚀 Features

- ✅ **User Registration** - Create new user accounts with username and email
- 🔐 **JWT Authentication** - Secure token-based authentication
- 🔑 **User Login** - Login with email or username
- 🔄 **Change Password** - Allow users to update their passwords
- 📧 **Forget Password** - OTP-based password recovery
- ✔️ **OTP Verification** - Verify OTP and reset password
- 🗄️ **SQLAlchemy ORM** - Database operations with SQLAlchemy
- 🔒 **Password Hashing** - Secure password storage with bcrypt

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- SQLite/PostgreSQL/MySQL (database)

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/ehsanaiverse/fastapi-auth-system.git
cd fastapi-auth-system
```

2. **Create a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the project root

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db
```

5. **Run the application**

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 🔌 API Endpoints

### Home
- `GET /` - Welcome message

### Authentication
- `POST /register` - Register a new user
- `POST /login` - Login and get access token
- `POST /change` - Change password
- `POST /forget` - Request OTP for password reset
- `POST /verify-otp` - Verify OTP and reset password

## 📝 Request Examples

### Register User
```json
POST /register
{
  "username": "ehsan",
  "email": "ehsan@example.com",
  "password": "ehsan123"
}
```

### Login
```json
POST /login
{
  "email": "ehsan@example.com",
  "password": "ehsan123"
}
```

### Change Password
```json
POST /change
{
  "email": "ehsan@example.com",
  "old_password": "ehsan123",
  "new_password": "newEhsan123"
}
```

### Forget Password (Request OTP)
```json
POST /forget
{
  "email": "ehsan@example.com"
}
```

### Verify OTP and Reset Password
```
POST /verify-otp
{
  "email": "ehsan@example.com",
  "otp": 123456,
  "new_password": "NewPassword789"
}
```

## 🏗️ Project Structure

```
fastapi-auth-system/
├── main.py              # Application entry point
├── routers.py           # API route handlers
├── models.py            # Database models
├── schemas.py           # Pydantic schemas
├── auth.py              # Authentication utilities
├── db.py                # Database configuration
├── dependency.py        # Dependency injection
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

## 🔧 Configuration

Update the `.env` file with your configuration:

```env
SECRET_KEY=your-super-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./test.db
```

For production, use a strong secret key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## 🗃️ Database

The application uses SQLAlchemy ORM and supports multiple databases:

- **SQLite** (default): `sqlite:///./test.db`
- **PostgreSQL**: `postgresql://user:password@localhost/dbname`
- **MySQL**: `mysql://user:password@localhost/dbname`

Update the `DATABASE_URL` in your `.env` file accordingly.

## 🧪 Testing

You can test the API using:
- **Swagger UI**: Built-in at `/docs`
- **Postman**: Import the endpoints
- **cURL**: Command-line testing
- **Python requests**: Write test scripts

## 🛡️ Security Features

- ✅ Password hashing with bcrypt
- ✅ JWT token authentication
- ✅ OTP-based password recovery
- ✅ Input validation with Pydantic
- ✅ SQL injection prevention with SQLAlchemy ORM

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👤 Author

**Ehsan Ullah**
- GitHub: [@ehsanaiverse](https://github.com/ehsanaiverse)
- Email: ehsanullah.contact@gmail.com

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [PassLib](https://passlib.readthedocs.io/) - Password hashing

## 📞 Support

If you have any questions or issues, please open an issue on GitHub.

---

⭐ **Star this repository if you find it helpful!**