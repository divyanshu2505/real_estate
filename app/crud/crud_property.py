from sqlalchemy.orm import Session
from app.models.property import Property
from app.schemas.property import PropertyCreate

def create_property(db: Session, property_in: PropertyCreate, owner_id: int):
    db_property = Property(**property_in.dict(), owner_id=owner_id)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)

    return db_property

