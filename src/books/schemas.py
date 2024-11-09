import uuid
from pydantic import BaseModel
from datetime import datetime, date
from typing import List

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    update_at: datetime


# class BookDetailModel(Book):
#     reviews: List[ReviewModel]
#     tags: List[TagModel]

class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

