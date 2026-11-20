from pydantic import BaseModel,EmailStr
from typing import Optional

class student_basic(BaseModel):
    name: str
    age : int
    email: EmailStr
    phone: Optional[int] = None #This is the Optional one and by default is set to the Null
    marks: int