import pytest
from rpg.models.players.purse import Purse


def test_balance_default_value_returns_0():
    test_purse = Purse()
    assert test_purse.balance == 0


def test_balance_start_value_returns_5():
    test_purse = Purse(5)
    assert test_purse.balance == 5


def test_can_afford_enough_money_returns_true():
    test_purse = Purse(5)
    assert test_purse.can_afford(4) is True


def test_can_afford_not_enough_money_returns_false():
    test_purse = Purse(5)
    assert test_purse.can_afford(6) is False


def test_give_money_enough_money_returns_value():
    test_purse = Purse(5)
    assert test_purse.give_money(4) == 4


def test_give_money_not_enough_money_raises_ValueError():
    test_purse = Purse(5)
    with pytest.raises(ValueError):
        test_purse.give_money(6)


def test_earn_money_increases_balance_returns_6():
    test_purse = Purse(5)
    test_purse.earn_money(1)
    assert test_purse.balance == 6
