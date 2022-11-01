from rpg.models.game_items.equippable_item import EquippableItem
from rpg.models.game_items.game_item_types import GameItemTypes


class Weapon(EquippableItem):
    def __init__(self, item_id: int,
                 item_name: str,
                 base_damage: int = 1,
                 item_price: int = 0,
                 skills: list = None,
                 stat_modifiers: list = None):
        super().__init__(item_id, item_name, GameItemTypes.WEAPON, item_price, stat_modifiers)
        if base_damage < 1:
            base_damage = 1
        self._base_damage = base_damage
        if skills is None:
            skills = []
        self._skills = skills

    @property
    def base_damage(self) -> int:
        return self._base_damage

    @property
    def skills(self) -> list:
        return self._skills
