from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.skills.damage_types import DamageTypes


def test_name_returns_test_skill():
    test_skill = Skill("test skill", True, SkillTargets.ENEMIES,
                       [SkillStep(DamageTypes.PURE, False, 0.8), SkillStep(DamageTypes.HEALING, True, 1.0), ],
                       "test description")
    assert test_skill.name == "test skill"


def test_is_direct_returns_true():
    test_skill = Skill("test skill", True, SkillTargets.ENEMIES,
                       [SkillStep(DamageTypes.PURE, False, 0.8), SkillStep(DamageTypes.HEALING, True, 1.0), ],
                       "test description")
    assert test_skill.is_direct == True


def test_targets_returns_enemies():
    test_skill = Skill("test skill", True, SkillTargets.ENEMIES,
                       [SkillStep(DamageTypes.PURE, False, 0.8), SkillStep(DamageTypes.HEALING, True, 1.0), ],
                       "test description")
    assert test_skill.targets == SkillTargets.ENEMIES


def test_skill_steps_returns_2():
    test_skill = Skill("test skill", True, SkillTargets.ENEMIES,
                       [SkillStep(DamageTypes.PURE, False, 0.8), SkillStep(DamageTypes.HEALING, True, 1.0), ],
                       "test description")
    assert len(test_skill.skill_steps) == 2


def test_description_returns_test_description():
    test_skill = Skill("test skill", True, SkillTargets.ENEMIES,
                       [SkillStep(DamageTypes.PURE, False, 0.8), SkillStep(DamageTypes.HEALING, True, 1.0), ],
                       "test description")
    assert test_skill.description == "test description"


def test_get_skill_step_damages_returns_44():
    test_skill = Skill("test skill", True, SkillTargets.ENEMIES,
                       [SkillStep(DamageTypes.PURE, False, 0.8), SkillStep(DamageTypes.HEALING, True, 1.0), ],
                       "test description")
    weapon_damage = 4
    assert test_skill.get_skill_step_damages(weapon_damage) == [4, 4]
