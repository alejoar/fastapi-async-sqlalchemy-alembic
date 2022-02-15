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
Note: App halts on startup because the db upgrade is not working. Remove the function decorated with `@app.on_event("startup")` to make the app work.

## Database
### cli: cenerate revision (works)

```
alembic revision --autogenerate
```

### cli: upgrade (works)

```
alembic upgrade head
```

### programmatically: upgrade (doesn't work)

See `run_async_upgrade` in `database.py` called from `main.py` on app startup.
