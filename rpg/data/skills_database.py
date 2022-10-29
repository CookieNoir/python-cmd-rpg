from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.damage_types import DamageTypes

all_skills = {
    "Single strike": Skill("Single strike", is_direct=True, targets=SkillTargets.ENEMIES,
                           skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 1.0), ],
                           description="Deals {} PHYSICAL damage to the target enemy."),
    "Whirlwind smash": Skill("Whirlwind smash", is_direct=True, targets=SkillTargets.ENEMIES,
                             skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 0.6),
                                          SkillStep(DamageTypes.PHYSICAL, False, 0.4), ],
                             description="Deals {} PHYSICAL damage to the target enemy "
                                         "and {} PHYSICAL damage to others."),
    "Weak healing": Skill("Weak healing", is_direct=True, targets=SkillTargets.ALLIES,
                          skill_steps=[SkillStep(DamageTypes.HEALING, True, 0.6), ],
                          description="HEALS selected ally for {} health points."),
    "Strong healing": Skill("Strong healing", is_direct=True, targets=SkillTargets.ALLIES,
                            skill_steps=[SkillStep(DamageTypes.HEALING, True, 1.3), ],
                            description="HEALS selected ally for {} health points."),
    "Bloodletting": Skill("Bloodletting", is_direct=True, targets=SkillTargets.EVERYONE,
                          skill_steps=[SkillStep(DamageTypes.PURE, True, 0.8),
                                       SkillStep(DamageTypes.HEALING, True, 1.0), ],
                          description="Deals {} PURE damage to the target ally. "
                                      "If it survives, HEALS it {} health points."),
    "50 to 50": Skill("50 to 50", is_direct=False, targets=SkillTargets.ENEMIES,
                      skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 0.5),
                                   SkillStep(DamageTypes.MAGICAL, False, 0.5), ],
                      description="Deals {} PHYSICAL damage to all enemies, "
                                  "then deals {} MAGICAL damage to them."),
    "Purification": Skill("Purification", is_direct=True, targets=SkillTargets.ENEMIES,
                          skill_steps=[SkillStep(DamageTypes.PURE, True, 0.6), ],
                          description="Deals {} PURE damage to the target enemy."),
    "Hail of arrows": Skill("Hail of arrows", is_direct=False, targets=SkillTargets.ENEMIES,
                            skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 0.4), ],
                            description="Deals {} PHYSICAL damage to all enemies."),
    "Piercing shot": Skill("Piercing shot", is_direct=True, targets=SkillTargets.ENEMIES,
                           skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 0.6),
                                        SkillStep(DamageTypes.PURE, True, 0.3), ],
                           description="Powerful shot, that deals {} PHYSICAL "
                                       "and {} PURE damage to the target enemy."),
    "Magic missile": Skill("Magic missile", is_direct=True, targets=SkillTargets.ENEMIES,
                           skill_steps=[SkillStep(DamageTypes.MAGICAL, True, 1.0), ],
                           description="Shiny missile, that deals {} MAGICAL damage to the target enemy."),
    "Almost magic missile": Skill("Almost magic missile", is_direct=False, targets=SkillTargets.EVERYONE,
                                  skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 0.6), ],
                                  description="Shiny missile, that deals {} PHYSICAL damage to everyone."),
    "Starfall": Skill("Starfall", is_direct=False, targets=SkillTargets.EVERYONE,
                      skill_steps=[SkillStep(DamageTypes.MAGICAL, True, 0.5),
                                   SkillStep(DamageTypes.PURE, True, 0.2), ],
                      description="Charming (but quite dangerous) spell, that deals {} "
                                  "MAGICAL and {} PURE damage to everyone."),
    "Pinch": Skill("Pinch", is_direct=True, targets=SkillTargets.ENEMIES,
                   skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 0.2), ],
                   description="Absolutely harmless pinch, that deals {} to the target enemy.")
}
