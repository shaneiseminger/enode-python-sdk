import datetime
from dataclasses import dataclass

@dataclass
class User:
    """Model Enode's user object"""
    id: str
    created_at: datetime.datetime