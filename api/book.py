from fastapi import APIRouter,Depends,Query
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from models.book import Book
from schemas.book import BookCreateSchema,BookResponseSchema

router = APIRouter(prefix='/api/books')

@router.post('/',response_model=BookResponseSchema)
def create_book(book:BookCreateSchema,db:Session=Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get('/',response_model=List[BookResponseSchema])
def list_books_api(db:Session=Depends(get_db)):
    books = db.query(Book)
    return books