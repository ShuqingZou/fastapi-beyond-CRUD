# FastAPI Beyond CRUD 

This is the source code for the [FastAPI Beyond CRUD](https://youtube.com/playlist?list=PLEt8Tae2spYnHy378vMlPH--87cfeh33P&si=rl-08ktaRjcm2aIQ) course. The course focuses on FastAPI development concepts that go beyond the basic CRUD operations.

For more details, visit the project's [website](https://jod35.github.io/fastapi-beyond-crud-docs/site/).

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Project Setup](#project-setup)
4. [Running the Application](#running-the-application)
5. [Running Tests](#running-tests)
6. [Continuous Integration & Deloyment](#continuous-integration--deployment)
7. [Contributing](#contributing)

## Getting Started
Follow the instructions below to set up and run your FastAPI project.

### Prerequisites
Ensure you have the following installed:

- Python >= 3.10
- PostgreSQL
- Redis
- Docker & Docker Compose

### Project Setup
1. Clone the project repository:
    ```bash
    git clone https://github.com/jod35/fastapi-beyond-CRUD.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd fastapi-beyond-CRUD/
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    env\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
5. Configure environment variables:
    ```bash
    cp .env.example .env
    ```
   Then update `.env` with valid database and email credentials:
   ```ini
   DATABASE_URL=postgresql+asyncpg://postgres:testpass@db:5432/bookly
   JWT_SECRET=<your-secret-key>
   JWT_ALGORITHM=HS256
   REDIS_URL=redis://redis:6379/0
   MAIL_USERNAME=<your-email>
   MAIL_PASSWORD=<your-email-password>
   MAIL_SERVER=smtp.ethereal.email
   MAIL_PORT=587
   MAIL_FROM=<your-email>
   MAIL_FROM_NAME="FastAPI Beyond CRUD"
   DOMAIN=http://localhost:8000

6. Run database migrations to initialize the database schema:
    ```bash
    alembic upgrade head
    ```

7. Open a new terminal and ensure your virtual environment is active. Start the Celery worker (Linux/Unix shell):
    ```bash
    sh runworker.sh
    ```

## Running the Application
Start the application:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```
Alternatively, you can run the application using Docker:
```bash
docker compose up -d
```
To check running services:
```bash
docker compose ps
```
## Running Tests
Run the tests using this command
```bash
pytest
```

## Contributing
I welcome contributions to improve the documentation! You can contribute [here](https://github.com/jod35/fastapi-beyond-crud-docs).