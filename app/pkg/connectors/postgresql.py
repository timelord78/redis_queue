"""Postgresql connector."""

from contextlib import asynccontextmanager

import aiopg
import pydantic
from aiopg import Connection

from .base_connector import BaseConnector

__all__ = ["Postgresql"]


class Postgresql(BaseConnector):
    def __init__(
        self,
        username: str,
        password: pydantic.SecretStr,
        host: pydantic.PositiveInt,
        port: pydantic.PositiveInt,
        database_name: str,
    ):
        self.pool = None
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database_name = database_name

    def get_dsn(self):
        return (
            f"postgresql://"
            f"{self.username}:"
            f"{self.password.get_secret_value()}@"
            f"{self.host}:{self.port}/"
            f"{self.database_name}"
        )

    @asynccontextmanager
    async def get_connect(self) -> Connection:
        if self.pool is None:
            self.pool = aiopg.create_pool(dsn=self.get_dsn())

        async with self.pool as pool:
            async with pool.acquire() as conn:
                yield conn
