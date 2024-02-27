from pydantic import BaseModel
from datetime import date

class expense(BaseModel):
    amount : float
    description : str
    date: date
