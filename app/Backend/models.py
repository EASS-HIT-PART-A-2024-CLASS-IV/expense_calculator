from pydantic import BaseModel
from datetime import date

class expense(BaseModel):
    Amount : float
    Description : str
    Date: date
