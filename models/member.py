from datetime import date
from pydantic import BaseModel

class Member(BaseModel):
    name: str
    age: int
    dateOfBirth: date
    gender: str
    role: str