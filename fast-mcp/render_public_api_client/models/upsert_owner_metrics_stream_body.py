from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upsert_owner_metrics_stream_body_provider import (
    UpsertOwnerMetricsStreamBodyProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertOwnerMetricsStreamBody")


@_attrs_define
class UpsertOwnerMetricsStreamBody:
    """Input for creating or updating a metrics stream

    Attributes:
        provider (Union[Unset, UpsertOwnerMetricsStreamBodyProvider]): Provider to send metrics to
        url (Union[Unset, str]): The endpoint URL to stream metrics to
        token (Union[Unset, str]): Authentication token for the metrics stream
    """

    provider: Union[Unset, UpsertOwnerMetricsStreamBodyProvider] = UNSET
    url: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        url = self.url

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if url is not UNSET:
            field_dict["url"] = url
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, UpsertOwnerMetricsStreamBodyProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = UpsertOwnerMetricsStreamBodyProvider(_provider)

        url = d.pop("url", UNSET)

        token = d.pop("token", UNSET)

        upsert_owner_metrics_stream_body = cls(
            provider=provider,
            url=url,
            token=token,
        )

        upsert_owner_metrics_stream_body.additional_properties = d
        return upsert_owner_metrics_stream_body

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
