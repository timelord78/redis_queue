"""Redis connector."""

from contextlib import asynccontextmanager

import aioredis
import pydantic
from aioredis import Redis

from .base_connector import BaseConnector

__all__ = ["RedisConn"]


class RedisConn(BaseConnector):
    _host: str
    _port: pydantic.PositiveInt
    _password: pydantic.SecretStr

    def __init__(
        self,
        host: str,
        port: pydantic.PositiveInt,
        password: pydantic.SecretStr,
    ):
        self._host = host
        self._port = port
        self._password = password

    def get_dsn(self) -> str:
        raise NotImplementedError()

    @asynccontextmanager
    def get_connect(self) -> Redis:
        return aioredis.from_url(
            f"redis://:{self._port}", password=self._password.get_secret_value(),
        )
