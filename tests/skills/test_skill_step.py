from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.damage_types import DamageTypes


def test_damage_type_returns_magical():
    step = SkillStep(DamageTypes.MAGICAL, False, 1.5)
    assert step.damage_type == DamageTypes.MAGICAL


def test_affects_target_returns_false():
    step = SkillStep(DamageTypes.MAGICAL, False, 1.5)
    assert step.affects_target is False


def test_damage_multiplier_returns_1dot5():
    step = SkillStep(DamageTypes.MAGICAL, False, 1.5)
    assert step.damage_multiplier == 1.5


def test_get_scaled_damage_returns_5():
    weapon_damage = 3
    step = SkillStep(DamageTypes.MAGICAL, False, 1.5)
    assert step.get_scaled_damage(weapon_damage) == 5
