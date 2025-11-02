import pymem
from pymem.process import module_from_name

# Import offsets
from src.memory.offsets import CUR_MGR_POINTER, CUR_MGR_OFFSET

def main():
    try:
        pm = pymem.Pymem("Wow.exe")
    except pymem.exception.ProcessNotFound:
        print("World of Warcraft process not found. Please make sure the game is running.")
        return

    try:
        # Get the base address of the Wow.exe module
        base_address = module_from_name(pm.process_handle, "Wow.exe").lpBaseOfDll

        # Read the pointer to the object manager
        try:
            object_manager_ptr = pm.read_uint(base_address + CUR_MGR_POINTER)
            print(f"Object Manager Pointer: {hex(object_manager_ptr)}")

            # Read the object manager address
            object_manager = pm.read_uint(object_manager_ptr + CUR_MGR_OFFSET)
            print(f"Object Manager Address: {hex(object_manager)}")

        except pymem.exception.MemoryReadError as e:
            print(f"Error reading memory: {e}")
            print("Please ensure the bot is compatible with the game version (3.3.5a).")

    finally:
        # Always close the handle to the process
        pm.close_process()
        print("Process handle closed.")

if __name__ == "__main__":
    main()
