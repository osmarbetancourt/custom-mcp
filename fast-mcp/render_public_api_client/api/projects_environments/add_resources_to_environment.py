from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.environment import Environment
from ...models.environment_resources_post_input import EnvironmentResourcesPOSTInput
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: EnvironmentResourcesPOSTInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/environments/{environment_id}/resources".format(
            environment_id=environment_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Environment, Error]]:
    if response.status_code == 200:
        response_200 = Environment.from_dict(response.json())

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
) -> Response[Union[Environment, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnvironmentResourcesPOSTInput,
) -> Response[Union[Environment, Error]]:
    """Add resources to environment

     Add resources to the environment with the provided ID.

    Args:
        environment_id (str):
        body (EnvironmentResourcesPOSTInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Environment, Error]]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnvironmentResourcesPOSTInput,
) -> Optional[Union[Environment, Error]]:
    """Add resources to environment

     Add resources to the environment with the provided ID.

    Args:
        environment_id (str):
        body (EnvironmentResourcesPOSTInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Environment, Error]
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnvironmentResourcesPOSTInput,
) -> Response[Union[Environment, Error]]:
    """Add resources to environment

     Add resources to the environment with the provided ID.

    Args:
        environment_id (str):
        body (EnvironmentResourcesPOSTInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Environment, Error]]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnvironmentResourcesPOSTInput,
) -> Optional[Union[Environment, Error]]:
    """Add resources to environment

     Add resources to the environment with the provided ID.

    Args:
        environment_id (str):
        body (EnvironmentResourcesPOSTInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Environment, Error]
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
