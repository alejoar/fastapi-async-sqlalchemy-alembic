# fastapi-async-sqlalchemy-alembic

## Install dependencies

```
pip install -r requirements.txt
```

## Run app

Halts on startup because the db upgrade is not working. Remove the function decorated with `@app.on_event("startup")` to make the app work.

```
uvicorn main:app --reload
```


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
