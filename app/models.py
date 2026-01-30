from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class ContactSubmission(Base):
    __tablename__ = "contact_submissions"

    id = Column(Integer, primary_key=True, index=True)

    inquiry_type = Column(
        Enum("General", "Collaboration"),
        nullable=False
    )

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))

    email = Column(String(255), nullable=False)

    state = Column(String(100))
    city = Column(String(100))
    zipcode = Column(String(20))

    message = Column(Text, nullable=False)

    status = Column(
        Enum("NEW", "REVIEWED", "CONTACTED", "CLOSED"),
        default="NEW"
    )

    created_at = Column(TIMESTAMP, server_default=func.now())
