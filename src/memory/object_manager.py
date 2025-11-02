# src/memory/object_manager.py

from src.memory.memory_reader import MemoryReader
from src.memory import offsets

class ObjectManager:
    def __init__(self, memory_reader: MemoryReader):
        self.memory_reader = memory_reader

    def get_object_manager_base(self):
        if not self.memory_reader or not self.memory_reader.pm:
            return None

        base_address = self.memory_reader.get_base_address()
        if not base_address:
            return None

        try:
            client_connection = self.memory_reader.pm.read_uint(
                base_address + offsets.STATIC_CLIENT_CONNECTION
            )
            object_manager_base = self.memory_reader.pm.read_uint(
                client_connection + offsets.OBJECT_MANAGER_OFFSET
            )
            return object_manager_base
        except Exception as e:
            print(f"Error reading object manager base: {e}")
            return None
