from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.services.email_service import send_contact_email
from app.logger import get_logger

router = APIRouter(prefix="/api/contact", tags=["Contact"])
logger = get_logger("contact")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def submit_contact(data: schemas.ContactCreate, db: Session = Depends(get_db)):
    try:
        entry = models.ContactSubmission(**data.dict())
        db.add(entry)
        db.commit()

        send_contact_email(data.dict())

        logger.info(f"Contact submission saved for {data.email}")

        return {
            "success": True,
            "message": "Thank you for contacting us."
        }

    except Exception as e:
        logger.error(f"Submission failed: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
