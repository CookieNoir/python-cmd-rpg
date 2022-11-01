from rpg.models.entities.entity import Entity
from rpg.models.skills.damage_types import DamageTypes
from rpg.models.game_items.stat_modifier import StatModifier
from rpg.models.game_items.stat_types import StatTypes
from rpg.models.game_items.game_item_types import GameItemTypes
from rpg.models.game_items.equippable_item import EquippableItem


def test_name_returns_mark1():
    test_entity = Entity("Mark-1")
    assert test_entity.name == "Mark-1"


def test_max_health_gequal_1_returns_40():
    test_entity = Entity("Mark-1", base_max_health=40)
    assert test_entity.max_health == 40


def test_max_health_less_1_returns_1():
    test_entity = Entity("Mark-1", base_max_health=0)
    assert test_entity.max_health == 1


def test_speed_gequal_1_returns_5():
    test_entity = Entity("Mark-1", base_max_health=40, base_speed=5)
    assert test_entity.speed == 5


def test_speed_less_1_returns_1():
    test_entity = Entity("Mark-1", base_max_health=40, base_speed=0)
    assert test_entity.speed == 1


def test_current_health_equals_to_max_health_on_init_returns_40():
    test_entity = Entity("Mark-1", base_max_health=40)
    assert test_entity.current_health == test_entity.max_health


def test_equip_item_other_type_returns_0():
    test_entity = Entity("Mark-1")
    test_item = EquippableItem(4, "Apple", GameItemTypes.OTHER, 10)
    assert test_entity.equip_item(test_item) == 0


def test_equip_item_in_slot_body_returns_0():
    test_entity = Entity("Mark-1", base_max_health=40)
    test_item = EquippableItem(4, "Apple", GameItemTypes.BODY, 10, [StatModifier(StatTypes.MAX_HEALTH, False, 10)])
    assert test_entity.equip_item(test_item) == 0


def test_get_item_from_slot_other_returns_0():
    test_entity = Entity("Mark-1")
    assert test_entity.get_item_from_slot(GameItemTypes.OTHER) == 0


def test_get_item_from_slot_equippable_slots_default_returns_0_0_0_0():
    test_entity = Entity("Mark-1", base_max_health=40)
    assert test_entity.get_item_from_slot(GameItemTypes.WEAPON) == 0
    assert test_entity.get_item_from_slot(GameItemTypes.HEAD) == 0
    assert test_entity.get_item_from_slot(GameItemTypes.BODY) == 0
    assert test_entity.get_item_from_slot(GameItemTypes.LEGS) == 0


def test_get_item_from_slot_body_if_equipped_returns_4():
    test_entity = Entity("Mark-1", base_max_health=40)
    test_item = EquippableItem(4, "Apple", GameItemTypes.BODY, 10, [StatModifier(StatTypes.MAX_HEALTH, False, 10)])
    test_entity.equip_item(test_item)
    assert test_entity.get_item_from_slot(GameItemTypes.BODY) == 4


def test_equip_item_in_slot_body_twice_returns_4_4_50():
    test_entity = Entity("Mark-1", base_max_health=40)
    test_item1 = EquippableItem(4, "Apple", GameItemTypes.BODY, 10, [StatModifier(StatTypes.MAX_HEALTH, False, 10)])
    test_entity.equip_item(test_item1)
    test_item2 = EquippableItem(4, "Corn", GameItemTypes.BODY, 50)
    assert test_entity.equip_item(test_item2) == 4
    assert test_entity.get_item_from_slot(GameItemTypes.BODY) == 4
    assert test_entity.max_health == 50


def test_equip_item_in_slot_replace_item_returns_4_3_40():
    test_entity = Entity("Mark-1", base_max_health=40)
    test_item1 = EquippableItem(4, "Apple", GameItemTypes.BODY, 10, [StatModifier(StatTypes.MAX_HEALTH, False, 10)])
    test_entity.equip_item(test_item1)
    test_item2 = EquippableItem(3, "Corn", GameItemTypes.BODY, 50)
    assert test_entity.equip_item(test_item2) == 4
    assert test_entity.get_item_from_slot(GameItemTypes.BODY) == 3
    assert test_entity.max_health == 40


