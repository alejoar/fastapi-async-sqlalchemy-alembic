from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from alembic import command, config

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"

Base: DeclarativeMeta = declarative_base()


async_engine = create_async_engine(DATABASE_URL, echo=True)


def run_upgrade(connection, cfg):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


async def run_async_upgrade():
    async with async_engine.begin() as conn:
        await conn.run_sync(run_upgrade, config.Config("alembic.ini"))
