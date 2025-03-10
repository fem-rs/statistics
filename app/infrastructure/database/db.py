from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# should probably put this in a config somewhere

from app.infrastructure.config import read_config

async_engine = create_async_engine(read_config()["database"][0]["url"], echo=True)

AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def init_db():
    try:    
        async with async_engine.begin() as conn:
            tables = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())

            if "form" not in tables:
                await conn.run_sync(Base.metadata.create_all)
    except Exception as err:
        raise err