def test_remove_item_item_not_found_returns_0():
    test_entity = Entity("Mark-1", base_max_health=40)
    test_item = EquippableItem(4, "Apple", GameItemTypes.BODY, 10, [StatModifier(StatTypes.MAX_HEALTH, False, 10)])
    assert test_entity.remove_item(test_item.item_id) == 0


def test_remove_item_item_found_returns_4_40():
    test_entity = Entity("Mark-1", base_max_health=40)
    test_item = EquippableItem(4, "Apple", GameItemTypes.BODY, 10, [StatModifier(StatTypes.MAX_HEALTH, False, 10)])
    test_entity.equip_item(test_item)
    assert test_entity.remove_item(test_item.item_id) == 4
    assert test_entity.max_health == 40


def test_buff_damage_returns_5():
    test_entity = Entity("Mark-1", base_damage=4)
    assert test_entity.buff_damage(1) == 5


def test_pierce_returns_10():
    test_entity = Entity("Mark-1", base_armor_pierce=4)
    assert test_entity.pierce == 4


def test_get_damaged_physical_no_reflection_no_pierce_no_armor_returns_5_0_5():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=0, base_damage_reflection=0)
    assert test_entity.get_damaged(DamageTypes.PHYSICAL, 5) == (5, 0)
    assert test_entity.current_health == 5


def test_get_damaged_physical_no_reflection_no_pierce_returns_3_0_7():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_damage_reflection=0)
    assert test_entity.get_damaged(DamageTypes.PHYSICAL, 5) == (3, 0)
    assert test_entity.current_health == 7


def test_get_damaged_physical_pierce_reflection_returns_4_2_6():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.PHYSICAL, 5, 1) == (4, 2)
    assert test_entity.current_health == 6


def test_get_damaged_physical_huge_armor_returns_1_2_9():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=20, base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.PHYSICAL, 5, 1) == (1, 2)
    assert test_entity.current_health == 9


def test_get_damaged_physical_huge_pierce_returns_9_2_1():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.PHYSICAL, 5, 6) == (9, 2)
    assert test_entity.current_health == 1


def test_get_damaged_physical_huge_damage_returns_15_2_0():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.PHYSICAL, 15, 2) == (15, 2)
    assert test_entity.current_health == 0


def test_get_damaged_magical_returns_1_2_9():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.MAGICAL, 5) == (1, 2)
    assert test_entity.current_health == 9


def test_get_damaged_pure_returns_5_2_5():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.PURE, 5, 4) == (5, 2)
    assert test_entity.current_health == 5


def test_get_damaged_healing_hp_is_full_returns_4_0_10():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.HEALING, 4) == (4, 0)
    assert test_entity.current_health == 10


def test_get_damaged_healing_hp_is_0_returns_0_0_0():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    test_entity.get_damaged(DamageTypes.PURE, 16)
    assert test_entity.get_damaged(DamageTypes.HEALING, 4) == (0, 0)
    assert test_entity.current_health == 0


def test_get_damaged_healing_inside_range_returns_4_0_8():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    test_entity.get_damaged(DamageTypes.PURE, 6)
    assert test_entity.get_damaged(DamageTypes.HEALING, 4) == (4, 0)
    assert test_entity.current_health == 8


def test_get_damaged_healing_overhealed_returns_4_0_10():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    test_entity.get_damaged(DamageTypes.PURE, 3)
    assert test_entity.get_damaged(DamageTypes.HEALING, 4) == (4, 0)
    assert test_entity.current_health == 10


def test_get_damaged_reflected_returns_5_0_5():
    test_entity = Entity("Mark-1", base_max_health=10, base_physical_armor=2, base_magical_armor=4,
                         base_damage_reflection=2)
    assert test_entity.get_damaged(DamageTypes.REFLECTED, 5, 4) == (5, 0)
    assert test_entity.current_health == 5
