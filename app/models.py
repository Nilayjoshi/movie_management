from sqlalchemy import Column, Integer, String, CheckConstraint
from .database import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    director = Column(String)
    release_year = Column(Integer, CheckConstraint('release_year >= 1000 AND release_year <= 9999'))
    genre = Column(String)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 10'))
