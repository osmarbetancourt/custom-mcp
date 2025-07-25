import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_logs_direction import ListLogsDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_id: str,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    direction: Union[Unset, ListLogsDirection] = ListLogsDirection.BACKWARD,
    resource: list[str],
    instance: Union[Unset, list[str]] = UNSET,
    host: Union[Unset, list[str]] = UNSET,
    status_code: Union[Unset, list[str]] = UNSET,
    method: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    text: Union[Unset, list[str]] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ownerId"] = owner_id

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    json_resource = resource

    params["resource"] = json_resource

    json_instance: Union[Unset, list[str]] = UNSET
    if not isinstance(instance, Unset):
        json_instance = instance

    params["instance"] = json_instance

    json_host: Union[Unset, list[str]] = UNSET
    if not isinstance(host, Unset):
        json_host = host

    params["host"] = json_host

    json_status_code: Union[Unset, list[str]] = UNSET
    if not isinstance(status_code, Unset):
        json_status_code = status_code

    params["statusCode"] = json_status_code

    json_method: Union[Unset, list[str]] = UNSET
    if not isinstance(method, Unset):
        json_method = method

    params["method"] = json_method

    json_level: Union[Unset, list[str]] = UNSET
    if not isinstance(level, Unset):
        json_level = level

    params["level"] = json_level

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_text: Union[Unset, list[str]] = UNSET
    if not isinstance(text, Unset):
        json_text = text

    params["text"] = json_text

    json_path: Union[Unset, list[str]] = UNSET
    if not isinstance(path, Unset):
        json_path = path

    params["path"] = json_path

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Error]:
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 406:
        response_406 = Error.from_dict(response.json())

        return response_406
    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    owner_id: str,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    direction: Union[Unset, ListLogsDirection] = ListLogsDirection.BACKWARD,
    resource: list[str],
    instance: Union[Unset, list[str]] = UNSET,
    host: Union[Unset, list[str]] = UNSET,
    status_code: Union[Unset, list[str]] = UNSET,
    method: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    text: Union[Unset, list[str]] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[Error]:
    """List logs

     List logs matching the provided filters. Logs are paginated by start and end timestamps.
    There are more logs to fetch if `hasMore` is true in the response. Provide the `nextStartTime`
    and `nextEndTime` timestamps as the `startTime` and `endTime` query parameters to fetch the next
    page of logs.

    You can query for logs across multiple resources, but all resources must be in the same region and
    belong to the same owner.

    Args:
        owner_id (str):
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        direction (Union[Unset, ListLogsDirection]):  Default: ListLogsDirection.BACKWARD.
        resource (list[str]):
        instance (Union[Unset, list[str]]):
        host (Union[Unset, list[str]]):
        status_code (Union[Unset, list[str]]):
        method (Union[Unset, list[str]]):
        level (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        text (Union[Unset, list[str]]):
        path (Union[Unset, list[str]]):
        limit (Union[Unset, int]): Defaults to 20 Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        start_time=start_time,
        end_time=end_time,
        direction=direction,
        resource=resource,
        instance=instance,
        host=host,
        status_code=status_code,
        method=method,
        level=level,
        type_=type_,
        text=text,
        path=path,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    owner_id: str,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    direction: Union[Unset, ListLogsDirection] = ListLogsDirection.BACKWARD,
    resource: list[str],
    instance: Union[Unset, list[str]] = UNSET,
    host: Union[Unset, list[str]] = UNSET,
    status_code: Union[Unset, list[str]] = UNSET,
    method: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    text: Union[Unset, list[str]] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[Error]:
    """List logs

     List logs matching the provided filters. Logs are paginated by start and end timestamps.
    There are more logs to fetch if `hasMore` is true in the response. Provide the `nextStartTime`
    and `nextEndTime` timestamps as the `startTime` and `endTime` query parameters to fetch the next
    page of logs.

    You can query for logs across multiple resources, but all resources must be in the same region and
    belong to the same owner.

    Args:
        owner_id (str):
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        direction (Union[Unset, ListLogsDirection]):  Default: ListLogsDirection.BACKWARD.
        resource (list[str]):
        instance (Union[Unset, list[str]]):
        host (Union[Unset, list[str]]):
        status_code (Union[Unset, list[str]]):
        method (Union[Unset, list[str]]):
        level (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        text (Union[Unset, list[str]]):
        path (Union[Unset, list[str]]):
        limit (Union[Unset, int]): Defaults to 20 Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        client=client,
        owner_id=owner_id,
        start_time=start_time,
        end_time=end_time,
        direction=direction,
        resource=resource,
        instance=instance,
        host=host,
        status_code=status_code,
        method=method,
        level=level,
        type_=type_,
        text=text,
        path=path,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    owner_id: str,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    direction: Union[Unset, ListLogsDirection] = ListLogsDirection.BACKWARD,
    resource: list[str],
    instance: Union[Unset, list[str]] = UNSET,
    host: Union[Unset, list[str]] = UNSET,
    status_code: Union[Unset, list[str]] = UNSET,
    method: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    text: Union[Unset, list[str]] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[Error]:
    """List logs

     List logs matching the provided filters. Logs are paginated by start and end timestamps.
    There are more logs to fetch if `hasMore` is true in the response. Provide the `nextStartTime`
    and `nextEndTime` timestamps as the `startTime` and `endTime` query parameters to fetch the next
    page of logs.

    You can query for logs across multiple resources, but all resources must be in the same region and
    belong to the same owner.

    Args:
        owner_id (str):
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        direction (Union[Unset, ListLogsDirection]):  Default: ListLogsDirection.BACKWARD.
        resource (list[str]):
        instance (Union[Unset, list[str]]):
        host (Union[Unset, list[str]]):
        status_code (Union[Unset, list[str]]):
        method (Union[Unset, list[str]]):
        level (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        text (Union[Unset, list[str]]):
        path (Union[Unset, list[str]]):
        limit (Union[Unset, int]): Defaults to 20 Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        start_time=start_time,
        end_time=end_time,
        direction=direction,
        resource=resource,
        instance=instance,
        host=host,
        status_code=status_code,
        method=method,
        level=level,
        type_=type_,
        text=text,
        path=path,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    owner_id: str,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    direction: Union[Unset, ListLogsDirection] = ListLogsDirection.BACKWARD,
    resource: list[str],
    instance: Union[Unset, list[str]] = UNSET,
    host: Union[Unset, list[str]] = UNSET,
    status_code: Union[Unset, list[str]] = UNSET,
    method: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, list[str]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    text: Union[Unset, list[str]] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[Error]:
    """List logs

     List logs matching the provided filters. Logs are paginated by start and end timestamps.
    There are more logs to fetch if `hasMore` is true in the response. Provide the `nextStartTime`
    and `nextEndTime` timestamps as the `startTime` and `endTime` query parameters to fetch the next
    page of logs.

    You can query for logs across multiple resources, but all resources must be in the same region and
    belong to the same owner.

    Args:
        owner_id (str):
        start_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:15:30Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2021-06-17T08:30:30Z.
        direction (Union[Unset, ListLogsDirection]):  Default: ListLogsDirection.BACKWARD.
        resource (list[str]):
        instance (Union[Unset, list[str]]):
        host (Union[Unset, list[str]]):
        status_code (Union[Unset, list[str]]):
        method (Union[Unset, list[str]]):
        level (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        text (Union[Unset, list[str]]):
        path (Union[Unset, list[str]]):
        limit (Union[Unset, int]): Defaults to 20 Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_id=owner_id,
            start_time=start_time,
            end_time=end_time,
            direction=direction,
            resource=resource,
            instance=instance,
            host=host,
            status_code=status_code,
            method=method,
            level=level,
            type_=type_,
            text=text,
            path=path,
            limit=limit,
        )
    ).parsed
