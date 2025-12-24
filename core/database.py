import sqlite3
from pathlib import Path
from contextlib import contextmanager

DB_PATH = Path("data/npc_log.db")

@contextmanager
def get_connection():
    """Context manager for database connections"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Initialize the database with required tables"""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS npcs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                dialogue TEXT NOT NULL,
                vibe TEXT NOT NULL,
                rarity TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_rarity ON npcs(rarity)
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_vibe ON npcs(vibe)
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_created_at ON npcs(created_at)
        """)
        conn.commit()