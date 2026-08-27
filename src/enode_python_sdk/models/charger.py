import datetime as dt
from dataclasses import dataclass
from typing import Any

@dataclass
class Location:
    """Model Enode's Charger object"""
    id: str
    user_id: str
    vendor: str
    last_seen: dt.datetime
    is_reachable: bool
    consumption_rate: float
    information: dict[str, Any]
    # Enode seems to be inconsistent with it's location representation in
    # location-aware objects. Probably should normalize this.
    location: dict[str, Any]
    # Extract locationId from location object for consistency.
    location_id: str
    information: dict[str, Any]
    capabilities: dict[str, Any]
    charge_state: dict[str, Any]
    scopes: list[str]
