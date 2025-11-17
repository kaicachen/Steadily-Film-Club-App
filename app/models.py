from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    member_name = Column(String, nullable=False)

    reviews = relationship("Review", back_populates="member")

class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    film_name = Column(String, nullable=False)
    film_date_discussed = Column(Date)
    film_year_released = Column(Integer)
    film_director = Column(String)
    film_host = Column(Integer, ForeignKey("members.id"))

    host = relationship("Member")
    reviews = relationship("Review", back_populates="film")

class Review(Base):
    __tablename__ = "reviews"

    member_id = Column(Integer, ForeignKey("members.id"), primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    review_initial_rating = Column(Integer)
    review_like = Column(String)
    review_final_rating = Column(Integer)

    member = relationship("Member", back_populates="reviews")
    film = relationship("Film", back_populates="reviews")
