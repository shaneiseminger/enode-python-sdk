from functools import cached_property

import httpx

from collections.abc import Callable, Mapping
from typing import TypeVar

from authlib.oauth2.rfc6749 import OAuth2Token
from authlib.integrations.httpx_client import OAuth2Client

from enode_python_sdk._configs import SANDBOX_ENDPOINTS, PRODUCTION_ENDPOINTS
from enode_python_sdk.models.page_response import PageResponse
from enode_python_sdk.models.result_collection import ResultCollection
from enode_python_sdk.models.user import User

T = TypeVar('T')

class Client:

    api_endpoint: str
    oauth_url: str
    client_id: str
    client_secret: str
    
    _API_TIMEOUT_RESPONSE=10.0
    _API_TIMEOUT_CONNECT=10.0
    _API_PAGE_SIZE: int=10

    def __init__(
            self,
            client_id: str,
            client_secret: str,
            *,
            production: bool=False):
        self.api_endpoint = PRODUCTION_ENDPOINTS.api_base_url if production else SANDBOX_ENDPOINTS.api_base_url
        self.oauth_url = PRODUCTION_ENDPOINTS.oauth_url if production else SANDBOX_ENDPOINTS.oauth_url
        self.client_id = client_id
        self.client_secret = client_secret

    @cached_property
    def client(self) -> httpx.Client:
        return httpx.Client(
            timeout=httpx.Timeout(
                timeout=self._API_TIMEOUT_RESPONSE, 
                connect=self._API_TIMEOUT_CONNECT
            ),
            headers={'Authorization': f"Bearer {self.access_token['access_token']}"}
        )

    @cached_property
    def access_token(self) -> OAuth2Token:
        oauth2_client = OAuth2Client(self.client_id, self.client_secret)
        try:
            return oauth2_client.fetch_token(
                self.oauth_url,
                timeout=self._API_TIMEOUT_RESPONSE
            )
        finally:
            oauth2_client.close()

    def users(self) -> ResultCollection:
        return ResultCollection(
            lambda after_cursor: self._request(
                method='GET',
                endpoint='/users',
                params = {'after': after_cursor, 'pageSize': self._API_PAGE_SIZE} if after_cursor else None,
                factory = lambda obj: User(obj['id'], obj['createdAt'])
            ),
        )

    def _request(
            self,
            method: str,
            endpoint: str,
            factory: Callable[[dict[str, object]], T],
            *,
            params: Mapping[str, object] | None = None,
            json: Mapping[str, object] | None = None
    ) -> PageResponse[T]:
        response = self.client.request(
            method,
            f"{self.api_endpoint.rstrip('/') + '/' + endpoint.lstrip('/')}",
            params=params,
            json=json,
        )
        response.raise_for_status()
        resp_data = response.json()

        print(resp_data)

        # TODO: Validation of response data

        return PageResponse(
            resp_data['data'],
            before=resp_data['pagination']['before'] if 'before' in resp_data['pagination'] else None,
            after=resp_data['pagination']['after'] if 'after' in resp_data['pagination'] else None,
            factory=factory,
        )

    def __enter__(self) -> 'Client':
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except:
            pass


    def close(self) -> None:
        if 'client' in self.__dict__:
            self.client.close()

