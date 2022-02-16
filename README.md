# fastapi-async-sqlalchemy-alembic

## Install dependencies

```
pip install -r requirements.txt
```

## Run app

Run a Postgres instance with docker:

```
docker run -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:alpine
```

Run the app:

```
uvicorn main:app --reload
```

## Database
### cli: cenerate revision

```
alembic revision --autogenerate
```

### cli: upgrade

```
alembic upgrade head
```

### programmatically: upgrade

See `run_async_upgrade` in `database.py` called from `main.py` on app startup.
