import datetime as dt
from dataclasses import dataclass

@dataclass
class Location:
    """Model Enode's Location object"""
    id: str
    user_id: str
    name: str
    latitude: float
    longitude: float
    timezone: dt.timezone
    created_at: dt.datetime
