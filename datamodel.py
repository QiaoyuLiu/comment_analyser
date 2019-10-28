from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String(256))
    note = Column(Integer)
    entity = relationship('Entity', back_populates='comments')


# The schema for entity table
class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity = Column(String(256))
    type = Column(String(20))
    salience = Column(FLOAT(precision=10, scale=2))
    magnitude = Column(FLOAT(precision=10, scale=2))
    score = Column(FLOAT(precision=10, scale=2))
    weight = Column(FLOAT(precision=10, scale=2))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship('Comment', back_populates='entity')

