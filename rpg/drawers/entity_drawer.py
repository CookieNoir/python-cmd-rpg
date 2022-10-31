from math import ceil
from rpg.models.entities.entity import Entity

HEALTH_BAR_LENGTH = 10


def get_health_bar(current_health: int, max_health: int) -> str:  # result example: [█████░░░░░] 17/40 HP
    bar = (chr(9608) * ceil(current_health / max_health * HEALTH_BAR_LENGTH)).ljust(HEALTH_BAR_LENGTH, chr(9617))
    return f"[{bar}] {current_health}/{max_health} HP"


def print_entities_health(allies: list, enemies: list):
    pass
