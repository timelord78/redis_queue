from dependency_injector import containers, providers

from app.repository.postgresql.image import ImageData


class RepositoryPostgres(containers.DeclarativeContainer):
    image_data = providers.Factory(ImageData)
