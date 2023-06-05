import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.pkg.settings import settings


class Logger:
    LOGGER_DIR_PATH = settings.APP_DIR_PATH
    LOGGER_LEVEL = settings.LOGGER_LEVEL
    log_format = (
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%("
        "funcName)s(%(lineno)d) - %(message)s "
    )

    @classmethod
    def get_file_handler(cls, file_name):
        Path(file_name).absolute().parent.mkdir(exist_ok=True, parents=True)
        file_handler = RotatingFileHandler(
            filename=file_name,
            maxBytes=5242880,
            backupCount=10,
        )
        file_handler.setFormatter(logging.Formatter(cls.log_format))
        return file_handler

    @classmethod
    def get_stream_handler(cls):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(cls.log_format))
        return stream_handler

    @classmethod
    def get_logger(cls, name):
        logger = logging.getLogger(name)
        file_path = str(
            Path().cwd().joinpath(settings.APP_DIR_PATH_INTERNAL, "logs.log"),
        )
        logger.addHandler(cls.get_file_handler(file_name=file_path))
        logger.addHandler(cls.get_stream_handler())
        logger.setLevel(cls.LOGGER_LEVEL)
        return logger
