from npc_log.core.storage import init_db
from npc_log.ui.cli import run_cli

def main():
    init_db()
    run_cli()

if __name__ == "__main__":
    main()
