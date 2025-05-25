from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from core.database import Base


class Author(Base):

    __tablename__='author'
    id= Column(Integer,primary_key=True)
    name = Column(String,nullable=False)

    # relationship

    books = relationship('Book',back_populates="author")

