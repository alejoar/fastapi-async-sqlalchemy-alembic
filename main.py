from fastapi import FastAPI

from database import run_async_upgrade

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await run_async_upgrade()


@app.get("/")
def read_root():
    return {"Hello": "World"}
