from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

async_engine = AsyncEngine(
    create_engine(
        url = Config.DATABASE_URL,
        echo= True
    )
)

# this function will help us to connect with db
# at the start of application.

async def init_db():
    async with async_engine.begin() as conn:
        # *** these statements are just for testing**
        # statment = text("Select 'hello';")
        # result = await conn.execute(statment)
        # print(result.all())
        # ******************************************
        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_= AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session