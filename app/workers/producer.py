import base64
import logging
import os
import os.path
import time
from os.path import isfile, join
from pathlib import Path
from typing import List

import redis

from app.pkg.logger import Logger
from app.pkg.settings import settings


class Producer:
    logger: logging.Logger

    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def parse_dir(self):
        try:
            result = []
            files = [
                f
                for f in os.listdir(f"{settings.IMAGES_DIR_PATH}")
                if isfile(join(f"{settings.IMAGES_DIR_PATH}", f))
            ]
            if not files:
                return
            for file in files:
                with open(
                    Path(f"{settings.IMAGES_DIR_PATH}/{file}"), "rb",
                ) as imageFile:
                    image_str = base64.b64encode(imageFile.read())
                    result.append(image_str)
                os.replace(
                    f"{settings.IMAGES_DIR_PATH}/{file}",
                    f"{settings.IMAGES_DIR_PATH}/handled/{file}",
                )
        except Exception:
            self.logger.exception("Ошибка парсинга директории")
        else:
            return result

    def push_to_redis(self, images: List[bytes]):
        try:
            with redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD.get_secret_value(),
                decode_responses=True,
            ) as redis_client:
                for el in images:
                    redis_client.lpush(settings.REDIS_QUEUE_NAME, el)
        except Exception:
            self.logger.exception("Ошибка отправки данных в редис")
        else:
            self.logger.info("Отправлены новые данные в очередь Редис")

    def main(self):
        while True:
            images = self.parse_dir()
            if not images:
                time.sleep(5)
                continue
            self.push_to_redis(images)
            time.sleep(5)
