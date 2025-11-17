from sqlalchemy.orm import Session
from app import models, schemas

def create_review(db: Session, review: schemas.ReviewCreate):
    new = models.Review(**review.dict())
    db.add(new)
    db.commit()
    return new

def get_reviews(db: Session):
    return db.query(models.Review).all()
