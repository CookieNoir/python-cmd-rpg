from equippable_item import EquippableItem
from game_item_types import GameItemTypes as IITypes


class Weapon(EquippableItem):
    def __init__(self, item_id: int,
                 item_name: str,
                 base_damage: int = 1,
                 item_price: int = 0,
                 skills: list = None,
                 stat_modifiers: list = None):
        super().__init__(item_id, item_name, IITypes.WEAPON, item_price, stat_modifiers)
        self._base_damage = base_damage
        self._skills = skills

    @property
    def base_damage(self) -> int:
        return self._base_damage

    @property
    def skills(self) -> list:
        return self._skills
