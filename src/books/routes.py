# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import APIRouter, status, Depends 
from src.books.schemas import Book
from src.db.main import get_session
from src.books.service import BookService
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from .schemas import BookCreateModel, BookUpdateModel
from uuid import UUID

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model = List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/", status_code = status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book
    # print("INFO ==>> data received ")
    # return book_data.model_dump()

@book_router.get("/{book_uid}", response_model=Book)
async def get_book(book_uid: UUID, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 

@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(book_uid: UUID, book_update_data: BookUpdateModel, session: AsyncSession = Depends(get_session)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book:
        return updated_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete("/{book_uid}")
async def delete_book(book_uid: UUID, session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_book(book_uid, session)
    if book_to_delete:
        return {}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
