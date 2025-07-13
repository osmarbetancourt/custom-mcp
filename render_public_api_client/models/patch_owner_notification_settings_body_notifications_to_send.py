from enum import Enum


class PatchOwnerNotificationSettingsBodyNotificationsToSend(str, Enum):
    ALL = "all"
    FAILURE = "failure"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
