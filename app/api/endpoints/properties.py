from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.property import PropertyCreate, PropertyOut
from app.api.deps import get_current_user
from app.crud import crud_property
from app.db.session import get_db
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=PropertyOut)
def create_property(property_in: PropertyCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_property.create_property(db, property_in, owner_id=current_user.id)