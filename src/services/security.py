from authx import AuthX, AuthXConfig
import os

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY=os.getenv("SECRET_KEY", "complete_secret")
)

security = AuthX(config=config)

def make_token(username: str):
    access_token = security.create_access_token(username)
    return access_token