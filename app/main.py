from fastapi import FastAPI
from app.db.session import engine
from app.api.v1.api import api_router
from app.db.session import Base, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api")

