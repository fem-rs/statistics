import sys 
import os
sys.dont_write_bytecode = True

from fastapi import FastAPI
from fastapi.routing import APIRoute

from starlette.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import create_session

from dotenv import load_dotenv

from app.api.router import api_router

load_dotenv()

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"

app = FastAPI(
    title="LC statistics project",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)