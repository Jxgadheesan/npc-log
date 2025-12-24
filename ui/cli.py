from core.models import NPC
from core.repository import NPCRepository

class CLI:
    """Command-line interface for NPC logging"""
    
    MENU = """
🎮 NPC.log — Background Character Database

[1] Log new NPC
[2] View all NPCs
[3] Filter NPCs
[4] View stats
[5] Delete NPC
[0] Exit

Choose an option: """
    
    @staticmethod
    def clear_screen():
        print("\n" * 2)
    
    @staticmethod
    def get_input(prompt: str, valid_options: list = None) -> str:
        """Get validated input from user"""
        while True:
            value = input(prompt).strip()
            if not value:
                print("❌ Input cannot be empty. Try again.")
                continue
            if valid_options and value.lower() not in valid_options:
                print(f"❌ Invalid option. Choose from: {', '.join(valid_options)}")
                continue
            return value.lower() if valid_options else value
    
    @staticmethod
    def log_npc():
        """Interactive NPC logging"""
        print("\n📝 New NPC Entry\n")
        
        name = CLI.get_input("NPC Codename: ")
        location = CLI.get_input("Location: ")
        dialogue = CLI.get_input("Memorable Dialogue: ")
        vibe = CLI.get_input(
            "Vibe (chill/neutral/unhinged): ",
            valid_options=['chill', 'neutral', 'unhinged']
        )
        rarity = CLI.get_input(
            "Rarity (common/rare/legendary): ",
            valid_options=['common', 'rare', 'legendary']
        )
        
        try:
            npc = NPC(name, location, dialogue, vibe, rarity)
            npc_id = NPCRepository.add(npc)
            print(f"\n✅ NPC #{npc_id} logged successfully!")
        except Exception as e:
            print(f"\n❌ Error logging NPC: {e}")
    
    @staticmethod
    def view_all():
        """Display all NPCs"""
        npcs = NPCRepository.get_all()
        
        if not npcs:
            print("\n📭 No NPCs logged yet.")
            return
        
        print(f"\n📋 All NPCs ({len(npcs)} total)\n")
        CLI._display_npcs(npcs)
    
    @staticmethod
    def filter_npcs():
        """Filter and display NPCs"""
        print("\n🔍 Filter Options")
        print("[1] By Vibe")
        print("[2] By Rarity")
        print("[3] Both")
        
        choice = CLI.get_input("Choose filter: ", valid_options=['1', '2', '3'])
        
        vibe = None
        rarity = None
        
        if choice in ['1', '3']:
            vibe = CLI.get_input(
                "Vibe (chill/neutral/unhinged): ",
                valid_options=['chill', 'neutral', 'unhinged']
            )
        
        if choice in ['2', '3']:
            rarity = CLI.get_input(
                "Rarity (common/rare/legendary): ",
                valid_options=['common', 'rare', 'legendary']
            )
        
        npcs = NPCRepository.filter_by(vibe=vibe, rarity=rarity)
        
        if not npcs:
            print("\n📭 No NPCs match your filters.")
            return
        
        print(f"\n📋 Filtered NPCs ({len(npcs)} found)\n")
        CLI._display_npcs(npcs)
    
    @staticmethod
    def view_stats():
        """Display statistics"""
        total = NPCRepository.count()
        all_npcs = NPCRepository.get_all()
        
        print(f"\n📊 NPC Statistics\n")
        print(f"Total NPCs: {total}")
        
        if total > 0:
            vibes = {}
            rarities = {}
            
            for npc in all_npcs:
                vibes[npc.vibe] = vibes.get(npc.vibe, 0) + 1
                rarities[npc.rarity] = rarities.get(npc.rarity, 0) + 1
            
            print("\nBy Vibe:")
            for vibe, count in vibes.items():
                print(f"  {vibe.capitalize()}: {count}")
            
            print("\nBy Rarity:")
            for rarity, count in rarities.items():
                print(f"  {rarity.capitalize()}: {count}")
    
    @staticmethod
    def delete_npc():
        """Delete an NPC by ID"""
        try:
            npc_id = int(CLI.get_input("Enter NPC ID to delete: "))
            npc = NPCRepository.get_by_id(npc_id)
            
            if not npc:
                print(f"\n❌ NPC #{npc_id} not found.")
                return
            
            print(f"\nAre you sure you want to delete NPC #{npc_id} ({npc.name})? (yes/no): ", end="")
            confirm = input().strip().lower()
            
            if confirm == 'yes':
                if NPCRepository.delete(npc_id):
                    print(f"\n✅ NPC #{npc_id} deleted successfully.")
                else:
                    print(f"\n❌ Failed to delete NPC #{npc_id}.")
            else:
                print("\n❌ Deletion cancelled.")
        except ValueError:
            print("\n❌ Invalid ID. Please enter a number.")
    
    @staticmethod
    def _display_npcs(npcs: list):
        """Helper to display NPC list"""
        for npc in npcs:
            emoji = {"common": "⚪", "rare": "🔵", "legendary": "🌟"}
            vibe_emoji = {"chill": "😎", "neutral": "😐", "unhinged": "🤪"}
            
            print(f"{emoji.get(npc.rarity, '•')} NPC #{npc.id} — {npc.name}")
            print(f"   📍 {npc.location}")
            print(f"   💬 \"{npc.dialogue}\"")
            print(f"   {vibe_emoji.get(npc.vibe, '•')} {npc.vibe.capitalize()} | {npc.rarity.capitalize()}")
            print(f"   🕒 {npc.created_at}")
            print()
    
    @staticmethod
    def run():
        """Main CLI loop"""
        while True:
            choice = input(CLI.MENU).strip()
            CLI.clear_screen()
            
            if choice == '1':
                CLI.log_npc()
            elif choice == '2':
                CLI.view_all()
            elif choice == '3':
                CLI.filter_npcs()
            elif choice == '4':
                CLI.view_stats()
            elif choice == '5':
                CLI.delete_npc()
            elif choice == '0':
                print("👋 Thanks for using NPC.log!")
                break
            else:
                print("❌ Invalid option. Please choose 0-5.")
            
            input("\nPress Enter to continue...")
            CLI.clear_screen()