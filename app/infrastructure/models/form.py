from sqlalchemy import CheckConstraint, Column, String, Integer, Boolean
from pydantic import BaseModel

from app.infrastructure.database.db import Base

class Form(Base):
    __tablename__ = 'form'
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False, default=5)
    useful = Column(Boolean, nullable=False, default=True)
    comment = Column(String(1000), nullable=True)

    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5', name='rating_range'),
    )

class FormSchema(BaseModel):
    id: int
