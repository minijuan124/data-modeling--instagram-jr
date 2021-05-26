import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    profile = relationship("Profile", backref='user', uselist=False)
    posts = relationship("Post", backref='user')
    followers = relationship("FollowRequest", backref='followed', foreign_keys=["followed_id"])
    followeds = relationship("FollowRequest", backref='follower', foreign_keys=["follower_id"])

class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    bio = Column(String(250), nullable =False)
    name = Column(String(250), nullable =False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    media_type = Column(String(250), nullable =False)
    caption = Column(String(250), nullable =False)
    location = Column(String(250), nullable =False)
    date = Column(DateTime, default= func.now())

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime, default= func.now())
    text = Column(String(250), nullable =False)

class FollowRequest(Base):
    __tablename__ = 'follow_request'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True) 
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))
    status = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e