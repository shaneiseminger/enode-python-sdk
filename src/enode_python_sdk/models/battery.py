import datetime as dt
from dataclasses import dataclass
from typing import Any

@dataclass
class Location:
    """Model Enode's Battery object"""
    id: str
    user_id: str
    hem_system_id: str
    vendor: str
    last_seen: dt.datetime
    is_reachable: bool
    charge_state: dict[str, str | float | int]
    config: dict[str, str]
    information: dict[str, str]
    information: dict[str, Any]
    # Enode seems to be inconsistent with it's location representation in
    # location-aware objects. Probably should normalize this.
    location: dict[str, Any]
    # Extract locationId from location object for consistency.
    location_id: str
    scopes: list[str]
