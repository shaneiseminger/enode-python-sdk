import datetime as dt
from dataclasses import dataclass
from typing import Any

@dataclass
class Hem:
    """Model Enode's HEM object"""
    id: str
    user_id: str
    location_id: str
    # Unlike with other objects, Enode puts last_seen under the
    # `status` object. Let's normalize it.
    last_seen: dt.datetime
    # The `status` object appears to only have one property (energy), so collapse that.
    status_energy: dict[str, Any]
