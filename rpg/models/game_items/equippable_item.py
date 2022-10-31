from game_item import GameItem
from game_item_types import GameItemTypes as IITypes


class EquippableItem(GameItem):
    def __init__(self, item_id: int,
                 item_name: str,
                 item_type: IITypes,
                 item_price: int = 0,
                 stat_modifiers: list = None):
        super().__init__(item_id, item_name, item_type, item_price)
        self._stat_modifiers = stat_modifiers

    @property
    def stat_modifiers(self):
        return self._stat_modifiers
