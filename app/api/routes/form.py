from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse

from app.infrastructure.form import Form

router = APIRouter(tags=["form"])


@router.post("/form")
def user_response_form(
    form: Form
):
    return jsonable_encoder(form)

