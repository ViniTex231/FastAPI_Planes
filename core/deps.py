import sys
default_path = "C:\\Users\\tev3ca\\Desktop\\FastAPI_Planes"
sys.path.append(default_path)

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()