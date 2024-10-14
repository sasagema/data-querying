from __future__ import annotations

from sqlalchemy.orm import Session
from app.model.models import User
from app.model.schemas import UserCreate, UserUpdate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session,user_id: int, user_in: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
            return
    user_data = user_in.model_dump()
    for field, value in user_data.items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
    

