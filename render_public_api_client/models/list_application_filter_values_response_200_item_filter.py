from enum import Enum


class ListApplicationFilterValuesResponse200ItemFilter(str, Enum):
    INSTANCE = "instance"

    def __str__(self) -> str:
        return str(self.value)
