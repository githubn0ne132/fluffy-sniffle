# AGENTS.MD: WoW 3.3.5a Bot Development Guide

This document outlines the architecture, conventions, and technical details for developing the Python-based World of Warcraft (3.3.5a) bot.

## 1. Core Architecture

The bot will follow a modular design to separate concerns and improve maintainability. The key components are:

- **Memory Reader:** Responsible for attaching to the `WoW.exe` process, finding memory offsets, and reading game state data.
- **Client Controller:** Handles sending simulated keyboard and mouse inputs to the game client.
- **Object Manager:** Parses the raw memory data into structured game objects (Player, Target, NPCs, etc.).
- **Rotation Engine:** Implements the combat logic and decision-making for different character classes.
- **Main Application:** The entry point that initializes and coordinates all other components.

## 2. Technical Stack and Libraries

- **Python 3.x:** The core programming language.
- **`pymem`:** For reading process memory.
- **`pydirectinput` or `pyautogui`:** For simulating keyboard and mouse input.
- **`ctypes`:** For low-level data type handling and calling Windows APIs.

## 3. Memory Offsets (WoW 3.3.5a - Build 12340)

This section will be populated with the memory offsets as they are discovered. Reverse engineering tools like Cheat Engine and Ghidra will be used to find these values.

**Base Addresses:**
- `ObjectManager`: TBD
- `LocalPlayerGUID`: TBD

**Pointer Chains:**
- `PlayerName`: `(ClientConnection + 0xoffset) -> ...`
- `PlayerHealth`: `(PlayerBase + 0xoffset) -> ...`

*Note: This section is critical and will require significant reverse engineering effort.*

## 4. Development Workflow

1. **Implement Memory Reader:** Start by creating a robust memory reader that can reliably attach to the WoW process and read basic data.
2. **Reverse Engineer Offsets:** Use Cheat Engine to find the key offsets for the Object Manager and player data.
3. **Develop Object Manager:** Create Python classes to represent game objects and populate them with data from the memory reader.
4. **Implement Client Controller:** Develop a simple and reliable way to send keystrokes and mouse clicks to the client.
5. **Build Rotation Engine:** Start with a simple combat rotation for a specific class.
6. **Integrate and Test:** Combine all components and test them in-game.

## 5. Coding Conventions

- **Style:** Follow PEP 8 for Python code.
- **Naming:** Use descriptive names for variables and functions (e.g., `get_player_health()` instead of `get_hp()`).
- **Modularity:** Keep each component in its own module/package.
- **Error Handling:** Implement robust error handling, especially for memory reading and process attachment.

## 6. Anti-Cheat Considerations

- **Memory Reading:** Prioritize memory reading over writing. It is generally less detectable.
- **Input Simulation:** Use realistic delays and patterns for simulated input to avoid detection.
- **DLL Injection:** Avoid DLL injection for now, as it is a more advanced and risky technique. We can explore it later if needed.

## 7. Setup and Running

1. **Setup the Python Environment:**
   ```bash
   python setup_env.py
   ```
   This will download a local Python binary and install the required dependencies.

2. **Run the bot:**
   ```bash
   # You can use the python executable from the .env file
   # For example, on Windows:
   #  .\python-3.11.4-embed-amd64\python.exe main.py
   python main.py
   ```

*This document is a living guide and will be updated as the project progresses.*
