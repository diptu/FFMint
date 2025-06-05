# app/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str
    log_level: str
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()
