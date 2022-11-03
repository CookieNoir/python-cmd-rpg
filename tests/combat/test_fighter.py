from rpg.combat.fighter import Fighter
from rpg.models.entities.entity import Entity


def test_step_returns_3():
    test_entity = Entity("Tom", base_speed=3)
    test_fighter = Fighter(test_entity, True)
    assert test_fighter.step == 3


def test_value_default_returns_0():
    test_entity = Entity("Tom", base_speed=3)
    test_fighter = Fighter(test_entity, True)
    assert test_fighter.value == 0


def test_controllable_returns_true():
    test_entity = Entity("Tom", base_speed=3)
    test_fighter = Fighter(test_entity, True)
    assert test_fighter.controllable is True


def test_make_step_returns_3():
    test_entity = Entity("Tom", base_speed=3)
    test_fighter = Fighter(test_entity, True)
    test_fighter.make_step()
    assert test_fighter.value == 3


def test_end_turn_returns_1():
    test_entity = Entity("Tom", base_speed=3)
    test_fighter = Fighter(test_entity, True)
    test_fighter.make_step()
    test_fighter.end_turn(2)
    assert test_fighter.value == 1


def test_equals_returns_true():
    test_entity1 = Entity("Tom", base_speed=3)
    test_fighter1 = Fighter(test_entity1, True)
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    assert (test_fighter1 == test_fighter2) is True


def test_equals_values_differ_returns_false():
    test_entity1 = Entity("Tom", base_speed=3)
    test_fighter1 = Fighter(test_entity1, True)
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    test_fighter1.make_step()
    assert (test_fighter1 == test_fighter2) is False


def test_equals_values_are_equal_but_steps_differ_returns_false():
    test_entity1 = Entity("Tom", base_speed=2)
    test_fighter1 = Fighter(test_entity1, True)
    test_fighter1.make_step()
    test_fighter1.make_step()
    test_fighter1.make_step()
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    test_fighter2.make_step()
    test_fighter2.make_step()
    assert (test_fighter1 == test_fighter2) is False


def test_lesser_value_is_lesser_returns_true():
    test_entity1 = Entity("Tom", base_speed=3)
    test_fighter1 = Fighter(test_entity1, True)
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    test_fighter2.make_step()
    assert (test_fighter1 < test_fighter2) is True


def test_lesser_values_are_equal_but_step_is_lesser_returns_true():
    test_entity1 = Entity("Tom", base_speed=2)
    test_fighter1 = Fighter(test_entity1, True)
    test_fighter1.make_step()
    test_fighter1.make_step()
    test_fighter1.make_step()
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    test_fighter2.make_step()
    test_fighter2.make_step()
    assert (test_fighter1 < test_fighter2) is True


def test_lesser_values_and_steps_are_equal_returns_false():
    test_entity1 = Entity("Tom", base_speed=3)
    test_fighter1 = Fighter(test_entity1, True)
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    assert (test_fighter1 < test_fighter2) is False


def test_lesser_values_are_equal_but_step_is_greater_returns_false():
    test_entity1 = Entity("Tom", base_speed=3)
    test_fighter1 = Fighter(test_entity1, True)
    test_fighter1.make_step()
    test_fighter1.make_step()
    test_entity2 = Entity("Moe", base_speed=2)
    test_fighter2 = Fighter(test_entity2, False)
    test_fighter2.make_step()
    test_fighter2.make_step()
    test_fighter2.make_step()
    assert (test_fighter1 < test_fighter2) is False


def test_lesser_value_is_greater_returns_false():
    test_entity1 = Entity("Tom", base_speed=3)
    test_fighter1 = Fighter(test_entity1, True)
    test_fighter1.make_step()
    test_entity2 = Entity("Moe", base_speed=3)
    test_fighter2 = Fighter(test_entity2, False)
    assert (test_fighter1 < test_fighter2) is False
