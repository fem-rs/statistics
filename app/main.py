from fastapi import FastAPI
from fastapi.routing import APIRoute

from starlette.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from app.infrastructure.database.db import init_db

from app.api.router import api_router

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="LC statistics project",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan
)

# just cuz dev, we need to change for prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)