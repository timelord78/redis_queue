import asyncio
import base64
import logging
import sys

import redis

from app.pkg.logger import Logger
from app.pkg.settings import settings
from app.repository.postgresql import ImageData


class Consumer:
    image_repo: ImageData
    logger: logging.Logger

    def __init__(self, image_repo: ImageData):
        self.image_repo = image_repo
        self.logger = Logger.get_logger(__name__)

    async def main(self):
        while True:
            with redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD.get_secret_value(),
                decode_responses=True,
            ) as redis_client:
                image_data = redis_client.rpop("images")
                if image_data is None:
                    await asyncio.sleep(1)
                else:
                    image_str = base64.b64decode(image_data)
                    file_size = sys.getsizeof(image_str)
                    try:
                        await self.image_repo.create(file_size)
                    except Exception:
                        self.logger.exception("Ошибка записи в БД")
                    else:
                        self.logger.info("Записаны данные по новому файлу")
