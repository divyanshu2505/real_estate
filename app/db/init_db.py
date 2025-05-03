from app.db.session import engine
from app.db.base import Base
from app.models import user

def init():
    Base.metadata.create_all(bind=engine)
    