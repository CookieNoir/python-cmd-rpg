from rpg.models.game_items.game_item import GameItem
from rpg.models.game_items.equippable_item import EquippableItem
from rpg.models.game_items.weapon import Weapon


class ItemRepository:
    _data: dict = {}

    @staticmethod
    def fill(data: dict):
        ItemRepository._data = data

    @staticmethod
    def get_item_by_id(item_id: int) -> GameItem or EquippableItem or Weapon:
        return ItemRepository._data[item_id]
