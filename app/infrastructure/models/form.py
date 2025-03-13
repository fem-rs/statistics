from sqlalchemy import CheckConstraint, Column, String, Integer, Date
from pydantic import BaseModel

from app.infrastructure.database.db import Base

class Form(Base):
    __tablename__ = 'form'
    
    id = Column(Integer, primary_key=True)
    comment = Column(String(1000), nullable=True)
    dob = Column(Date, nullable=False, default=True)
    rating = Column(Integer, nullable=False, default=5)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5', name='rating_range'),
    )

class FormSchema(BaseModel):
    id: int
