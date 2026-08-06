import datetime
from dataclasses import dataclass

@dataclass
class User:
    id: str
    created_at: datetime.datetime