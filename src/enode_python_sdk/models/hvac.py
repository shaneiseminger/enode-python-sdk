import datetime as dt
from dataclasses import dataclass
from typing import Any

@dataclass
class Hvac:
    """Model Enode's HVAC object"""
    id: str
    user_id: str
    vendor: str
    last_seen: dt.datetime
    is_reachable: bool
    consumption_rate: float,
    information: dict[str, Any]
    location_id: str
    capabilities: dict[str, Any]
    thermostatState: dict[str, Any]
    temperatureState: dict[str, Any]
    scopes: list[str]