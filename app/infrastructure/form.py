from datetime import datetime
from pydantic import BaseModel


class Form(BaseModel):
    found_useful: bool
    useful_for: str
    age: datetime