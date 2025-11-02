# src/memory/memory_reader.py

import pymem

class MemoryReader:
    def __init__(self, process_name="Wow.exe"):
        self.process_name = process_name
        self.pm = None

    def attach(self):
        try:
            self.pm = pymem.Pymem(self.process_name)
            print(f"Successfully attached to {self.process_name}")
            return True
        except pymem.exception.ProcessNotFound:
            print(f"Error: Could not find process {self.process_name}")
            return False

    def get_base_address(self):
        if self.pm:
            return self.pm.base_address
        return None
