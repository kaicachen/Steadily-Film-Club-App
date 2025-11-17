from sqlalchemy.orm import Session
from app import models, schemas

def create_film(db: Session, film: schemas.FilmCreate):
    new = models.Film(**film.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_films(db: Session):
    return db.query(models.Film).all()

def get_film(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()

def update_film(db: Session, film_id: int, film: schemas.FilmCreate):
    db_film = get_film(db, film_id)
    if db_film:
        for key, value in film.dict().items():
            setattr(db_film, key, value)
        db.commit()
        db.refresh(db_film)
    return db_film

def delete_film(db: Session, film_id: int):
    db_film = get_film(db, film_id)
    if db_film:
        db.delete(db_film)
        db.commit()
    return db_film
