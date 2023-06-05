from starlette import status

from app.pkg.models.base.exception import BaseApiException


class EmptyResult(BaseApiException):
    message = "Empty result"
    status_code = status.HTTP_502_BAD_GATEWAY


class UniqueViolation(BaseApiException):
    message = "Not unique"
    status_code = status.HTTP_409_CONFLICT


class DriverError(BaseApiException):
    def __init__(self, message: str = None):
        if message:
            self.message = message

    message = "Internal error"
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
