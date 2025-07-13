from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.protected_status import ProtectedStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentPATCHInput")


@_attrs_define
class EnvironmentPATCHInput:
    """
    Attributes:
        name (Union[Unset, str]):
        network_isolation_enabled (Union[Unset, bool]): Indicates whether network connections across environments are
            allowed.
        protected_status (Union[Unset, ProtectedStatus]): Indicates whether an environment is `unprotected` or
            `protected`. Only admin users can perform destructive actions in `protected` environments.
    """

    name: Union[Unset, str] = UNSET
    network_isolation_enabled: Union[Unset, bool] = UNSET
    protected_status: Union[Unset, ProtectedStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        network_isolation_enabled = self.network_isolation_enabled

        protected_status: Union[Unset, str] = UNSET
        if not isinstance(self.protected_status, Unset):
            protected_status = self.protected_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if network_isolation_enabled is not UNSET:
            field_dict["networkIsolationEnabled"] = network_isolation_enabled
        if protected_status is not UNSET:
            field_dict["protectedStatus"] = protected_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        network_isolation_enabled = d.pop("networkIsolationEnabled", UNSET)

        _protected_status = d.pop("protectedStatus", UNSET)
        protected_status: Union[Unset, ProtectedStatus]
        if isinstance(_protected_status, Unset):
            protected_status = UNSET
        else:
            protected_status = ProtectedStatus(_protected_status)

        environment_patch_input = cls(
            name=name,
            network_isolation_enabled=network_isolation_enabled,
            protected_status=protected_status,
        )

        environment_patch_input.additional_properties = d
        return environment_patch_input

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
