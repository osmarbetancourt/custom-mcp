from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.env_var_key_generate_value import EnvVarKeyGenerateValue
from ...models.env_var_key_value import EnvVarKeyValue
from ...models.env_var_with_cursor import EnvVarWithCursor
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    service_id: str,
    *,
    body: list[Union["EnvVarKeyGenerateValue", "EnvVarKeyValue"]],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/services/{service_id}/env-vars".format(
            service_id=service_id,
        ),
    }

    _kwargs["json"] = []
    for componentsschemasenv_var_input_array_item_data in body:
        componentsschemasenv_var_input_array_item: dict[str, Any]
        if isinstance(componentsschemasenv_var_input_array_item_data, EnvVarKeyValue):
            componentsschemasenv_var_input_array_item = (
                componentsschemasenv_var_input_array_item_data.to_dict()
            )
        else:
            componentsschemasenv_var_input_array_item = (
                componentsschemasenv_var_input_array_item_data.to_dict()
            )

        _kwargs["json"].append(componentsschemasenv_var_input_array_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, list["EnvVarWithCursor"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EnvVarWithCursor.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[Error, list["EnvVarWithCursor"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["EnvVarKeyGenerateValue", "EnvVarKeyValue"]],
) -> Response[Union[Error, list["EnvVarWithCursor"]]]:
    """Update environment variables

     Replace all environment variables for a service with the provided list of environment variables.

    Args:
        service_id (str):
        body (list[Union['EnvVarKeyGenerateValue', 'EnvVarKeyValue']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['EnvVarWithCursor']]]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["EnvVarKeyGenerateValue", "EnvVarKeyValue"]],
) -> Optional[Union[Error, list["EnvVarWithCursor"]]]:
    """Update environment variables

     Replace all environment variables for a service with the provided list of environment variables.

    Args:
        service_id (str):
        body (list[Union['EnvVarKeyGenerateValue', 'EnvVarKeyValue']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['EnvVarWithCursor']]
    """

    return sync_detailed(
        service_id=service_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["EnvVarKeyGenerateValue", "EnvVarKeyValue"]],
) -> Response[Union[Error, list["EnvVarWithCursor"]]]:
    """Update environment variables

     Replace all environment variables for a service with the provided list of environment variables.

    Args:
        service_id (str):
        body (list[Union['EnvVarKeyGenerateValue', 'EnvVarKeyValue']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['EnvVarWithCursor']]]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[Union["EnvVarKeyGenerateValue", "EnvVarKeyValue"]],
) -> Optional[Union[Error, list["EnvVarWithCursor"]]]:
    """Update environment variables

     Replace all environment variables for a service with the provided list of environment variables.

    Args:
        service_id (str):
        body (list[Union['EnvVarKeyGenerateValue', 'EnvVarKeyValue']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['EnvVarWithCursor']]
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            client=client,
            body=body,
        )
    ).parsed
