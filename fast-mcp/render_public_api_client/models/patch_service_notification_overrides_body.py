from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_service_notification_overrides_body_notifications_to_send import (
    PatchServiceNotificationOverridesBodyNotificationsToSend,
)
from ..models.patch_service_notification_overrides_body_preview_notifications_enabled import (
    PatchServiceNotificationOverridesBodyPreviewNotificationsEnabled,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServiceNotificationOverridesBody")


@_attrs_define
class PatchServiceNotificationOverridesBody:
    """
    Attributes:
        preview_notifications_enabled (Union[Unset, PatchServiceNotificationOverridesBodyPreviewNotificationsEnabled]):
        notifications_to_send (Union[Unset, PatchServiceNotificationOverridesBodyNotificationsToSend]):
    """

    preview_notifications_enabled: Union[
        Unset, PatchServiceNotificationOverridesBodyPreviewNotificationsEnabled
    ] = UNSET
    notifications_to_send: Union[
        Unset, PatchServiceNotificationOverridesBodyNotificationsToSend
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preview_notifications_enabled: Union[Unset, str] = UNSET
        if not isinstance(self.preview_notifications_enabled, Unset):
            preview_notifications_enabled = self.preview_notifications_enabled.value

        notifications_to_send: Union[Unset, str] = UNSET
        if not isinstance(self.notifications_to_send, Unset):
            notifications_to_send = self.notifications_to_send.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview_notifications_enabled is not UNSET:
            field_dict["previewNotificationsEnabled"] = preview_notifications_enabled
        if notifications_to_send is not UNSET:
            field_dict["notificationsToSend"] = notifications_to_send

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _preview_notifications_enabled = d.pop("previewNotificationsEnabled", UNSET)
        preview_notifications_enabled: Union[
            Unset, PatchServiceNotificationOverridesBodyPreviewNotificationsEnabled
        ]
        if isinstance(_preview_notifications_enabled, Unset):
            preview_notifications_enabled = UNSET
        else:
            preview_notifications_enabled = (
                PatchServiceNotificationOverridesBodyPreviewNotificationsEnabled(
                    _preview_notifications_enabled
                )
            )

        _notifications_to_send = d.pop("notificationsToSend", UNSET)
        notifications_to_send: Union[
            Unset, PatchServiceNotificationOverridesBodyNotificationsToSend
        ]
        if isinstance(_notifications_to_send, Unset):
            notifications_to_send = UNSET
        else:
            notifications_to_send = (
                PatchServiceNotificationOverridesBodyNotificationsToSend(
                    _notifications_to_send
                )
            )

        patch_service_notification_overrides_body = cls(
            preview_notifications_enabled=preview_notifications_enabled,
            notifications_to_send=notifications_to_send,
        )

        patch_service_notification_overrides_body.additional_properties = d
        return patch_service_notification_overrides_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
