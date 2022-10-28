from equippable_item import EquippableItem
from inventory_item_types import InventoryItemTypes as IITypes


class Weapon(EquippableItem):
    def __init__(self, item_id: int,
                 item_name: str,
                 base_damage: int = 1,
                 item_price: int = 0,
                 skills: list = None,
                 stat_modifiers: list = None):
        super().__init__(item_id, item_name, IITypes.WEAPON, item_price, stat_modifiers)
        self.base_damage = base_damage
        self.skills = skills
