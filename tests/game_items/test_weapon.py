from rpg.models.game_items.weapon import Weapon


def test_base_damage_gequal_1_returns_15():
    test_wpn = Weapon(3, "Brick", 15, 100, ["Throw it!", "Throw it again!"], None)
    assert test_wpn.base_damage == 15


def test_base_damage_less_1_returns_15():
    test_wpn = Weapon(3, "Brick", 0, 100, ["Throw it!", "Throw it again!"], None)
    assert test_wpn.base_damage == 1


def test_skills_set_returns_skill_names():
    test_wpn = Weapon(3, "Brick", 15, 1, ["Throw it!", "Throw it again!"], None)
    assert test_wpn.skills == ["Throw it!", "Throw it again!"]


def test_skills_none_returns_empty_list():
    test_wpn = Weapon(3, "Brick", 15, 1)
    assert test_wpn.skills == []
