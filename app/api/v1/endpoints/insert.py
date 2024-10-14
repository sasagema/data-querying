from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.model.schemas import UserCreate, User
from app.crud import data
from app.db.session import get_db

router = APIRouter()

@router.get("/insert/")

def insert_data(db: Session = Depends(get_db)):
    response = data.insert_data(db)
    return response