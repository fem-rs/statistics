from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.infrastructure.models.form import Form

router = APIRouter(tags=["form"])

@router.post("/form")
def user_response_form(
    form: Form
):
    return jsonable_encoder(form)

