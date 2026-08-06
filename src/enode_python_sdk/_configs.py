from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class _Endpoints:
    api_base_url: str
    oauth_url: str

SANDBOX_ENDPOINTS : Final[_Endpoints] = _Endpoints(
    api_base_url = "https://enode-api.sandbox.enode.io/",
    oauth_url = "https://oauth.sandbox.enode.io/oauth2/token",
)

PRODUCTION_ENDPOINTS : Final[_Endpoints] = _Endpoints(
    api_base_url = "https://enode-api.production.enode.io/",
    oauth_url = "https://oauth.production.enode.io/oauth2/token",
)
