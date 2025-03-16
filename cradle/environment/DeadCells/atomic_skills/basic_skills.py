from cradle.config import Config
from cradle.log import Logger
from cradle.gameio.io_env import IOEnvironment
from cradle.environment.DeadCells.skill_registry import register_skill
import time

config = Config()
logger = Logger()
io_env = IOEnvironment()

# --- 基础移动动作 ---

@register_skill("move_left")
def move_left(duration):
    """
    Moves the in-game character left for the specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should move left.
    """
    io_env.key_hold('a', duration)

@register_skill("move_right")
def move_right(duration):
    """
    Moves the in-game character right for the specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should move right.
    """
    io_env.key_hold('d', duration)

@register_skill("jump")
def jump(times=1):
    """
    Makes the in-game character jump one or more times.

    Parameters:
    - times: The number of times the character jumps (1 for single jump, 2 for double jump).
    """
    for _ in range(min(times, 2)):  # Maximum 2 jumps in Dead Cells
        io_env.key_press('w')
        time.sleep(0.1)  # Small delay between jumps

@register_skill("crouch")
def crouch(duration):
    """
    Makes the in-game character crouch for the specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should crouch.
    """
    io_env.key_hold('s', duration)

@register_skill("roll")
def roll(direction=None):
    """
    Makes the in-game character roll in a specified direction.
    
    Parameters:
    - direction: Optional direction ('left', 'right', None). If None, rolls in current facing direction.
    """
    if direction == 'left':
        io_env.key_hold('a', 0.1)
    elif direction == 'right':
        io_env.key_hold('d', 0.1)
    
    io_env.key_press('ctrl')

@register_skill("ground_slam")
def ground_slam():
    """
    Performs a ground slam attack while in air (down+attack).
    """
    io_env.key_hold('s', 0.1)
    io_env.key_press('j')  

@register_skill("jumpDown")
def jumpDown():
    """
    Makes the in-game character jump off the platform.
    """
    io_env.key_hold('s', 0.05)
    io_env.key_press('space')  # Changed from 'space' to 'w' to match other controls

@register_skill("wall_jump")
def wall_jump(direction):
    """
    Performs a wall jump in the specified direction.
    
    Parameters:
    - direction: The direction to jump ('left' or 'right').
    """
    opposite = 'd' if direction == 'left' else 'a'
    io_env.key_hold(opposite, 0.2)  # Hold against wall briefly
    io_env.key_press('w')
    
    # Jump away from wall
    jump_key = 'a' if direction == 'left' else 'd'
    io_env.key_hold(jump_key, 0.1)

@register_skill("climb_ladder_up")
def climb_ladder_up(duration):
    """
    Moves the in-game character up a ladder for a specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should climb up.
    """
    io_env.key_hold('w', duration)

@register_skill("climb_ladder_down")
def climb_ladder_down(duration):
    """
    Moves the in-game character down a ladder for a specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should climb down.
    """
    io_env.key_hold('s', duration)

# --- 战斗系统动作 ---

@register_skill("weapon1")
def weapon1(combo_count=1):
    """
    Makes the in-game character use weapon 1 with optional combo. (This action can attack the enemy and break the door)

    Parameters:
    - combo_count: Number of consecutive attacks (for combo).
    """
    for _ in range(combo_count):
        io_env.key_press('j')
        time.sleep(0.15)  # Slight delay between combo hits

@register_skill("weapon2")
def weapon2(combo_count=1):
    """
    Makes the in-game character use weapon 2 with optional combo. (This action can attack the enemy and break the door)

    Parameters:
    - combo_count: Number of consecutive attacks (for combo).
    """
    for _ in range(combo_count):
        io_env.key_press('k')
        time.sleep(0.15)  # Slight delay between combo hits

@register_skill("skill1")
def skill1():
    """
    Makes the in-game character use skill 1. (This action can attack the enemy and break the door)
    """
    io_env.key_press('q')

@register_skill("skill2")
def skill2():
    """
    Makes the in-game character use skill 2. (This action can attack the enemy and break the door)
    """
    io_env.key_press('e')


@register_skill("air_attack")
def air_attack():
    """
    Performs an attack while in the air.
    """
    io_env.key_press('w')  # Jump
    time.sleep(0.2)  # Wait to reach apex
    io_env.key_press('j')  # Attack

# --- 环境交互动作 ---

@register_skill("interact")
def interact():
    """
    Interacts with objects, NPCs, doors, etc.
    """
    io_env.key_press('r')  # Assuming 'r' is the interact key

@register_skill("teleport")
def teleport():
    """
    Interacts with teleporters.
    """
    io_env.key_press('f')  # Same as interact, context dependent
    time.sleep(0.5)  # Wait for teleport menu
    io_env.key_press('f')  # Confirm teleport

@register_skill("collect")
def collect():
    """
    Makes the in-game character pick up items or open the door. (Espacially when there is a prompt to press 'r')
    """
    io_env.key_press('r')

# --- 资源管理动作 ---

@register_skill("health")
def health():
    """
    Makes the in-game character drink health potion.
    """
    io_env.key_hold('h', 0.2)  # Reduced hold time, doesn't need full 1 second

@register_skill("switch_item")
def switch_item(slot):
    """
    Switches to a different item loadout.
    
    Parameters:
    - slot: The loadout slot to switch to (1-3)
    """
    if slot == 1:
        io_env.key_press('1')
    elif slot == 2:
        io_env.key_press('2')
    elif slot == 3:
        io_env.key_press('3')
    
# --- 组合动作 ---

@register_skill("dodge_and_attack")
def dodge_and_attack(direction=None):
    """
    Performs a roll followed immediately by an attack.
    
    Parameters:
    - direction: Optional direction for the roll ('left', 'right', None)
    """
    roll(direction)
    time.sleep(0.2)  # Wait for roll to complete
    weapon1()

@register_skill("jump_attack_combo")
def jump_attack_combo():
    """
    Performs a jump followed by an aerial attack and ground slam.
    """
    jump()
    time.sleep(0.2)  # Wait to reach apex
    weapon1()  # Air attack
    time.sleep(0.1)
    ground_slam()  # Follow with ground slam

__all__ = [
    "move_left",
    "move_right",
    "jump",
    "crouch",
    "roll",
    "jumpDown",
    "wall_jump",
    "climb_ladder_up",
    "climb_ladder_down",
    "weapon1",
    "weapon2",
    "skill1",
    "skill2",
    "ground_slam",
    "air_attack",
    "interact",
    "teleport",
    "collect",
    "health",
    "switch_item",
    "dodge_and_attack",
    "jump_attack_combo"
]