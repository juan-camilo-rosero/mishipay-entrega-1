from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    email: str
    tel: int
    name: str
    money: int
    transactions: Optional[list] = []