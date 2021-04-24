from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.database import database
from utils.sentry import sentry_init
from apps.auth.handlers import auth_router
from apps.user.handlers import user_router


origins = [
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()
    sentry_init()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def api_home():
    return {"status": "ok"}


app.include_router(
    user_router,
    prefix="/users"
)
app.include_router(
    auth_router,
    prefix="/auth"
)
