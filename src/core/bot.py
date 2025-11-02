# src/core/bot.py

from src.memory.memory_reader import MemoryReader
from src.memory.object_manager import ObjectManager

class Bot:
    def __init__(self):
        print("Initializing bot...")
        self.memory_reader = MemoryReader()
        self.object_manager = ObjectManager(self.memory_reader)

    def run(self):
        print("Bot is running...")
        if self.memory_reader.attach():
            print("Attached to WoW process.")
            object_manager_base = self.object_manager.get_object_manager_base()
            if object_manager_base:
                print(f"Object Manager base address found: {hex(object_manager_base)}")
            else:
                print("Could not find Object Manager base address.")
        else:
            print("Could not attach to WoW process.")
