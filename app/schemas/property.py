from pydantic import BaseModel

class PropertyCreate(BaseModel):
    title: str
    description: str
    price: int

class PropertyOut(PropertyCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

        