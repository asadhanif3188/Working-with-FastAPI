import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import APIRouter, status 
from src.books.schemas import Book
from typing import List

book_router = APIRouter()

book_router.get("/books", response_model = List[Book])
async def get_all_books():
    return "All books"

book_router.post("/books", status_code = status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    # add record to db
    return new_book

book_router.get("/books/{book_id}")
async def get_book():
    return "a book"

book_router.delete("/books/{book_id}")
async def delete_book():
    return "book deleted"
