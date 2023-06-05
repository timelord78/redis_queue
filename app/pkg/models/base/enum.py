from enum import Enum

__all__ = ["BaseEnum"]


class BaseEnum(Enum):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.value)
