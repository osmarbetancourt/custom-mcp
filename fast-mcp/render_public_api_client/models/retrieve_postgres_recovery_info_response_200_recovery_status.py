from enum import Enum


class RetrievePostgresRecoveryInfoResponse200RecoveryStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    BACKUP_NOT_READY = "BACKUP_NOT_READY"
    NOT_AVAILABLE = "NOT_AVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
