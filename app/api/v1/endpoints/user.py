from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Union, Optional, Any, Dict, Annotated
from app.model.schemas import UserCreate, User, UserResponse, UserUpdate
from app.crud import user as crud_user
from app.db.session import get_db

router = APIRouter()


@router.get("/users/", response_model=List[Union[UserResponse | User]])
def read_users( db: Session = Depends(get_db)):
    users = crud_user.get_users(db)
    return users

@router.get("/users/{user_id}", response_model=Union[UserResponse | User], response_model_exclude_unset=True)
def read_user(user_id: int, include: Union[str, None] = None,  db: Session = Depends(get_db)):
    user = crud_user.get_user(db,user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    if include: 
        return UserResponse.include_relations(user, include)
    return User.model_validate(user)

@router.post("/users/", response_model=UserCreate)
def create_user(post: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, post) 

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    user = crud_user.update_user(db, user_id, user)
    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    return user
