from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="InlineNotificationSettingsOverridesServicesServiceIdPatchRequestBodyContentApplicationJsonSchemaPropertiesPreviewNotificationsEnabled",
)


@_attrs_define
class InlineNotificationSettingsOverridesServicesServiceIdPatchRequestBodyContentApplicationJsonSchemaPropertiesPreviewNotificationsEnabled:
    """Stub for #/paths/~1notification-settings~1overrides~1services~1%7BserviceId%7D/patch/requestBody/content/application
    ~1json/schema/properties/previewNotificationsEnabled

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inline_notification_settings_overrides_services_service_id_patch_request_body_content_application_json_schema_properties_preview_notifications_enabled = cls()

        inline_notification_settings_overrides_services_service_id_patch_request_body_content_application_json_schema_properties_preview_notifications_enabled.additional_properties = d
        return inline_notification_settings_overrides_services_service_id_patch_request_body_content_application_json_schema_properties_preview_notifications_enabled

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
