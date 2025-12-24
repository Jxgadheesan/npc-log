from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

@dataclass
class NPC:
    name: str
    location: str
    dialogue: str
    vibe: str
    rarity: str
    id: Optional[int] = None
    created_at: Optional[str] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Validate vibe
        valid_vibes = ['chill', 'neutral', 'unhinged']
        if self.vibe.lower() not in valid_vibes:
            raise ValueError(f"Vibe must be one of: {', '.join(valid_vibes)}")
        
        # Validate rarity
        valid_rarities = ['common', 'rare', 'legendary']
        if self.rarity.lower() not in valid_rarities:
            raise ValueError(f"Rarity must be one of: {', '.join(valid_rarities)}")
    
    def to_dict(self):
        return asdict(self)