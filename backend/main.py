from fastapi import FastAPI

from utils.database import database
from utils.sentry import sentry_init

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
    event_router,
    prefix="/events"
)
app.include_router(
    event_user_router,
    prefix="/event_users"
)
app.include_router(
    gift_router,
    prefix="/gift"
)
app.include_router(
    user_router,
    prefix="/users"
)
app.include_router(
    authentication_router,
    prefix="/auth"
)
app.include_router(
    payment_router,
    prefix="/payments"
)
app.include_router(
    upload_router,
    prefix="/uploads"
)
app.include_router(
    invite_router,
    prefix="/invites"
)
