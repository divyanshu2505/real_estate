import os
from dotenv import load_dotenv

load_dotenv() 

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

settings = Settings()


# Add this line for debugging:
print("DEBUG - Loaded DATABASE_URL:", settings.DATABASE_URL)
