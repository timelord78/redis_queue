import datetime

from app.pkg.models.base.model import BaseModel

__all__ = ["Image"]


class BaseImageData(BaseModel):
    """Base model for user."""


class Image(BaseImageData):
    size: int
    created_at: datetime.datetime
