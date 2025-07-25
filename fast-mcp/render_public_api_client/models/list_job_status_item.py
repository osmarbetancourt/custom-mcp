from enum import Enum


class ListJobStatusItem(str, Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
