from fastapi import Depends, HTTPException , status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verify_token
from app import crud, models

def get_db_session():
    db = get_db()
    try:
        yield next(db)
    finally:
        db.close()

def get_current_user(token: str = Depends(verify_token), db: Session = Depends(get_db_session)):
    user = crud.crud_user.get_user_by_token(db,token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

