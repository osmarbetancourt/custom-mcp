from enum import Enum


class UpdateOwnerLogStreamBodyPreview(str, Enum):
    DROP = "drop"
    SEND = "send"

    def __str__(self) -> str:
        return str(self.value)
