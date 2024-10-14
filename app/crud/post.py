
from __future__ import annotations
from sqlalchemy.orm import Session
from app.model.models import Post, User, Tag
from app.model.schemas import PostCreate, PostUpdate
from app.utils.filters import apply_filters
from typing import Optional, List

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session, filters: None):
    query = db.query(Post)
    query = apply_filters(query, filters)
    return query.all()

def create_post(db: Session, post: PostCreate):    
    db_post = Post(**post.model_dump()) 
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post_in: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
            return
    post_data = post_in.model_dump()
    for field, value in post_data.items():
        setattr(db_post, field, value)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(User.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

def add_post_tags(db: Session, post_id: int, tags: List[int]):
    db_post = db.query(Post).filter(User.id == post_id).first()
    if not db_post:
        raise ValueError("Post not found")
    db_tags = db.query(Tag).filter(Tag.id.in_(tags)).all()
    if not db_tags:
        raise ValueError("Tags not found")
    for db_tag in db_tags:
        if not db_post.tags.__contains__(db_tag):
            db_post.tags.append(db_tag)
    db.commit()
    db.refresh(db_post)
    return db_post
