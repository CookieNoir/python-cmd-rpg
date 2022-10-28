from inventory_item import InventoryItem
from inventory_item_types import InventoryItemTypes as IITypes


class EquippableItem(InventoryItem):
    def __init__(self, item_id: int,
                 item_name: str,
                 item_type: IITypes,
                 item_price: int = 0,
                 stat_modifiers: list = None):
        super().__init__(item_id, item_name, item_type, item_price)
        self.stat_modifiers = stat_modifiers
