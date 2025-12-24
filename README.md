# 🎮 NPC.log

> **Document the background characters of your life**

NPC.log is a Python-based journaling application that treats real-life strangers as NPCs (Non-Player Characters) in an RPG-style world. Capture memorable encounters, quirky dialogues, and unique vibes from the people you meet every day.

## ✨ Features

- 📝 **Structured NPC Logging** - Record name, location, dialogue, vibe, and rarity
- 🗄️ **SQLite Persistence** - All your NPCs stored locally and securely
- 🎯 **Smart Filtering** - Find NPCs by vibe (chill/neutral/unhinged) or rarity (common/rare/legendary)
- 📊 **Statistics Dashboard** - Track your NPC collection with detailed stats
- 🏗️ **Clean Architecture** - Layered design with repository pattern
- 🔒 **Privacy-First** - All data stays on your machine
- 🎨 **Rich CLI Interface** - Beautiful emoji-enhanced terminal experience

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/npc-log.git
cd npc-log

# Run the application (no dependencies needed!)
python main.py
```

## 📁 Project Structure

```
npc-log/
├── 📂 core/
│   ├── 🐍 __init__.py
│   ├── 🐍 database.py      # Database connection & initialization
│   ├── 🐍 repository.py    # CRUD operations
│   └── 🐍 models.py         # Data models & validation
├── 📂 ui/
│   ├── 🐍 __init__.py
│   └── 🐍 cli.py            # Command-line interface
├── 📂 utils/
│   ├── 🐍 __init__.py
│   └── 🐍 helpers.py        # Utility functions
├── 📂 data/
│   └── 💾 npc_log.db       # SQLite database (created automatically)
├── 🐍 __init__.py           # Package initialization
├── 🐍 main.py               # Application entry point
├── 📋 requirements.txt      # Dependencies (none yet!)
├── 🚫 .gitignore            # Git ignore rules
└── 📖 README.md             # You are here
```

## 🎯 Usage

### Main Menu
```
🎮 NPC.log — Background Character Database

[1] Log new NPC
[2] View all NPCs
[3] Filter NPCs
[4] View stats
[5] Delete NPC
[0] Exit
```

### Example: Logging an NPC
```
📝 New NPC Entry

NPC Codename: Coffee Shop Philosopher
Location: Downtown Café
Memorable Dialogue: Life is just a series of espresso shots
Vibe (chill/neutral/unhinged): chill
Rarity (common/rare/legendary): rare

✅ NPC #1 logged successfully!
```

### Example: Viewing NPCs
```
📋 All NPCs (3 total)

🌟 NPC #3 — Shadow Merchant
   📍 Dark Alley, District 9
   💬 "Prices negotiable... for the right customer."
   😎 Chill | Legendary
   🕒 2024-12-24 15:30:22

🔵 NPC #2 — Guard Captain
   📍 City Gates
   💬 "None shall pass without proper documentation!"
   😐 Neutral | Rare
   🕒 2024-12-24 14:15:10

⚪ NPC #1 — Bartender Joe
   📍 The Rusty Tankard
   💬 "Rough day? I've got just the thing."
   🤪 Unhinged | Common
   🕒 2024-12-24 13:45:55
```

## 🛠️ Tech Stack

- 🐍 **Python 3.8+** - Core language
- 💾 **SQLite3** - Local database
- 🖥️ **CLI** - Terminal interface
- 🏗️ **Repository Pattern** - Clean architecture

## 🎨 NPC Attributes

### Vibe Options
- 😎 **Chill** - Relaxed, friendly, easygoing
- 😐 **Neutral** - Normal, unremarkable, everyday
- 🤪 **Unhinged** - Chaotic, bizarre, memorable

### Rarity Tiers
- ⚪ **Common** - Everyday encounters
- 🔵 **Rare** - Unusual or memorable
- 🌟 **Legendary** - Once-in-a-lifetime characters

## 🔮 Roadmap

### Version 1.0 (Current)
- ✅ Core CLI functionality
- ✅ CRUD operations
- ✅ Filtering and statistics
- ✅ SQLite storage

### Version 2.0 (Planned)
- 🔲 REST API with FastAPI
- 🔲 Web interface
- 🔲 Search by name/dialogue
- 🔲 Export to JSON/CSV
- 🔲 Import from file
- 🔲 Tags/categories system

### Version 3.0 (Future)
- 🔲 NPC relationship mapping
- 🔲 Location-based tracking
- 🔲 Photos/attachments support
- 🔲 Cloud sync (optional)
- 🔲 Mobile app

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📜 License

MIT License - feel free to use this project however you'd like!

## 💬 Philosophy

Every person you meet has a story. Some are quest-givers, some are merchants, and some are just... unhinged. NPC.log helps you remember these fleeting encounters and build a personal database of the interesting characters that populate your world.

---

**Made with ☕ and 🎮 by [Your Name]**

*"The world is full of NPCs. Some of them are worth documenting."*