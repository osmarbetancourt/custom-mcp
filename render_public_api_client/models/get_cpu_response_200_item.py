from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_cpu_response_200_item_labels_item import (
        GetCpuResponse200ItemLabelsItem,
    )
    from ..models.get_cpu_response_200_item_values_item import (
        GetCpuResponse200ItemValuesItem,
    )


T = TypeVar("T", bound="GetCpuResponse200Item")


@_attrs_define
class GetCpuResponse200Item:
    """A time series data point

    Attributes:
        labels (list['GetCpuResponse200ItemLabelsItem']): List of labels describing the time series
        values (list['GetCpuResponse200ItemValuesItem']): The values of the time series
        unit (str):  Example: GB.
    """

    labels: list["GetCpuResponse200ItemLabelsItem"]
    values: list["GetCpuResponse200ItemValuesItem"]
    unit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
                "values": values,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_cpu_response_200_item_labels_item import (
            GetCpuResponse200ItemLabelsItem,
        )
        from ..models.get_cpu_response_200_item_values_item import (
            GetCpuResponse200ItemValuesItem,
        )

        d = dict(src_dict)
        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = GetCpuResponse200ItemLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = GetCpuResponse200ItemValuesItem.from_dict(values_item_data)

            values.append(values_item)

        unit = d.pop("unit")

        get_cpu_response_200_item = cls(
            labels=labels,
            values=values,
            unit=unit,
        )

        get_cpu_response_200_item.additional_properties = d
        return get_cpu_response_200_item

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
