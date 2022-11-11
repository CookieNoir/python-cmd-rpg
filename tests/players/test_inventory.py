import pytest
from rpg.models.players.inventory import Inventory


def test_get_items_no_items_by_default_returns_empty_list():
    test_inventory = Inventory()
    assert len(test_inventory.get_items()) == 0


def test_get_items_has_start_items_returns_items_length():
    test_inventory = Inventory([4, 3, 5])
    assert len(test_inventory.get_items()) == 3


def test_get_items_in_range_lower_border_set_returns_3_5():
    test_inventory = Inventory([4, 3, 5])
    assert test_inventory.get_items(1) == [3, 5]


def test_get_items_in_range_upper_border_set_returns_3():
    test_inventory = Inventory([4, 3, 5])
    assert test_inventory.get_items(1, 2) == [3]


def test_add_item_returns_len_equals_to_4():
    test_inventory = Inventory([4, 3, 5])
    test_inventory.add_item(6)
    assert len(test_inventory.get_items()) == 4


def test_take_item_has_item_returns_item_id():
    test_inventory = Inventory([4, 3, 5])
    assert test_inventory.take_item(3) == 3


def test_take_item_no_item_raises_ValueError():
    test_inventory = Inventory([4, 3, 5])
    with pytest.raises(ValueError):
        test_inventory.take_item(6)
