from pydantic import BaseModel
# from typing import Optional

class Transaction(BaseModel):
    sender_email: str
    reciever_email: str
    sender_name: str
    reciever_name: str
    amount: float