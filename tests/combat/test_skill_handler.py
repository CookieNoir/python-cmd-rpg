from rpg.models.entities.entity import Entity
from rpg.models.game_items.weapon import Weapon
from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.skills.damage_types import DamageTypes
import rpg.combat.skill_handler as sh


def test_apply_skill_step_log_and_targets_lengths_are_equal_if_no_reflection_returns_true():
    test_entity_caster = Entity("Barko")
    targets = [Entity("Boris"), Entity("Ben"), Entity("Bear")]
    skill_step = SkillStep(DamageTypes.PURE, True, 1.0)
    log = sh._apply_skill_step(skill_step, 1, 0, test_entity_caster, targets)
    assert len(log) == len(targets)


def test_apply_skill_step_log_length_is_greater_by_one_if_reflection_returns_true():
    test_entity_caster = Entity("Barko")
    targets = [Entity("Boris", base_damage_reflection=1), Entity("Ben"), Entity("Bear")]
    skill_step = SkillStep(DamageTypes.PURE, True, 1.0)
    log = sh._apply_skill_step(skill_step, 1, 0, test_entity_caster, targets)
    assert len(log) == (len(targets) + 1)


def test_apply_skill_step_log_contains_special_tuples_returns_true():
    test_entity_caster = Entity("Barko")
    targets = [Entity("Boris")]
    skill_step = SkillStep(DamageTypes.PURE, True, 1.0)
    log = sh._apply_skill_step(skill_step, 1, 0, test_entity_caster, targets)

    assert type(log[0]) is tuple
    assert type(log[0][0]) is Entity
    assert type(log[0][1]) is DamageTypes
    assert type(log[0][2]) is int


def test_apply_skill_step_deals_damage_returns_4():
    test_entity_caster = Entity("Barko")
    targets = [Entity("Boris", base_max_health=5)]
    skill_step = SkillStep(DamageTypes.PURE, True, 1.0)
    sh._apply_skill_step(skill_step, 1, 0, test_entity_caster, targets)
    assert targets[0].current_health == 4


def test_apply_skill_step_applies_pierce_returns_3():
    test_entity_caster = Entity("Barko")
    targets = [Entity("Boris", base_max_health=5)]
    skill_step = SkillStep(DamageTypes.PHYSICAL, True, 1.0)
    sh._apply_skill_step(skill_step, 1, 1, test_entity_caster, targets)
    assert targets[0].current_health == 3


def test_apply_skill_applies_one_skill_step_returns_1():
    test_entity_caster = Entity("Barko")
    test_target = Entity("Boris")
    test_weapon = Weapon(1, "Test weapon", base_damage=3)
    test_skill = Skill("Test skill", is_direct=True, targets=SkillTargets.ENEMIES,
                       skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 1.0)], description="Placeholder description")
    log = sh.apply_skill(test_skill, test_weapon, test_entity_caster, test_target)
    assert len(log) == 1


def test_apply_skill_applies_all_skill_steps_returns_2():
    test_entity_caster = Entity("Barko")
    test_target = Entity("Boris")
    test_weapon = Weapon(1, "Test weapon", base_damage=3)
    test_skill = Skill("Test skill", is_direct=True, targets=SkillTargets.ENEMIES,
                       skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 1.0),
                                    SkillStep(DamageTypes.MAGICAL, True, 1.0)], description="Placeholder description")
    log = sh.apply_skill(test_skill, test_weapon, test_entity_caster, test_target)
    assert len(log) == 2


def test_apply_skill_deals_damage_returns_0():
    test_entity_caster = Entity("Barko")
    test_target = Entity("Boris")
    test_weapon = Weapon(1, "Test weapon", base_damage=3)
    test_skill = Skill("Test skill", is_direct=True, targets=SkillTargets.ENEMIES,
                       skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 1.0)], description="Placeholder description")
    sh.apply_skill(test_skill, test_weapon, test_entity_caster, test_target)
    assert test_target.current_health == 0


def test_apply_skill_applies_damage_returns_0():
    test_entity_caster = Entity("Barko", base_armor_pierce=2)
    test_target = Entity("Boris", base_max_health=3)
    test_weapon = Weapon(1, "Test weapon", base_damage=1)
    test_skill = Skill("Test skill", is_direct=True, targets=SkillTargets.ENEMIES,
                       skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 1.0)], description="Placeholder description")
    sh.apply_skill(test_skill, test_weapon, test_entity_caster, test_target)
    assert test_target.current_health == 0


def test_apply_skill_affects_indirect_targets_if_skill_is_indirect_returns_0():
    test_entity_caster = Entity("Barko")
    test_direct_target = Entity("Boris", base_max_health=3)
    test_indirect_target = Entity("Painter", base_max_health=3)
    test_weapon = Weapon(1, "Test weapon", base_damage=3)
    test_skill = Skill("Test skill", is_direct=False, targets=SkillTargets.ENEMIES,
                       skill_steps=[SkillStep(DamageTypes.PHYSICAL, True, 1.0)], description="Placeholder description")
    sh.apply_skill(test_skill, test_weapon, test_entity_caster, test_direct_target, [test_indirect_target])
    assert test_indirect_target.current_health == 0


def test_apply_skill_affects_indirect_targets_if_skill_is_direct_and_does_not_affect_target_returns_0():
    test_entity_caster = Entity("Barko")
    test_direct_target = Entity("Boris", base_max_health=3)
    test_indirect_target = Entity("Painter", base_max_health=3)
    test_weapon = Weapon(1, "Test weapon", base_damage=3)
    test_skill = Skill("Test skill", is_direct=True, targets=SkillTargets.ENEMIES,
                       skill_steps=[SkillStep(DamageTypes.PHYSICAL, False, 1.0)], description="Placeholder description")
    sh.apply_skill(test_skill, test_weapon, test_entity_caster, test_direct_target, [test_indirect_target])
    assert test_indirect_target.current_health == 0
