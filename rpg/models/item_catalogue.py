from inventory_item import InventoryItem
from inventory_item_types import InventoryItemTypes as IITypes
from equippable_item import EquippableItem
from weapon import Weapon
from skill import Skill
from skill_step import SkillStep
from damage_types import DamageTypes as DTypes
from stat_modifier import StatModifier
from entity_stat_types import EntityStatTypes as ESTypes
from skill_targets import SkillTargets

all_skills = {
    "Single strike": Skill("Single strike", is_direct=True, targets=SkillTargets.ENEMIES,
                           skill_steps=[SkillStep(DTypes.PHYSICAL, True, 1.0), ],
                           description="Deals {} PHYSICAL damage to the target enemy."),
    "Whirlwind smash": Skill("Whirlwind smash", is_direct=True, targets=SkillTargets.ENEMIES,
                             skill_steps=[SkillStep(DTypes.PHYSICAL, True, 0.6),
                                          SkillStep(DTypes.PHYSICAL, False, 0.4), ],
                             description="Deals {} PHYSICAL damage to the target enemy "
                                         "and {} PHYSICAL damage to others."),
    "Weak healing": Skill("Weak healing", is_direct=True, targets=SkillTargets.ALLIES,
                          skill_steps=[SkillStep(DTypes.HEALING, True, 0.6), ],
                          description="HEALS selected ally for {} health points."),
    "Strong healing": Skill("Strong healing", is_direct=True, targets=SkillTargets.ALLIES,
                            skill_steps=[SkillStep(DTypes.HEALING, True, 1.3), ],
                            description="HEALS selected ally for {} health points."),
    "Bloodletting": Skill("Bloodletting", is_direct=True, targets=SkillTargets.EVERYONE,
                          skill_steps=[SkillStep(DTypes.PURE, True, 0.8),
                                       SkillStep(DTypes.HEALING, True, 1.0), ],
                          description="Deals {} PURE damage to the target ally. "
                                      "If it survives, HEALS it {} health points."),
    "50 to 50": Skill("50 to 50", is_direct=False, targets=SkillTargets.ENEMIES,
                      skill_steps=[SkillStep(DTypes.PHYSICAL, True, 0.5),
                                   SkillStep(DTypes.MAGICAL, False, 0.5), ],
                      description="Deals {} PHYSICAL damage to all enemies, "
                                  "then deals {} MAGICAL damage to them."),
    "Purification": Skill("Purification", is_direct=True, targets=SkillTargets.ENEMIES,
                          skill_steps=[SkillStep(DTypes.PURE, True, 0.6), ],
                          description="Deals {} PURE damage to the target enemy."),
    "Hail of arrows": Skill("Hail of arrows", is_direct=False, targets=SkillTargets.ENEMIES,
                            skill_steps=[SkillStep(DTypes.PHYSICAL, True, 0.4), ],
                            description="Deals {} PHYSICAL damage to all enemies."),
    "Piercing shot": Skill("Piercing shot", is_direct=True, targets=SkillTargets.ENEMIES,
                           skill_steps=[SkillStep(DTypes.PHYSICAL, True, 0.6),
                                        SkillStep(DTypes.PURE, True, 0.3), ],
                           description="Powerful shot, that deals {} PHYSICAL "
                                       "and {} PURE damage to the target enemy."),
    "Magic missile": Skill("Magic missile", is_direct=True, targets=SkillTargets.ENEMIES,
                           skill_steps=[SkillStep(DTypes.MAGICAL, True, 1.0), ],
                           description="Shiny missile, that deals {} MAGICAL damage to the target enemy."),
    "Almost magic missile": Skill("Almost magic missile", is_direct=False, targets=SkillTargets.EVERYONE,
                                  skill_steps=[SkillStep(DTypes.PHYSICAL, True, 0.6), ],
                                  description="Shiny missile, that deals {} PHYSICAL damage to everyone."),
    "Starfall": Skill("Starfall", is_direct=False, targets=SkillTargets.EVERYONE,
                      skill_steps=[SkillStep(DTypes.MAGICAL, True, 0.5),
                                   SkillStep(DTypes.PURE, True, 0.2), ],
                      description="Charming (but quite dangerous) spell, that deals {} "
                                  "MAGICAL and {} PURE damage to everyone."),
    "Pinch": Skill("Pinch", is_direct=True, targets=SkillTargets.ENEMIES,
                   skill_steps=[SkillStep(DTypes.PHYSICAL, True, 0.2), ],
                   description="Absolutely harmless pinch, that deals {} to the target enemy.")
}

