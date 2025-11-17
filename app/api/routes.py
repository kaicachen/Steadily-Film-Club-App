from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas
from app.crud import films, members, reviews

router = APIRouter()

@router.post("/members", response_model=schemas.Member)
def create_member(m: schemas.MemberCreate, db: Session = Depends(get_db)):
    return members.create_member(db, m)

@router.get("/members", response_model=list[schemas.Member])
def get_members(db: Session = Depends(get_db)):
    return members.get_members(db)

@router.post("/films", response_model=schemas.Film)
def create_film(f: schemas.FilmCreate, db: Session = Depends(get_db)):
    return films.create_film(db, f)

@router.get("/films", response_model=list[schemas.Film])
def get_films(db: Session = Depends(get_db)):
    return films.get_films(db)

@router.put("/films/{film_id}", response_model=schemas.Film)
def update_film(film_id: int, f: schemas.FilmCreate, db: Session = Depends(get_db)):
    return films.update_film(db, film_id, f)

@router.delete("/films/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db)):
    return films.delete_film(db, film_id)

@router.post("/reviews", response_model=schemas.Review)
def create_review(r: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return reviews.create_review(db, r)
