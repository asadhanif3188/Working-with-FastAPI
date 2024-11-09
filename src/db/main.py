from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(
    create_engine(
        url = Config.DATABASE_URL,
        echo= True
    )
)

# this function will help us to connect with db
# at the start of application.

async def init_db():
    async with engine.begin() as conn:
        statment = text("Select 'hello';")
        result = await conn.execute(statment)
        print(result.all())
