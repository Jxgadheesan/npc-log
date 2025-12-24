from typing import List, Optional
from core.database import get_connection
from core.models import NPC

class NPCRepository:
    """Handle all database operations for NPCs"""
    
    @staticmethod
    def add(npc: NPC) -> int:
        """Add a new NPC to the database"""
        with get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO npcs (name, location, dialogue, vibe, rarity, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                npc.name,
                npc.location,
                npc.dialogue,
                npc.vibe.lower(),
                npc.rarity.lower(),
                npc.created_at
            ))
            return cursor.lastrowid
    
    @staticmethod
    def get_all() -> List[NPC]:
        """Retrieve all NPCs from the database"""
        with get_connection() as conn:
            cursor = conn.execute("""
                SELECT id, name, location, dialogue, vibe, rarity, created_at
                FROM npcs
                ORDER BY created_at DESC
            """)
            return [NPC(
                id=row['id'],
                name=row['name'],
                location=row['location'],
                dialogue=row['dialogue'],
                vibe=row['vibe'],
                rarity=row['rarity'],
                created_at=row['created_at']
            ) for row in cursor.fetchall()]
    
    @staticmethod
    def get_by_id(npc_id: int) -> Optional[NPC]:
        """Retrieve a specific NPC by ID"""
        with get_connection() as conn:
            cursor = conn.execute("""
                SELECT id, name, location, dialogue, vibe, rarity, created_at
                FROM npcs
                WHERE id = ?
            """, (npc_id,))
            row = cursor.fetchone()
            if row:
                return NPC(
                    id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    dialogue=row['dialogue'],
                    vibe=row['vibe'],
                    rarity=row['rarity'],
                    created_at=row['created_at']
                )
            return None
    
    @staticmethod
    def filter_by(vibe: Optional[str] = None, rarity: Optional[str] = None) -> List[NPC]:
        """Filter NPCs by vibe and/or rarity"""
        query = "SELECT id, name, location, dialogue, vibe, rarity, created_at FROM npcs WHERE 1=1"
        params = []
        
        if vibe:
            query += " AND vibe = ?"
            params.append(vibe.lower())
        
        if rarity:
            query += " AND rarity = ?"
            params.append(rarity.lower())
        
        query += " ORDER BY created_at DESC"
        
        with get_connection() as conn:
            cursor = conn.execute(query, params)
            return [NPC(
                id=row['id'],
                name=row['name'],
                location=row['location'],
                dialogue=row['dialogue'],
                vibe=row['vibe'],
                rarity=row['rarity'],
                created_at=row['created_at']
            ) for row in cursor.fetchall()]
    
    @staticmethod
    def delete(npc_id: int) -> bool:
        """Delete an NPC by ID"""
        with get_connection() as conn:
            cursor = conn.execute("DELETE FROM npcs WHERE id = ?", (npc_id,))
            return cursor.rowcount > 0
    
    @staticmethod
    def count() -> int:
        """Get total count of NPCs"""
        with get_connection() as conn:
            cursor = conn.execute("SELECT COUNT(*) as count FROM npcs")
            return cursor.fetchone()['count']