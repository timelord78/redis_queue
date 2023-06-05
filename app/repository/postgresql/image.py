from typing import List

from app.pkg.models.base import Model
from app.pkg.models.image import Image
from app.repository.postgresql.connection import get_connection
from app.repository.postgresql.handlers.collect_response import collect_response
from app.repository.repository import Repository

__all__ = ["ImageData"]


class ImageData(Repository):
    @collect_response
    async def create(self, file_size: int) -> Image:
        q = """
                insert into image_data (size)
                values (%(file_size)s)
                returning size, created_at
            """
        async with get_connection() as cur:
            await cur.execute(q, {"file_size": file_size})
            return await cur.fetchone()

    async def read(self, query: Model) -> Model:
        raise NotImplementedError

    async def read_all(self) -> List[Model]:
        raise NotImplementedError

    async def update(self, cmd: Model) -> Model:
        raise NotImplementedError

    async def delete(self, cmd: Model) -> Model:
        raise NotImplementedError
