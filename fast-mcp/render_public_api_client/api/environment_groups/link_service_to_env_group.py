from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.env_group import EnvGroup
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    env_group_id: str,
    service_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/env-groups/{env_group_id}/services/{service_id}".format(
            env_group_id=env_group_id,
            service_id=service_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EnvGroup, Error]]:
    if response.status_code == 200:
        response_200 = EnvGroup.from_dict(response.json())

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
) -> Response[Union[EnvGroup, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    env_group_id: str,
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EnvGroup, Error]]:
    """Link service

     Link a particular service to a particular environment group.

    The linked service will have access to the environment variables and secret files in the group.

    Args:
        env_group_id (str):
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnvGroup, Error]]
    """

    kwargs = _get_kwargs(
        env_group_id=env_group_id,
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    env_group_id: str,
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EnvGroup, Error]]:
    """Link service

     Link a particular service to a particular environment group.

    The linked service will have access to the environment variables and secret files in the group.

    Args:
        env_group_id (str):
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnvGroup, Error]
    """

    return sync_detailed(
        env_group_id=env_group_id,
        service_id=service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    env_group_id: str,
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EnvGroup, Error]]:
    """Link service

     Link a particular service to a particular environment group.

    The linked service will have access to the environment variables and secret files in the group.

    Args:
        env_group_id (str):
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnvGroup, Error]]
    """

    kwargs = _get_kwargs(
        env_group_id=env_group_id,
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    env_group_id: str,
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EnvGroup, Error]]:
    """Link service

     Link a particular service to a particular environment group.

    The linked service will have access to the environment variables and secret files in the group.

    Args:
        env_group_id (str):
        service_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnvGroup, Error]
    """

    return (
        await asyncio_detailed(
            env_group_id=env_group_id,
            service_id=service_id,
            client=client,
        )
    ).parsed
