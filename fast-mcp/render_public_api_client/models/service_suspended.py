from enum import Enum


class ServiceSuspended(str, Enum):
    NOT_SUSPENDED = "not_suspended"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
