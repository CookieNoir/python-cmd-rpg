from game_item_types import GameItemTypes


class GameItem:
    def __init__(self,
                 item_id: int,
                 item_name: str,
                 item_type: GameItemTypes,
                 item_price: int = 0):
        self._item_id = item_id
        self._item_name = item_name
        self._item_type = item_type
        self._item_price = item_price

    @property
    def item_id(self) -> int:
        return self._item_id

    @property
    def item_name(self) -> str:
        return self._item_name

    @property
    def item_type(self) -> GameItemTypes:
        return self._item_type

    @property
    def item_price(self) -> int:
        return self._item_price
