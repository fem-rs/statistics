from app.infrastructure.database.db import AsyncSessionLocal

async def inject_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        except Exception as err:
            raise err
        finally:
            await db.close() # Fuck memory leaks
