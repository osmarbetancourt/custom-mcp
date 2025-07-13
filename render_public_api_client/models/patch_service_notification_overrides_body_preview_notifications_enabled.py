from enum import Enum


class PatchServiceNotificationOverridesBodyPreviewNotificationsEnabled(str, Enum):
    DEFAULT = "default"
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
