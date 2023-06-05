"""All connectors in declarative container."""

from dependency_injector import containers, providers

from app.pkg.settings import settings

from .postgresql import Postgresql
from .redis import RedisConn

__all__ = ["Connectors", "RedisConn"]


class Connectors(containers.DeclarativeContainer):

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    postgresql = providers.Factory(
        Postgresql,
        username=configuration.POSTGRES_USER,
        password=configuration.POSTGRES_PASSWORD,
        host=configuration.POSTGRES_HOST,
        port=configuration.POSTGRES_PORT,
        database_name=configuration.POSTGRES_DB,
    )

    redis = providers.Factory(
        RedisConn,
        host=configuration.REDIS_HOST,
        port=configuration.REDIS_PORT,
        password=configuration.REDIS_PASSWORD,
    )
