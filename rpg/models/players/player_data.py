from inventory import Inventory
from purse import Purse


class PlayerData:
    def __init__(self, entities: list, start_inventory: list = None, start_balance: int = 0):
        self._entities = entities.copy()
        self._inventory: Inventory = Inventory(start_inventory)
        self._purse = Purse(start_balance)

    @property
    def entities(self) -> list:
        return self._entities

    @property
    def inventory(self) -> Inventory:
        return self._inventory

    @property
    def purse(self) -> Purse:
        return self._purse
