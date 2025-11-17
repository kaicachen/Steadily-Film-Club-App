from sqlalchemy.orm import Session
from app import models, schemas

def create_member(db: Session, member: schemas.MemberCreate):
    new = models.Member(member_name=member.member_name)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_members(db: Session):
    return db.query(models.Member).all()

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.id == member_id).first()
