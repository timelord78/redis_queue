from app.pkg.connectors import Connectors
from app.pkg.models.core import Container, Containers
from app.repository.postgresql import RepositoryPostgres
from app.workers import Workers

__all__ = ["__containers__"]

__containers__ = Containers(
    pkg_name=__name__,
    containers=[
        Container(container=Connectors),
        Container(container=RepositoryPostgres),
        Container(container=Workers),
    ],
)
