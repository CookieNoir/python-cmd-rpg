from rpg.models.game_items.equippable_item import EquippableItem
from rpg.models.game_items.stat_modifier import StatModifier
from rpg.models.game_items.game_item_types import GameItemTypes
from rpg.models.game_items.stat_types import StatTypes


def test_stat_modifiers_set_returns_1():
    test_item = EquippableItem(7, "Boot", GameItemTypes.LEGS, 40, [StatModifier(StatTypes.SPEED, False, 20)])
    assert len(test_item.stat_modifiers) == 1


def test_stat_modifiers_none_returns_0():
    test_item = EquippableItem(7, "Boot", GameItemTypes.LEGS, 40)
    assert len(test_item.stat_modifiers) == 0
