import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Comments(Base):
    __tablename__ = 'Comments'


    id_comment=Column(Integer, primary_key=True)
    comment = Column(String(250))
    likes= Column(Integer)
    date = Column(Date)
    

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_post = Column(Integer, primary_key=True)
    description = Column(String(250))
    likes = Column(Integer)
    media = Column(String(250), nullable=False)
    comment_id = Column(Integer, ForeignKey('Comments.id_comment'))
    comment = relationship(Comments)

class Stories(Base):
    __tablename__ = 'Stories'


    id_stories=Column(Integer, primary_key=True)
    media = Column(String(250))
    philter= Column(String(250))
    date = Column(Date)
    

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    bio = Column(String(250), nullable=False)
    img = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id_post'))
    post = relationship(Post)
    story_id = Column(Integer, ForeignKey('Stories.id_stories'))
    story = relationship(Stories)
    





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')