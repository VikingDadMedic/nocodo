from fastapi import FastAPI

from utils.database import database
from utils.sentry import sentry_init
from apps.authentication.handlers import authentication_router
from apps.user.handlers import user_router

app = FastAPI()


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
    authentication_router,
    prefix="/auth"
)
