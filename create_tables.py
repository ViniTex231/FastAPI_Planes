from core.configs import settings
from core.database import engine
from models import __all_models

async def create_tables() -> None:
    import models.__all_models
    print('Creating tables from DB...')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tables created with successfully")

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())