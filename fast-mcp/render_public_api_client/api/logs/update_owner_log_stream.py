from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.update_owner_log_stream_body import UpdateOwnerLogStreamBody
from ...types import Response


def _get_kwargs(
    owner_id: str,
    *,
    body: UpdateOwnerLogStreamBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/logs/streams/owner/{owner_id}".format(
            owner_id=owner_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateOwnerLogStreamBody,
) -> Response[Error]:
    """Update log stream

     Updates log stream information for the specified workspace. All logs for resources owned by this
    workspace will be sent to this log stream unless overridden by individual resources.

    Args:
        owner_id (str):
        body (UpdateOwnerLogStreamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateOwnerLogStreamBody,
) -> Optional[Error]:
    """Update log stream

     Updates log stream information for the specified workspace. All logs for resources owned by this
    workspace will be sent to this log stream unless overridden by individual resources.

    Args:
        owner_id (str):
        body (UpdateOwnerLogStreamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        owner_id=owner_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateOwnerLogStreamBody,
) -> Response[Error]:
    """Update log stream

     Updates log stream information for the specified workspace. All logs for resources owned by this
    workspace will be sent to this log stream unless overridden by individual resources.

    Args:
        owner_id (str):
        body (UpdateOwnerLogStreamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    owner_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateOwnerLogStreamBody,
) -> Optional[Error]:
    """Update log stream

     Updates log stream information for the specified workspace. All logs for resources owned by this
    workspace will be sent to this log stream unless overridden by individual resources.

    Args:
        owner_id (str):
        body (UpdateOwnerLogStreamBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            owner_id=owner_id,
            client=client,
            body=body,
        )
    ).parsed
