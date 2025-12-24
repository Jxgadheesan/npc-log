from dataclasses import dataclass
from datetime import datetime

@dataclass
class NPC:
    name: str
    location: str
    dialogue: str
    vibe: str
    rarity: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M")
