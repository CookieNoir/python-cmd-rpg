from rpg.models.game_items.game_item_types import GameItemTypes
from rpg.models.game_items.equippable_item import EquippableItem
from rpg.models.game_items.weapon import Weapon
from rpg.models.game_items.stat_modifier import StatModifier
from rpg.models.game_items.stat_types import StatTypes

all_items = {
    # special
    0: EquippableItem(0, "Empty", item_type=GameItemTypes.OTHER, item_price=0),
    # weapons
    1: Weapon(1, "Rusty sword", base_damage=5, item_price=3,
              skills=["Single strike", "Whirlwind smash"],
              stat_modifiers=[StatModifier(StatTypes.ARMOR_PIERCE, False, 1),
                              StatModifier(StatTypes.SPEED, False, 1), ]),
    2: Weapon(2, "Wooden bow", base_damage=8, item_price=20,
              skills=["Hail of arrows", "Piercing shot"],
              stat_modifiers=[StatModifier(StatTypes.ARMOR_PIERCE, False, 3),
                              StatModifier(StatTypes.ARMOR_PIERCE, True, 1.5),
                              StatModifier(StatTypes.SPEED, False, 3), ]),
    3: Weapon(3, "Weak healing staff", base_damage=10, item_price=30,
              skills=["Purification", "Weak healing"],
              stat_modifiers=[StatModifier(StatTypes.MAGICAL_RESISTANCE, False, 3),
                              StatModifier(StatTypes.MAGICAL_RESISTANCE, True, 1.2)]),
    4: Weapon(4, "Strong healing staff", base_damage=30, item_price=100,
              skills=["Purification", "Pinch", "Strong healing"],
              stat_modifiers=[StatModifier(StatTypes.MAGICAL_RESISTANCE, False, 5),
                              StatModifier(StatTypes.MAGICAL_RESISTANCE, True, 1.4),
                              StatModifier(StatTypes.ARMOR_PIERCE, False, -2),
                              StatModifier(StatTypes.ARMOR_PIERCE, False, 3)]),
    5: Weapon(5, "Shaman book", base_damage=20, item_price=100,
              skills=["Bloodletting", "50 to 50", "Weak healing"],
              stat_modifiers=[StatModifier(StatTypes.PHYSICAL_RESISTANCE, False, 2),
                              StatModifier(StatTypes.MAGICAL_RESISTANCE, False, 2),
                              StatModifier(StatTypes.MAX_HEALTH, False, 10), ]),
    6: Weapon(6, "No-Way-To-Survive staff", base_damage=40, item_price=80,
              skills=["Almost magic missile", "Starfall", "Bloodletting"], ),
    # head
    21: EquippableItem(21, "Fisherman's hat", item_type=GameItemTypes.HEAD, item_price=5,
                       stat_modifiers=[StatModifier(StatTypes.SPEED, False, 2),
                                       StatModifier(StatTypes.MAGICAL_RESISTANCE, False, 1), ]),
    22: EquippableItem(22, "Leather helmet", item_type=GameItemTypes.HEAD, item_price=30,
                       stat_modifiers=[StatModifier(StatTypes.MAX_HEALTH, False, 5),
                                       StatModifier(StatTypes.PHYSICAL_RESISTANCE, False, 3),
                                       StatModifier(StatTypes.ARMOR_PIERCE, True, 1.1),
                                       ]),
    23: EquippableItem(23, "Spiked helmet", item_type=GameItemTypes.HEAD, item_price=70,
                       stat_modifiers=[StatModifier(StatTypes.PHYSICAL_RESISTANCE, False, 5),
                                       StatModifier(StatTypes.ARMOR_PIERCE, False, 3),
                                       StatModifier(StatTypes.ARMOR_PIERCE, True, 1.3),
                                       StatModifier(StatTypes.DAMAGE_REFLECTION, True, 2),
                                       StatModifier(StatTypes.DAMAGE_REFLECTION, True, 1.1), ]),
    24: EquippableItem(24, "Dragonscale helmet", item_type=GameItemTypes.HEAD, item_price=100,
                       stat_modifiers=[StatModifier(StatTypes.MAX_HEALTH, False, 20),
                                       StatModifier(StatTypes.MAX_HEALTH, True, 1.1),
                                       StatModifier(StatTypes.PHYSICAL_RESISTANCE, False, 5),
                                       StatModifier(StatTypes.PHYSICAL_RESISTANCE, True, 1.1),
                                       StatModifier(StatTypes.MAGICAL_RESISTANCE, False, 5),
                                       StatModifier(StatTypes.MAGICAL_RESISTANCE, True, 1.1), ]),
}
