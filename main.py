"""
NPC.log - Background Character Database
A CLI tool for logging and tracking memorable NPCs
"""
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent))

from core.database import init_db
from ui.cli import CLI

def main():
    """Initialize database and run CLI"""
    try:
        init_db()
        CLI.run()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting NPC.log...")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()