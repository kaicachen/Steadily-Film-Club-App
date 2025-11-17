from pydantic import BaseModel
from datetime import date
from typing import Optional

class MemberBase(BaseModel):
    member_name: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int
    class Config: orm_mode = True

# ---- Films ----

class FilmBase(BaseModel):
    film_name: str
    film_date_discussed: Optional[date] = None
    film_year_released: Optional[int] = None
    film_director: Optional[str] = None
    film_host: Optional[int] = None

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    id: int
    class Config: orm_mode = True

# ---- Reviews ----

class ReviewBase(BaseModel):
    review_initial_rating: int
    review_like: str
    review_final_rating: int

class ReviewCreate(ReviewBase):
    member_id: int
    film_id: int

class Review(ReviewBase):
    member_id: int
    film_id: int
    class Config: orm_mode = True
