from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.key_value_connection_info import KeyValueConnectionInfo
from ...types import Response


def _get_kwargs(
    key_value_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/key-value/{key_value_id}/connection-info".format(
            key_value_id=key_value_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, KeyValueConnectionInfo]]:
    if response.status_code == 200:
        response_200 = KeyValueConnectionInfo.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
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
) -> Response[Union[Error, KeyValueConnectionInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_value_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, KeyValueConnectionInfo]]:
    """Retrieve Key Value connection info

     Retrieve connection info for a Key Value instance by ID. Connection info includes sensitive
    information.

    Args:
        key_value_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, KeyValueConnectionInfo]]
    """

    kwargs = _get_kwargs(
        key_value_id=key_value_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_value_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, KeyValueConnectionInfo]]:
    """Retrieve Key Value connection info

     Retrieve connection info for a Key Value instance by ID. Connection info includes sensitive
    information.

    Args:
        key_value_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, KeyValueConnectionInfo]
    """

    return sync_detailed(
        key_value_id=key_value_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_value_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, KeyValueConnectionInfo]]:
    """Retrieve Key Value connection info

     Retrieve connection info for a Key Value instance by ID. Connection info includes sensitive
    information.

    Args:
        key_value_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, KeyValueConnectionInfo]]
    """

    kwargs = _get_kwargs(
        key_value_id=key_value_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_value_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, KeyValueConnectionInfo]]:
    """Retrieve Key Value connection info

     Retrieve connection info for a Key Value instance by ID. Connection info includes sensitive
    information.

    Args:
        key_value_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, KeyValueConnectionInfo]
    """

    return (
        await asyncio_detailed(
            key_value_id=key_value_id,
            client=client,
        )
    ).parsed
