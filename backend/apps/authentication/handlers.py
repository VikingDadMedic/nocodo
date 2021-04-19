from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils.database import database, get_database
from .schema import Token
from .utils import authenticate_user, create_access_token

authentication_router = APIRouter()


@authentication_router.post("/token", response_model=Token)
async def login_with_password(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: database = Depends(get_database)
):
    result = await authenticate_user(
        username=form_data.username,
        password=form_data.password,
        db=db
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={
            "username": result["email"]
        },
    )
    return {"access_token": access_token, "token_type": "bearer"}
