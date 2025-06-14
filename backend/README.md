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

run the application

```sh
uvicorn app.main:app --reload
```

```sh
curl http://localhost:8000/api/v1/
{"message":"Hello, World!"}%
```

## Migrations
