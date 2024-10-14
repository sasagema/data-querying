from __future__ import annotations

from sqlalchemy.orm import Session
from app.model.models import Comment
from app.model.schemas import CommentCreate

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comments(db: Session):
    return db.query(Comment).all()

def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment