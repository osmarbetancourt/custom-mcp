from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route import Route


T = TypeVar("T", bound="PatchRouteResponse200")


@_attrs_define
class PatchRouteResponse200:
    """
    Attributes:
        headers (Union[Unset, Route]):
    """

    headers: Union[Unset, "Route"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route import Route

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, Route]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = Route.from_dict(_headers)

        patch_route_response_200 = cls(
            headers=headers,
        )

        patch_route_response_200.additional_properties = d
        return patch_route_response_200

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
