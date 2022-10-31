from local_repository import LocalRepository
from rpg.models.game_items.game_item import GameItem
from rpg.models.game_items.equippable_item import EquippableItem
from rpg.models.game_items.weapon import Weapon


class ItemRepository(LocalRepository):
    def __init__(self):
        super().__init__()

    def get_item(self, key: int) -> GameItem or EquippableItem or Weapon:
        return super().get_item(key)
