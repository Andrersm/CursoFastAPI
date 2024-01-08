from typing import Type
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:Andre%4034313605@localhost:5432/faculdade"
    DBBaseModel: Type[Base] = Base

    JWT_SECRET: str = "UOlPacNX3McnRAoEpsdwa0IyGpU4Ve3e1p_p0QgT1xM"
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()

