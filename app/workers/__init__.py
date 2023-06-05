from dependency_injector import containers, providers

from app.repository.postgresql import RepositoryPostgres
from app.workers.consumer import Consumer
from app.workers.producer import Producer

__all__ = ["Workers", "Producer"]


class Workers(containers.DeclarativeContainer):
    repository_postgres = providers.Container(RepositoryPostgres)

    producer = providers.Factory(
        Producer,
    )

    consumer = providers.Factory(
        Consumer,
        image_repo=repository_postgres.image_data,
    )
