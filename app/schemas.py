from pydantic import BaseModel, EmailStr
from typing import Optional, Literal

class ContactCreate(BaseModel):
    inquiry_type: Literal["General", "Collaboration"]

    first_name: str
    last_name: Optional[str] = None

    email: EmailStr

    state: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None

    message: str
