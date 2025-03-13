from datetime import date
from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.injection import inject_db
from app.infrastructure.models.form import Form

router = APIRouter(tags=["form"])

class FormCreate(BaseModel):
    comment: Optional[str] = None
    dob: date
    rating: int

@router.post("/form")
async def user_response_form(
    form: FormCreate,
    db: AsyncSession = Depends(inject_db)
):
    if not (1 <= form.rating <= 5):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Invalid rating")

    new_form = Form(**form.model_dump())

    db.add(new_form)
    await db.commit()
    await db.refresh(new_form)

    return HTTPStatus.OK

