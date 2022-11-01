from rpg.models.game_items.game_item import GameItem
from rpg.models.game_items.game_item_types import GameItemTypes


def test_item_id_returns_5():
    test_item = GameItem(5, "Hoe", GameItemTypes.OTHER, 10)
    assert test_item.item_id == 5


def test_item_name_returns_hoe():
    test_item = GameItem(5, "Hoe", GameItemTypes.OTHER, 10)
    assert test_item.item_name == "Hoe"


def test_item_type_returns_other():
    test_item = GameItem(5, "Hoe", GameItemTypes.OTHER, 10)
    assert test_item.item_type == GameItemTypes.OTHER


def test_item_price_gequal_0_returns_10():
    test_item = GameItem(5, "Hoe", GameItemTypes.OTHER, 10)
    assert test_item.item_price == 10


def test_item_price_less_0_returns_0():
    test_item = GameItem(5, "Hoe", GameItemTypes.OTHER, -17)
    assert test_item.item_price == 0
