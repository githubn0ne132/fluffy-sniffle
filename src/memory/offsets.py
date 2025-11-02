# Offsets for WoW Client Version 3.3.5a (Build 12340)
# This file consolidates and refactors offsets from all provided sources into a single, comprehensive list.

# =============================================================================
# --- Player, Target, and GUIDs ---
# =============================================================================
PLAYER_NAME = 0xC79D18
PLAYER_BASE = 0xD38AE4
LOCAL_GUID = 0xCA1238
CURRENT_TARGET_GUID = 0xBD07B0
LAST_TARGET_GUID = 0xBD07B8
MOUSE_OVER_GUID = 0xBD07A0
FOLLOW_GUID = 0xCA11F8
PET_GUID = 0xC234D0
COMBO_POINTS = 0xBD084D

# =============================================================================
# --- Object Manager ---
# =============================================================================
CUR_MGR_POINTER = 0xC79CE0
CUR_MGR_OFFSET = 0x2ED0
FIRST_OBJECT = 0xAC
NEXT_OBJECT = 0x3C
OBJECT_MANAGER_LOCAL_GUID = 0xC0

# =============================================================================
# --- Game State & World ---
# =============================================================================
GAME_STATE = 0xB6A9E0
IS_LOADING_OR_CONNECTING = 0xB6AA38
IS_INGAME = 0xBEBAA4
IS_WORLD_LOADED = 0xBEBA40
MAP_ID = 0xADFBC4
ZONE_ID = 0xBD080C
GET_ZONE_ID = ZONE_ID # Alias
GET_MINIMAP_ZONE_TEXT = 0xBD077C
ZONE_TEXT = 0xBD0788
GET_ZONE_TEXT = ZONE_TEXT # Alias
SUB_ZONE_TEXT = 0xBD0784
GET_SUB_ZONE_TEXT = SUB_ZONE_TEXT # Alias
GET_INTERNAL_MAP_NAME = 0xCE06D0
CORPSE_X = 0xBD0A58
CORPSE_Y = CORPSE_X + 4
CORPSE_Z = CORPSE_X + 8
CORPSE_POSITION = CORPSE_X # Alias

# =============================================================================
# --- Object & Unit Properties ---
# =============================================================================
WOW_OBJECT_DESCRIPTOR = 0x8
WOW_OBJECT_TYPE = 0x14
WOW_UNIT_POSITION = 0x798
WOW_GAMEOJECT_POSITION = 0x1D8
WOW_DYNOBJECT_POSITION = 0xE8
CLIMB_ANGLE = 0x858
WOW_UNIT_IS_AUTO_ATTACKING = 0xA20
CURRENTLY_CASTING_SPELL_ID = 0xA6C
CURRENTLY_CHANNELING_SPELL_ID = 0xA80
MOVEMENT_FIELD = 0xD8
IS_BOBBING_OFFSET = 0xBC
# Unit Name Offsets from DB Entry
UNIT_NAME_1 = 0x964
UNIT_NAME_2 = 0x5C

# =============================================================================
# --- Auras ---
# =============================================================================
CG_UNIT_AURA = 0x556E10
AURA_COUNT_1 = 0xDD0
AURA_COUNT_2 = 0xC54
AURA_TABLE_1 = 0xC50
AURA_TABLE_2 = 0xC58
AURA_SIZE = 0x18
AURA_SPELL_ID = 0x8

# =============================================================================
# --- Battleground & PvP ---
# =============================================================================
BATTLEGROUND_FINISHED = 0xBEA588
IS_BATTLEGROUND_FINISHED = BATTLEGROUND_FINISHED # Alias
BATTLEGROUND_STATUS = 0xBEA4D0

# =============================================================================
# --- Spells, Cooldowns & Runes ---
# =============================================================================
KNOWN_SPELL = 0xBE5D88
SPELL_COOLDOWN_PTR = 0xD3F5AC
RUNES = 0xC24388
RUNE_TYPE = 0xC24304

# =============================================================================
# --- Camera ---
# =============================================================================
CG_WORLD_FRAME_GET_ACTIVE_CAMERA = 0x4F5960
CAMERA_POINTER = 0xB7436C
CAMERA_OFFSET = 0x7E20
CAMERA_X = 0x8
CAMERA_Y = 0xC
CAMERA_Z = 0x10
CAMERA_FOLLOW_GUID = 0x88

# =============================================================================
# --- Click To Move (CTM) ---
# =============================================================================
CTM_BASE = 0xCA11D8
CTM_POINTER = 0xBD08F4 # Points to a structure that contains the CTM_BASE
CTM_IS_ENABLED_OFFSET = 0x30 # Offset from CTM_POINTER to get a value that indicates if CTM is active
# Offsets from CTM_BASE
CTM_ACTION = CTM_BASE + 0x1C
CTM_X = CTM_BASE + 0x8C
CTM_Y = CTM_BASE + 0x90
CTM_Z = CTM_BASE + 0x94
CTM_DISTANCE = CTM_BASE + 0xC
CTM_GUID = CTM_BASE + 0x20
CTM_TURN_SPEED = CTM_BASE + 0x4

# =============================================================================
# --- Player Movement & Status ---
# =============================================================================
IS_FLYING_OFFSET = 0x44
IS_FLYING_MASK = 0x2000000
IS_SWIMMING_OFFSET = 0xA30
IS_SWIMMING_MASK = 0x200000

