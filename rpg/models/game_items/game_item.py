from game_item_types import GameItemTypes as IITypes


class GameItem:
    def __init__(self,
                 item_id: int,
                 item_name: str,
                 item_type: IITypes,
                 item_price: int = 0):
        self.item_id = item_id
        self.item_name = item_name
        self.item_type = item_type
        self.item_price = item_price
