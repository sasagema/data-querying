from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional, Type, Dict, Any 

from sqlalchemy.orm import Session
from app.api.v1.endpoints import post
from app.api.v1.endpoints import user
from app.api.v1.endpoints import insert

api_router = APIRouter()

api_router.include_router(post.router, prefix="/v1", tags=["posts"])
api_router.include_router(user.router, prefix="/v1", tags=["users"])
api_router.include_router(insert.router, prefix="/v1", tags=["insert"])