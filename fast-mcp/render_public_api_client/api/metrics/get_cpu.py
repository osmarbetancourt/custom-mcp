import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_cpu_aggregation_method import GetCpuAggregationMethod
from ...models.get_cpu_response_200_item import GetCpuResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    resolution_seconds: Union[Unset, float] = 60.0,
    resource: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    aggregation_method: Union[Unset, GetCpuAggregationMethod] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["resolutionSeconds"] = resolution_seconds

    params["resource"] = resource

    params["service"] = service

    params["instance"] = instance

    json_aggregation_method: Union[Unset, str] = UNSET
    if not isinstance(aggregation_method, Unset):
        json_aggregation_method = aggregation_method.value

    params["aggregationMethod"] = json_aggregation_method

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metrics/cpu",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, list["GetCpuResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetCpuResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, list["GetCpuResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    resolution_seconds: Union[Unset, float] = 60.0,
    resource: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    aggregation_method: Union[Unset, GetCpuAggregationMethod] = UNSET,
) -> Response[Union[Error, list["GetCpuResponse200Item"]]]:
    """Get CPU usage

     Get CPU usage for one or more resources.

    Args:
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        resolution_seconds (Union[Unset, float]):  Default: 60.0. Example: 60.
        resource (Union[Unset, str]):  Example: srv-xxxxx,dpg-xxxxx,red-xxxxx.
        service (Union[Unset, str]):  Example: srv-xxxxx.
        instance (Union[Unset, str]):  Example: srv-xxxxx-yyyy.
        aggregation_method (Union[Unset, GetCpuAggregationMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['GetCpuResponse200Item']]]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        resolution_seconds=resolution_seconds,
        resource=resource,
        service=service,
        instance=instance,
        aggregation_method=aggregation_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    resolution_seconds: Union[Unset, float] = 60.0,
    resource: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    aggregation_method: Union[Unset, GetCpuAggregationMethod] = UNSET,
) -> Optional[Union[Error, list["GetCpuResponse200Item"]]]:
    """Get CPU usage

     Get CPU usage for one or more resources.

    Args:
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        resolution_seconds (Union[Unset, float]):  Default: 60.0. Example: 60.
        resource (Union[Unset, str]):  Example: srv-xxxxx,dpg-xxxxx,red-xxxxx.
        service (Union[Unset, str]):  Example: srv-xxxxx.
        instance (Union[Unset, str]):  Example: srv-xxxxx-yyyy.
        aggregation_method (Union[Unset, GetCpuAggregationMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['GetCpuResponse200Item']]
    """

    return sync_detailed(
        client=client,
        start_time=start_time,
        end_time=end_time,
        resolution_seconds=resolution_seconds,
        resource=resource,
        service=service,
        instance=instance,
        aggregation_method=aggregation_method,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    resolution_seconds: Union[Unset, float] = 60.0,
    resource: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    aggregation_method: Union[Unset, GetCpuAggregationMethod] = UNSET,
) -> Response[Union[Error, list["GetCpuResponse200Item"]]]:
    """Get CPU usage

     Get CPU usage for one or more resources.

    Args:
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        resolution_seconds (Union[Unset, float]):  Default: 60.0. Example: 60.
        resource (Union[Unset, str]):  Example: srv-xxxxx,dpg-xxxxx,red-xxxxx.
        service (Union[Unset, str]):  Example: srv-xxxxx.
        instance (Union[Unset, str]):  Example: srv-xxxxx-yyyy.
        aggregation_method (Union[Unset, GetCpuAggregationMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['GetCpuResponse200Item']]]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        resolution_seconds=resolution_seconds,
        resource=resource,
        service=service,
        instance=instance,
        aggregation_method=aggregation_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    resolution_seconds: Union[Unset, float] = 60.0,
    resource: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    aggregation_method: Union[Unset, GetCpuAggregationMethod] = UNSET,
) -> Optional[Union[Error, list["GetCpuResponse200Item"]]]:
    """Get CPU usage

     Get CPU usage for one or more resources.

    Args:
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        resolution_seconds (Union[Unset, float]):  Default: 60.0. Example: 60.
        resource (Union[Unset, str]):  Example: srv-xxxxx,dpg-xxxxx,red-xxxxx.
        service (Union[Unset, str]):  Example: srv-xxxxx.
        instance (Union[Unset, str]):  Example: srv-xxxxx-yyyy.
        aggregation_method (Union[Unset, GetCpuAggregationMethod]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['GetCpuResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_time=start_time,
            end_time=end_time,
            resolution_seconds=resolution_seconds,
            resource=resource,
            service=service,
            instance=instance,
            aggregation_method=aggregation_method,
        )
    ).parsed
