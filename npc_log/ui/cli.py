from npc_log.core.models import NPC
from npc_log.core.logic import add_npc

def run_cli():
    print("🎮 NPC.log — documenting background characters\n")

    name = input("NPC Codename: ")
    location = input("Location: ")
    dialogue = input("Dialogue: ")
    vibe = input("Vibe (chill/neutral/unhinged): ")
    rarity = input("Rarity (common/rare/legendary): ")

    npc = NPC(name, location, dialogue, vibe, rarity)
    add_npc(npc)

    print("\n✔ NPC logged successfully.")
