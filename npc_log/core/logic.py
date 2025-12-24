from .storage import get_connection
from .models import NPC

def add_npc(npc: NPC):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO npcs 
            (name, location, dialogue, vibe, rarity, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            npc.name,
            npc.location,
            npc.dialogue,
            npc.vibe,
            npc.rarity,
            npc.created_at
        ))
