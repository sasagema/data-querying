from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any, Union, Annotated
from app.model.schemas import PostCreate, Post, PostResponse, PostFilterParams, CommentCreate, CommentUpdate, TagCreate, PostTags
from app.crud import post as crud_post
from app.crud import comment as crud_comment
from app.crud import tag as crud_tag
from app.db.session import get_db

router = APIRouter()

@router.get("/posts/", response_model=List[PostResponse | Post])
async def read_posts(filter_query: Annotated[PostFilterParams, Query()], db: Session = Depends(get_db)):
    filters = dict(filter_query.__dict__.items())
    include = filters.get('include')
    posts = crud_post.get_posts(db, filters)
    if include:
        return [PostResponse.include_relations(post, include) for post in posts]
    return [Post.model_validate(post) for post in posts]

@router.get("/posts/{post_id}", response_model=Union[PostResponse, Post])
def read_post(post_id: int, include: Union[str, None] = None, db: Session = Depends(get_db)):
    db_post = crud_post.get_post(db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail= "Post not found")
    if include:
        # return db_post
        return PostResponse.include_relations(db_post, include)
    return Post.model_validate(db_post)

@router.post("/posts", response_model=PostCreate)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud_post.create_post(db, post)

@router.post("/posts/{post_id}/comments", response_model=CommentCreate)
def create_post_comment(post_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    db_post = crud_post.get_post(db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail= "Post not found")
    if db_post and comment:
        return crud_comment.create_comment(db, comment)
    return None

@router.post("/posts/{post_id}/tags", response_model=Union[PostResponse, Post])
def add_post_tags(post_id: int, tags_in: PostTags, db: Session = Depends(get_db)):
    tags_to_add = []
    for tag_name in tags_in.tags:
        db_tag = crud_tag.get_tag_by_name(db, tag_name)
        if db_tag:
            tags_to_add.append(db_tag.id)
        else:
            new_tag = crud_tag.create_tag(db, TagCreate(name=tag_name))
            if new_tag:
                tags_to_add.append(new_tag.id)
    try:
        db_post = crud_post.add_post_tags(db, post_id, tags_to_add)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return PostResponse.include_relations(db_post, "tags")
   