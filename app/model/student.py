from typing import Optional, List
from pydantic import BaseModel, Field


class createStudentModel(BaseModel):
    id: str = Field(min_length=10, max_length=10)
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    gender: Optional[str]
    age: Optional[int]
    height: Optional[int]
    weight: Optional[float]
    hobby: Optional[List[str]]
    country: Optional[str]
    city: Optional[str]


class updateStudentModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    gender: Optional[str]
    age: Optional[int]
    height: Optional[int]
    weight: Optional[float]
    hobby: Optional[List[str]]
    country: Optional[str]
    city: Optional[str]
