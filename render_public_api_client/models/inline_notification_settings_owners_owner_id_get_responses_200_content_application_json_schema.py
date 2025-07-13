from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="InlineNotificationSettingsOwnersOwnerIdGetResponses200ContentApplicationJsonSchema",
)


@_attrs_define
class InlineNotificationSettingsOwnersOwnerIdGetResponses200ContentApplicationJsonSchema:
    """Stub for #/paths/~1notification-settings~1owners~1%7BownerId%7D/get/responses/200/content/application~1json/schema"""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inline_notification_settings_owners_owner_id_get_responses_200_content_application_json_schema = cls()

        inline_notification_settings_owners_owner_id_get_responses_200_content_application_json_schema.additional_properties = d
        return inline_notification_settings_owners_owner_id_get_responses_200_content_application_json_schema

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
