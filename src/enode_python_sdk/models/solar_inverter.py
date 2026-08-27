import datetime as dt
from dataclasses import dataclass
from typing import Any

@dataclass
class SolarInverter:
    """Model Enode's Solar Inverter object"""
    id: str
    user_id: str
    vendor: str
    last_seen: dt.datetime
    is_reachable: bool
    capabilities: dict[str, Any]
    production_state: dict[str, Any]
    timezone: str
    scopes: list[str]
    information: dict[str, str]
    location: dict[str, str]
    hem_system_id: str
    timezone: dt.timezone
    created_at: dt.datetime
