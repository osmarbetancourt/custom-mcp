from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="InlineEventsEventIdGetResponses200ContentApplicationJsonSchemaPropertiesDetailsOneOf0",
)


@_attrs_define
class InlineEventsEventIdGetResponses200ContentApplicationJsonSchemaPropertiesDetailsOneOf0:
    """Stub for
    #/paths/~1events~1%7BeventId%7D/get/responses/200/content/application~1json/schema/properties/details/oneOf/0

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inline_events_event_id_get_responses_200_content_application_json_schema_properties_details_one_of_0 = cls()

        inline_events_event_id_get_responses_200_content_application_json_schema_properties_details_one_of_0.additional_properties = d
        return inline_events_event_id_get_responses_200_content_application_json_schema_properties_details_one_of_0

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
