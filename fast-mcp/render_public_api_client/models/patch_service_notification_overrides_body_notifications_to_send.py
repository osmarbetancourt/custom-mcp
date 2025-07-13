from enum import Enum


class PatchServiceNotificationOverridesBodyNotificationsToSend(str, Enum):
    ALL = "all"
    DEFAULT = "default"
    FAILURE = "failure"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
