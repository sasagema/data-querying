from __future__ import annotations

from sqlalchemy.orm import Session
from app.model.models import Tag
from app.model.schemas import TagCreate

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()
def get_tag_by_name(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()
def get_tags(db: Session):
    return db.query(Tag).all()

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
    return db_tag