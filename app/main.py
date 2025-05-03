from fastapi import FastAPI, Request,Depends
from fastapi.templating import Jinja2Templates

from app.api.endpoints import users,auth,properties
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Autentication"])
app.include_router(properties.router, prefix="/properties", tags=["properties"])

