from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Review(Base):

    __tablename__='review'
    id= Column(Integer,primary_key=True)
    text = Column(String,nullable=False)
    rating = Column(Integer)

    book_id = Column(Integer,ForeignKey('book.id'))
    book = relationship('Book', back_populates='reviews')