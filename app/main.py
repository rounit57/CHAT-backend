from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import contact
from app.database import Base, engine
from app.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CHAT Contact API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact.router)
