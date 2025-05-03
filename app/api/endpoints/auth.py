from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session
from app.schemas.user import Token, UserLogin
from app.core.security import authenticate_user, create_access_token
from app.db.session import get_db

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user= authenticate_user(db, user_in.email,user_in.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token(data={"sub": user.email})
    return {"access_token":token, "token_type": "bearer"}
