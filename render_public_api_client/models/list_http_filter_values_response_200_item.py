from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_http_filter_values_response_200_item_filter import (
    ListHttpFilterValuesResponse200ItemFilter,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListHttpFilterValuesResponse200Item")


@_attrs_define
class ListHttpFilterValuesResponse200Item:
    """
    Attributes:
        filter_ (Union[Unset, ListHttpFilterValuesResponse200ItemFilter]):
        values (Union[Unset, list[str]]):
    """

    filter_: Union[Unset, ListHttpFilterValuesResponse200ItemFilter] = UNSET
    values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_: Union[Unset, str] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.value

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, ListHttpFilterValuesResponse200ItemFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ListHttpFilterValuesResponse200ItemFilter(_filter_)

        values = cast(list[str], d.pop("values", UNSET))

        list_http_filter_values_response_200_item = cls(
            filter_=filter_,
            values=values,
        )

        list_http_filter_values_response_200_item.additional_properties = d
        return list_http_filter_values_response_200_item

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