# =============================================================================
# --- UI & Interface ---
# =============================================================================
LOOT_WINDOW_OPEN = 0xBFA8D8
CHATBOX_IS_OPEN = 0xD41660
NB_ITEMS_SELL_BY_MERCHANT = 0xBFA3F0
AUTO_LOOT_ACTIVATE_POINTER = 0xBD0914
AUTO_LOOT_ACTIVATE_OFFSET = 0x30
AUTO_SELF_CAST_ACTIVATE_POINTER = 0xBD0920
AUTO_SELF_CAST_ACTIVATE_OFFSET = 0x30
CHAT_BUFFER_START = 0xB75A60
NEXT_MESSAGE = 0x17C0

# =============================================================================
# --- Game Functions ---
# =============================================================================
# Lua
LUA_STATE = 0xD3F78C
LUA_DO_STRING = 0x819210
LUA_GET_LOCALIZED_TEXT = 0x7225E0
LUA_SET_TOP = 0x84DBF0
# Player/Unit Actions
CG_PLAYER_C_CLICK_TO_MOVE = 0x727400
FUNCTION_PLAYER_CLICK_TO_MOVE = CG_PLAYER_C_CLICK_TO_MOVE # Alias
FUNCTION_PLAYER_CLICK_TO_MOVE_STOP = 0x72B3A0
CG_GAME_UI_TARGET = 0x524BF0
FUNCTION_SET_TARGET = CG_GAME_UI_TARGET # Alias
SPELL_C_CAST_SPELL = 0x80DA40
HANDLE_TERRAIN_CLICK_FUNC = 0x527830
FUNCTION_HANDLE_TERRAIN_CLICK = HANDLE_TERRAIN_CLICK_FUNC # Alias
# Movement
MOVE_FORWARD_START = 0x5FC200
MOVE_FORWARD_STOP = 0x5FC250
MOVE_BACKWARD_START = 0x5FC290
MOVE_BACKWARD_STOP = 0x5FC2E0
TURN_LEFT_START = 0x5FC320
TURN_LEFT_STOP = 0x5FC360
TURN_RIGHT_START = 0x5FC3B0
TURN_RIGHT_STOP = 0x5FC3F0
JUMP_OR_ASCEND_START = 0x5FBF80
ASCEND_STOP = 0x5FC0A0
# Unit Information
CG_UNIT_C_GET_CREATURE_TYPE = 0x71F300
CG_UNIT_C_GET_CREATURE_RANK = 0x718DE0
CG_UNIT_C_GET_SHAPESHIFT_FORM_ID = 0x71AF70
CLNT_OBJ_MGR_GET_ACTIVE_PLAYER_OBJ = 0x4038F0
FUNCTION_GET_ACTIVE_PLAYER_OBJECT = CLNT_OBJ_MGR_GET_ACTIVE_PLAYER_OBJ # Alias
FUNCTION_IS_OUTDOORS = 0x71B7F0
# World & Rendering
CG_WORLD_FRAME_RENDER_WORLD = 0x4FAF90
FUNCTION_WORLD_RENDER_WORLD = CG_WORLD_FRAME_RENDER_WORLD # Alias
CG_WORLD_FRAME_INTERSECT = 0x77F310
FUNCTION_TRACELINE = 0x7A3B70
# Miscellaneous
CLNT_OBJ_MGR_OBJECT_PTR = 0x4D4DB0
CLNT_OBJ_MGR_GET_ACTIVE_PLAYER = 0x4D3790
C_INPUT_CONTROL = 0xC24954

# =============================================================================
# --- Rendering & Collision ---
# =============================================================================
# Direct3D9
P_DEVICE_PTR_1 = 0xC5DF88
P_DEVICE_PTR_2 = 0x397C
O_BEGIN_SCENE = 0xA4
O_END_SCENE = 0xA8
O_CLEAR = 0xAC
END_SCENE_OFFSET = O_END_SCENE # Alias
END_SCENE_STATIC_DEVICE = P_DEVICE_PTR_1 # Alias
END_SCENE_OFFSET_DEVICE = P_DEVICE_PTR_2 # Alias
# Collision
COLLISION_M2C = 0x7A50CF
COLLISION_M2S = 0x7A52EC
COLLISION_WMO = 0x7AE7EA
# Other
RENDER_FLAGS = 0xCD774C
M2_MODEL_IS_OUTDOORS = 0x77FBF0

# =============================================================================
# --- Miscellaneous ---
# =============================================================================
TIMESTAMP = 0xB1D618
LAST_HARDWARE_ACTION = 0xB499A4
TICK_COUNT = LAST_HARDWARE_ACTION # Alias
BUILD_NUMBER = 0xB3203C
CVAR_MAX_FPS = 0xC5DF7C
BREATH_TIMER = 0xBD0BA0
# VFTable
VFTABLE_INDEX_INTERACT = 44
VFTABLE_INDEX_GET_NAME = 54
# Party/Raid
S_LEADER_GUID = 0xBD1968
RAID_LEADER = 0xBD1990
S_MEMBER_1_GUID = 0xBD1948
S_MEMBER_2_GUID = S_MEMBER_1_GUID + 8
S_MEMBER_3_GUID = S_MEMBER_2_GUID + 8
S_MEMBER_4_GUID = S_MEMBER_3_GUID + 8
RAID_GROUP_START = 0xBEB568
# Account/Realm
CURRENT_ACCOUNT = 0xB6AA40
CURRENT_REALM = 0xC79B9E
