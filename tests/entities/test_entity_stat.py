from rpg.models.entities.entity_stat import EntityStat


def test_get_total_value_returns_5():
    stat = EntityStat(3, 1.5)
    assert stat.get_total_value() == 5


def test_add_modifier_multiplier_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, True, 2.0)
    assert stat.get_total_value() == 9


def test_add_modifier_multiplier_same_id_twice_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, True, 2.0)
    stat.add_modifier(10, True, 2.0)
    assert stat.get_total_value() == 9


def test_add_modifier_multiplier_same_id_lower_value_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, True, 2.0)
    stat.add_modifier(10, True, 1.0)
    assert stat.get_total_value() == 9


def test_add_modifier_multiplier_same_id_higher_value_returns_18():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, True, 2.0)
    stat.add_modifier(10, True, 4.0)
    assert stat.get_total_value() == 18


def test_add_modifier_multiplier_different_ids_returns_18():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, True, 2.0)
    stat.add_modifier(12, True, 2.0)
    assert stat.get_total_value() == 18


def test_add_modifier_addition_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, False, 3)
    assert stat.get_total_value() == 9


def test_add_modifier_addition_same_id_twice_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, False, 3)
    stat.add_modifier(10, False, 3)
    assert stat.get_total_value() == 9


def test_add_modifier_addition_same_id_lower_value_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, False, 3)
    stat.add_modifier(10, False, 2)
    assert stat.get_total_value() == 9


def test_add_modifier_addition_same_id_higher_value_returns_9():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, False, 3)
    stat.add_modifier(10, False, 5)
    assert stat.get_total_value() == 12


def test_remove_modifier_returns_5():
    stat = EntityStat(3, 1.5)
    stat.add_modifier(10, True, 3)
    stat.add_modifier(10, False, 5)
    stat.remove_modifier(10)
    assert stat.get_total_value() == 5
