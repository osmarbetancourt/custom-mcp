from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.owner import Owner
from ...types import Response


def _get_kwargs(
    owner_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/owners/{owner_id}".format(
            owner_id=owner_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Owner]]:
    if response.status_code == 200:
        response_200 = Owner.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
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
) -> Response[Union[Error, Owner]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, Owner]]:
    """Retrieve workspace

     Retrieve the workspace with the provided ID.

    Workspace IDs start with `tea-`. If you provide a user ID (starts with `own-`), this endpoint
    returns the user's default workspace.

    Args:
        owner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Owner]]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, Owner]]:
    """Retrieve workspace

     Retrieve the workspace with the provided ID.

    Workspace IDs start with `tea-`. If you provide a user ID (starts with `own-`), this endpoint
    returns the user's default workspace.

    Args:
        owner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Owner]
    """

    return sync_detailed(
        owner_id=owner_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, Owner]]:
    """Retrieve workspace

     Retrieve the workspace with the provided ID.

    Workspace IDs start with `tea-`. If you provide a user ID (starts with `own-`), this endpoint
    returns the user's default workspace.

    Args:
        owner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Owner]]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, Owner]]:
    """Retrieve workspace

     Retrieve the workspace with the provided ID.

    Workspace IDs start with `tea-`. If you provide a user ID (starts with `own-`), this endpoint
    returns the user's default workspace.

    Args:
        owner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Owner]
    """

    return (
        await asyncio_detailed(
            owner_id=owner_id,
            client=client,
        )
    ).parsed
