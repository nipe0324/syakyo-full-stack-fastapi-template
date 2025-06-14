# Backend

## Requirements

- Docker
- uv for Python package and environment management

## Setup

```sh
cd backend
uv sync

# activate the virtual environment
source .venv/bin/activate
```

## Run

start the database

```sh
cd syakyo-full-stack-fastapi-template
docker compose up -d
```

run the application

```sh
uvicorn app.main:app --reload
```

## Migrations

run migration

```sh
alembic upgrade head
```

create migration file

```sh
alembic revision -m "<migration description>"

# auto generate migration file
alembic revision --autogenerate -m "<migration description>"
```

connect to database

```sh
docker compose exec db psql -U postgres -d app
```
