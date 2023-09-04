from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Airpolution(BaseModel):
    nox: float
    co: float
    so2: float
    _id: str
    