import uuid
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List

class Book(BaseModel):
    uid: uuid.UUID | None = None
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    # created_at: datetime = Field(default_factory=datetime.now)
    # update_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime | None = None
    update_at: datetime | None = None
    class Config:
        from_attributes = True


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
    published_date: date
    page_count: int
    language: str

# class BookDetailModel(Book):
#     reviews: List[ReviewModel]
#     tags: List[TagModel]