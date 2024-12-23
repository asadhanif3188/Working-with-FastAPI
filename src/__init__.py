from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting up...")
    await init_db()
    yield
    print("Server is Shutting down...")

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for books.",
    version = version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
