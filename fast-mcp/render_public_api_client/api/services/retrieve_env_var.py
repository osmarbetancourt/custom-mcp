from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.env_var import EnvVar
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    service_id: str,
    env_var_key: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/{service_id}/env-vars/{env_var_key}".format(
            service_id=service_id,
            env_var_key=env_var_key,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EnvVar, Error]]:
    if response.status_code == 200:
        response_200 = EnvVar.from_dict(response.json())

        return response_200
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
) -> Response[Union[EnvVar, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_id: str,
    env_var_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EnvVar, Error]]:
    """Retrieve environment variable

     Retrieve a particular environment variable for a particular service.

    This only applies to environment variables set directly on the service, not to environment variables
    in a linked environment group.

    Args:
        service_id (str):
        env_var_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnvVar, Error]]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        env_var_key=env_var_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: str,
    env_var_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EnvVar, Error]]:
    """Retrieve environment variable

     Retrieve a particular environment variable for a particular service.

    This only applies to environment variables set directly on the service, not to environment variables
    in a linked environment group.

    Args:
        service_id (str):
        env_var_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnvVar, Error]
    """

    return sync_detailed(
        service_id=service_id,
        env_var_key=env_var_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_id: str,
    env_var_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EnvVar, Error]]:
    """Retrieve environment variable

     Retrieve a particular environment variable for a particular service.

    This only applies to environment variables set directly on the service, not to environment variables
    in a linked environment group.

    Args:
        service_id (str):
        env_var_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnvVar, Error]]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        env_var_key=env_var_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: str,
    env_var_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EnvVar, Error]]:
    """Retrieve environment variable

     Retrieve a particular environment variable for a particular service.

    This only applies to environment variables set directly on the service, not to environment variables
    in a linked environment group.

    Args:
        service_id (str):
        env_var_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnvVar, Error]
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            env_var_key=env_var_key,
            client=client,
        )
    ).parsed
