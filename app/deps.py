# dependecies
import os
from dotenv import load_dotenv
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Header
from app.database import get_db

# Load variables from the .env file
load_dotenv()

SessionDB = Annotated[Session, Depends(get_db)]

APIKEY_HEADER = os.getenv("API_KEY")


def validate_apikey(key:  Annotated[str, Header()]):    
    if key != APIKEY_HEADER:
        raise HTTPException(
            status_code=401,
            detail="Authentication failed: invalid token."
        )