all_items = {
    # special
    0: EquippableItem(0, "Empty", item_type=IITypes.OTHER, item_price=0),
    # weapons
    1: Weapon(1, "Rusty sword", base_damage=5, item_price=3,
              skills=["Single strike", "Whirlwind smash"],
              stat_modifiers=[StatModifier(ESTypes.ARMOR_PIERCE, False, 1),
                              StatModifier(ESTypes.SPEED, False, 1), ]),
    2: Weapon(2, "Wooden bow", base_damage=8, item_price=20,
              skills=["Hail of arrows", "Piercing shot"],
              stat_modifiers=[StatModifier(ESTypes.ARMOR_PIERCE, False, 3),
                              StatModifier(ESTypes.ARMOR_PIERCE, True, 1.5),
                              StatModifier(ESTypes.SPEED, False, 3), ]),
    3: Weapon(3, "Weak healing staff", base_damage=10, item_price=30,
              skills=["Purification", "Weak healing"],
              stat_modifiers=[StatModifier(ESTypes.MAGICAL_RESISTANCE, False, 3),
                              StatModifier(ESTypes.MAGICAL_RESISTANCE, True, 1.2)]),
    4: Weapon(4, "Strong healing staff", base_damage=30, item_price=100,
              skills=["Purification", "Pinch", "Strong healing"],
              stat_modifiers=[StatModifier(ESTypes.MAGICAL_RESISTANCE, False, 5),
                              StatModifier(ESTypes.MAGICAL_RESISTANCE, True, 1.4),
                              StatModifier(ESTypes.ARMOR_PIERCE, False, -2),
                              StatModifier(ESTypes.ARMOR_PIERCE, False, 3)]),
    5: Weapon(5, "Shaman book", base_damage=20, item_price=100,
              skills=["Bloodletting", "50 to 50", "Weak healing"],
              stat_modifiers=[StatModifier(ESTypes.PHYSICAL_RESISTANCE, False, 2),
                              StatModifier(ESTypes.MAGICAL_RESISTANCE, False, 2),
                              StatModifier(ESTypes.MAX_HEALTH, False, 10), ]),
    6: Weapon(6, "No-Way-To-Survive staff", base_damage=40, item_price=80,
              skills=["Almost magic missile", "Starfall", "Bloodletting"], ),
    # head
    21: EquippableItem(21, "Fisherman's hat", item_type=IITypes.HEAD, item_price=5,
                       stat_modifiers=[StatModifier(ESTypes.SPEED, False, 2),
                                       StatModifier(ESTypes.MAGICAL_RESISTANCE, False, 1), ]),
    22: EquippableItem(22, "Leather helmet", item_type=IITypes.HEAD, item_price=30,
                       stat_modifiers=[StatModifier(ESTypes.MAX_HEALTH, False, 5),
                                       StatModifier(ESTypes.PHYSICAL_RESISTANCE, False, 3),
                                       StatModifier(ESTypes.ARMOR_PIERCE, True, 1.1),
                                       ]),
    23: EquippableItem(23, "Spiked helmet", item_type=IITypes.HEAD, item_price=70,
                       stat_modifiers=[StatModifier(ESTypes.PHYSICAL_RESISTANCE, False, 5),
                                       StatModifier(ESTypes.ARMOR_PIERCE, False, 3),
                                       StatModifier(ESTypes.ARMOR_PIERCE, True, 1.3),
                                       StatModifier(ESTypes.DAMAGE_REFLECTION, True, 2),
                                       StatModifier(ESTypes.DAMAGE_REFLECTION, True, 1.1), ]),
    24: EquippableItem(24, "Dragonscale helmet", item_type=IITypes.HEAD, item_price=100,
                       stat_modifiers=[StatModifier(ESTypes.MAX_HEALTH, False, 20),
                                       StatModifier(ESTypes.MAX_HEALTH, True, 1.1),
                                       StatModifier(ESTypes.PHYSICAL_RESISTANCE, False, 5),
                                       StatModifier(ESTypes.PHYSICAL_RESISTANCE, True, 1.1),
                                       StatModifier(ESTypes.MAGICAL_RESISTANCE, False, 5),
                                       StatModifier(ESTypes.MAGICAL_RESISTANCE, True, 1.1), ]),
}


def get_item_by_id(item_id: int):
    return all_items[item_id]


def get_skill_by_name(skill_name: str):
    return all_skills[skill_name]
