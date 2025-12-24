import sqlite3

DB_PATH = "data/npc_log.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS npcs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                location TEXT,
                dialogue TEXT,
                vibe TEXT,
                rarity TEXT,
                created_at TEXT
            )
        """)
