from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.retrieve_postgres_recovery_info_response_200 import (
    RetrievePostgresRecoveryInfoResponse200,
)
from ...types import Response


def _get_kwargs(
    postgres_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/postgres/{postgres_id}/recovery".format(
            postgres_id=postgres_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, RetrievePostgresRecoveryInfoResponse200]]:
    if response.status_code == 200:
        response_200 = RetrievePostgresRecoveryInfoResponse200.from_dict(
            response.json()
        )

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
) -> Response[Union[Error, RetrievePostgresRecoveryInfoResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    postgres_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, RetrievePostgresRecoveryInfoResponse200]]:
    """Retrieve point-in-time recovery status

     Retrieve information on the availability of Postgres point-in-time recovery for a Postgres instance
    by ID.

    Args:
        postgres_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RetrievePostgresRecoveryInfoResponse200]]
    """

    kwargs = _get_kwargs(
        postgres_id=postgres_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, RetrievePostgresRecoveryInfoResponse200]]:
    """Retrieve point-in-time recovery status

     Retrieve information on the availability of Postgres point-in-time recovery for a Postgres instance
    by ID.

    Args:
        postgres_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RetrievePostgresRecoveryInfoResponse200]
    """

    return sync_detailed(
        postgres_id=postgres_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    postgres_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, RetrievePostgresRecoveryInfoResponse200]]:
    """Retrieve point-in-time recovery status

     Retrieve information on the availability of Postgres point-in-time recovery for a Postgres instance
    by ID.

    Args:
        postgres_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, RetrievePostgresRecoveryInfoResponse200]]
    """

    kwargs = _get_kwargs(
        postgres_id=postgres_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, RetrievePostgresRecoveryInfoResponse200]]:
    """Retrieve point-in-time recovery status

     Retrieve information on the availability of Postgres point-in-time recovery for a Postgres instance
    by ID.

    Args:
        postgres_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, RetrievePostgresRecoveryInfoResponse200]
    """

    return (
        await asyncio_detailed(
            postgres_id=postgres_id,
            client=client,
        )
    ).parsed
