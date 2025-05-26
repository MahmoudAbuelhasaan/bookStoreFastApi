from fastapi import APIRouter,Depends,Query,HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from typing import Optional
from sqlalchemy import or_ , desc
from models.book import Book
from schemas.book import BookCreateSchema,BookResponseSchema,BookUpdateSchema

router = APIRouter(prefix='/api/books')

@router.post('/',response_model=BookResponseSchema)
def create_book(book:BookCreateSchema,db:Session=Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# @router.get('/',response_model=List[BookResponseSchema])
# def list_books_api(db:Session=Depends(get_db)):
#     books = db.query(Book)
#     return books

@router.get('/{book_id}',response_model=BookResponseSchema)
def book_detail_api(book_id:int,db:Session=Depends(get_db)):
    book = db.query(Book).filter(Book.id==book_id).first()
    if not book:
       raise HTTPException(status_code=404,detail="book not found")
        
    return book


@router.delete('/{book_id}',status_code=204)
def book_delete_api(book_id:int,db:Session=Depends(get_db)):
    book = db.query(Book).filter(Book.id==book_id).first()
    if not book:
       raise HTTPException(status_code=404,detail="book not found")
    
    db.delete(book)
    db.commit()
        
    return {"detil":"Book deleted successfuly"}


@router.put('/{book_id}',response_model=BookResponseSchema)
def book_update_api(book_id:int,book_update:BookUpdateSchema,db:Session=Depends(get_db)):
    book = db.query(Book).filter(Book.id==book_id).first()
    if not book:
       raise HTTPException(status_code=404,detail="book not found")
    

    update_data = book_update.model_dump() # convert to dict key:value

    for k,v in update_data.items():
        setattr(book,k,v)

    db.commit()
    db.refresh(book)
    return book


@router.get('/',response_model=List[BookResponseSchema])
def list_books_api(
    search:Optional[str] = Query(None,description='search by title or description'),
    order_by:Optional[str] = Query("id",regex="^-?(title|id)$",description='order by title or id'),
    db:Session=Depends(get_db)

    
    ):
    books = db.query(Book)

    if search:
        books = books.filter(or_(Book.title.ilike(f'%{search}%'),Book.description.ilike(f'%{search}%')))


    if order_by == "title":
        books = books.order_by(Book.title) 

    elif order_by == "-title":
        books = books.order_by(desc(Book.title)) 

    elif order_by == "-id":
        books = books.order_by(desc(Book.id)) 
    
    return books