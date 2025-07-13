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

T = TypeVar("T", bound="EnvironmentPOSTInput")


@_attrs_define
class EnvironmentPOSTInput:
    """
    Attributes:
        name (str):
        project_id (str):
        protected_status (Union[Unset, ProtectedStatus]): Indicates whether an environment is `unprotected` or
            `protected`. Only admin users can perform destructive actions in `protected` environments.
        network_isolation_enabled (Union[Unset, bool]): Indicates whether network connections across environments are
            allowed.
    """

    name: str
    project_id: str
    protected_status: Union[Unset, ProtectedStatus] = UNSET
    network_isolation_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

        protected_status: Union[Unset, str] = UNSET
        if not isinstance(self.protected_status, Unset):
            protected_status = self.protected_status.value

        network_isolation_enabled = self.network_isolation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectId": project_id,
            }
        )
        if protected_status is not UNSET:
            field_dict["protectedStatus"] = protected_status
        if network_isolation_enabled is not UNSET:
            field_dict["networkIsolationEnabled"] = network_isolation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        project_id = d.pop("projectId")

        _protected_status = d.pop("protectedStatus", UNSET)
        protected_status: Union[Unset, ProtectedStatus]
        if isinstance(_protected_status, Unset):
            protected_status = UNSET
        else:
            protected_status = ProtectedStatus(_protected_status)

        network_isolation_enabled = d.pop("networkIsolationEnabled", UNSET)

        environment_post_input = cls(
            name=name,
            project_id=project_id,
            protected_status=protected_status,
            network_isolation_enabled=network_isolation_enabled,
        )

        environment_post_input.additional_properties = d
        return environment_post_input

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
