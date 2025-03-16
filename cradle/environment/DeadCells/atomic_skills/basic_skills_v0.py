from cradle.config import Config
from cradle.log import Logger
from cradle.gameio.io_env import IOEnvironment
from cradle.environment.DeadCells.skill_registry import register_skill
import time

config = Config()
logger = Logger()
io_env = IOEnvironment()


@register_skill("move_left")
def move_left(duration):
    """
    Moves the in-game character left for the specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should move forward.
    """
    io_env.key_hold('a', duration)

@register_skill("move_right")
def move_right(duration):
    """
    Moves the in-game character right for the specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should move forward.
    """
    io_env.key_hold('d', duration)

@register_skill("jump")
def jump(time):
    """
    Moves the in-game character jump up for the specified duration.

    Parameters:
    - time: The number of times the character jumps up (1 or 2 jumps).
    """
    for _ in range(time):
        io_env.key_press('w')

@register_skill("crouch")
def crouch(duration):
    """
    Moves the in-game character crouch for the specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should crouch.
    """
    io_env.key_hold('s', duration)

@register_skill("roll")
def roll():
    """
    Moves the in-game character roll forward.
    """
    io_env.key_press('ctrl')

@register_skill("jumpDown")
def jumpDown():
    """
    Moves the in-game character jump off the the platform. 
    """
    io_env.key_hold('s',0.05)
    io_env.key_hold('space',0.05)
    io_env.key_hold('space',0.05)

@register_skill("climb_ladder_up")
def climb_ladder_up(duration):
    """
    Move the in-game character up a ladder for a specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should move forward.
    """
    io_env.key_hold('w', duration)

@register_skill("climb_ladder_down")
def climb_ladder_down(duration):
    """
    Move the in-game character down a ladder for a specified duration.

    Parameters:
    - duration: The duration in seconds for which the character should move forward.
    """
    io_env.key_hold('s', duration)

@register_skill("weapon1")
def weapon1():
    """
    Make the in-game character use weapons 1.
    """
    io_env.key_press('j')

@register_skill("weapon2")
def weapon2():
    """
    Make the in-game character use weapons 2.
    """
    io_env.key_press('k')

@register_skill("game_prop1")
def game_prop1():
    """
    Make the in-game character use game prop 1.
    """
    io_env.key_press('q')

@register_skill("game_prop2")
def game_prop2():
    """
    Make the in-game character use game prop 2.
    """
    io_env.key_press('e')

@register_skill("health")
def health():
    """
    Make the in-game character drink health potion.
    """
    io_env.key_hold('h', 1)

@register_skill("collect")
def collect():
    """
    Make the in-game character pick up items.
    """
    io_env.key_press('r')

__all__ = [
    # move
    "move_left",
    "move_right",
    "jump",
    "crouch",
    "roll",
    "jumpDown",
    "climb_ladder_up",
    "climb_ladder_down",
    # combat
    "weapon1",
    "weapon2",
    "game_prop1",
    "game_prop2",
    # other
    "health",
    "collect"
]