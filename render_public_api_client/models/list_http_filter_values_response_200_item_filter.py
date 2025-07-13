from enum import Enum


class ListHttpFilterValuesResponse200ItemFilter(str, Enum):
    HOST = "host"
    STATUSCODE = "statusCode"

    def __str__(self) -> str:
        return str(self.value)
