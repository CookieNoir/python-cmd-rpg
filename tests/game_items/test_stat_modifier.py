from rpg.models.game_items.stat_types import StatTypes
from rpg.models.game_items.stat_modifier import StatModifier


def test_stat_type_returns_speed():
    stat_mod = StatModifier(StatTypes.SPEED, False, 1.2)
    assert stat_mod.stat_type == StatTypes.SPEED


def test_is_multiplier_returns_false():
    stat_mod = StatModifier(StatTypes.SPEED, False, 1.2)
    assert stat_mod.is_multiplier is False


def test_value_returns_1dot2():
    stat_mod = StatModifier(StatTypes.SPEED, False, 1.2)
    assert stat_mod.value == 1.2
