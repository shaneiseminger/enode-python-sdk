import datetime as dt
from dataclasses import dataclass
from typing import Any

@dataclass
class Meter:
    """Model Enode's Meter object"""
    id: str
    user_id: str
    vendor: str
    is_reachable: bool
    consumption_rate: float
    location_id: str
    information: dict[str, Any]
    temperatureState: dict[str, Any]
    thermostatState: dict[str, Any]
    capabilities: dict[str, Any]
    scopes: list[str]
    latitude: float
    longitude: float
    last_seen: dt.timezone
    created_at: dt.datetime
