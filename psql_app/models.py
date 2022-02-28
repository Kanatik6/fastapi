from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from database import Base


class PostModel(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    descriptions = Column(String)
    likes = Column(Integer,default=0)
    unlikes = Column(Integer,default=0)
    date = Column(DateTime,default=datetime.now())

    author_id = Column(Integer,ForeignKey('authors.id'))
    author = relationship("AuthorModel",back_populates='posts')

class AuthorModel(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)

    posts = relationship('PostModel',back_populates='author')
