from rpg.models.players.player_data import PlayerData
from rpg.models.entities.entity import Entity


def test_has_only_entities_by_default_returns_1_0_0():
    test_player = PlayerData([Entity("Tom")])
    assert len(test_player.entities) == 1
    assert len(test_player.inventory.get_items()) == 0
    assert test_player.purse.balance == 0


def test_has_start_values_returns_1_2_10():
    test_player = PlayerData([Entity("Tom")], [4, 3], 10)
    assert len(test_player.entities) == 1
    assert len(test_player.inventory.get_items()) == 2
    assert test_player.purse.balance == 10
