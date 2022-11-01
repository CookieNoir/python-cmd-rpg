from rpg.models.game_items.game_item import GameItem
from rpg.models.game_items.game_item_types import GameItemTypes


class EquippableItem(GameItem):
    def __init__(self, item_id: int,
                 item_name: str,
                 item_type: GameItemTypes,
                 item_price: int = 0,
                 stat_modifiers: list = None):
        super().__init__(item_id, item_name, item_type, item_price)
        if stat_modifiers is None:
            stat_modifiers = []
        self._stat_modifiers = stat_modifiers

    @property
    def stat_modifiers(self):
        return self._stat_modifiers
