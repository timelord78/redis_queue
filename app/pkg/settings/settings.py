from functools import lru_cache
from pathlib import Path

import pydantic
from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.types import PositiveInt, SecretStr

from app.pkg.models.logger.logger import Logger

__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    class Config:
        env_file_encoding = "utf-8"
        arbitrary_types_allowed = True


class Settings(_Settings):
    LOGGER_LEVEL: Logger
    APP_DIR_PATH_INTERNAL: Path
    APP_DIR_PATH: Path
    IMAGES_DIR_PATH: Path

    POSTGRES_HOST: str
    POSTGRES_PORT: PositiveInt
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str

    REDIS_PORT: int
    REDIS_HOST: str
    REDIS_PASSWORD: SecretStr
    REDIS_QUEUE_NAME: str

    @pydantic.validator("APP_DIR_PATH_INTERNAL")
    def create_logger_directory(cls, v: Path) -> Path:
        if not v.exists():
            v.mkdir(parents=True, exist_ok=True)
        return v

    @pydantic.validator("IMAGES_DIR_PATH")
    def create_image_directory(cls, v: Path) -> Path:
        if not v.exists():
            v.mkdir(parents=True, exist_ok=True)
            v.joinpath("handled").mkdir(parents=True, exist_ok=True)
        return v


@lru_cache()
def get_settings(env_file: str = ".env") -> Settings:
    return Settings(_env_file=find_dotenv(env_file))
