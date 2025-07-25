import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.retrieve_postgres_recovery_info_response_200_recovery_status import (
    RetrievePostgresRecoveryInfoResponse200RecoveryStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrievePostgresRecoveryInfoResponse200")


@_attrs_define
class RetrievePostgresRecoveryInfoResponse200:
    """
    Attributes:
        recovery_status (RetrievePostgresRecoveryInfoResponse200RecoveryStatus): Availability of point-in-time recovery.
        starts_at (Union[Unset, datetime.datetime]):
    """

    recovery_status: RetrievePostgresRecoveryInfoResponse200RecoveryStatus
    starts_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recovery_status = self.recovery_status.value

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recoveryStatus": recovery_status,
            }
        )
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recovery_status = RetrievePostgresRecoveryInfoResponse200RecoveryStatus(
            d.pop("recoveryStatus")
        )

        _starts_at = d.pop("startsAt", UNSET)
        starts_at: Union[Unset, datetime.datetime]
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = isoparse(_starts_at)

        retrieve_postgres_recovery_info_response_200 = cls(
            recovery_status=recovery_status,
            starts_at=starts_at,
        )

        retrieve_postgres_recovery_info_response_200.additional_properties = d
        return retrieve_postgres_recovery_info_response_200

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
