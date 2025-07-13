from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="InlineBlueprintsBlueprintIdPatchRequestBodyContentApplicationJsonSchemaPropertiesAutoSync",
)


@_attrs_define
class InlineBlueprintsBlueprintIdPatchRequestBodyContentApplicationJsonSchemaPropertiesAutoSync:
    """Stub for
    #/paths/~1blueprints~1%7BblueprintId%7D/patch/requestBody/content/application~1json/schema/properties/autoSync

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inline_blueprints_blueprint_id_patch_request_body_content_application_json_schema_properties_auto_sync = cls()

        inline_blueprints_blueprint_id_patch_request_body_content_application_json_schema_properties_auto_sync.additional_properties = d
        return inline_blueprints_blueprint_id_patch_request_body_content_application_json_schema_properties_auto_sync

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
