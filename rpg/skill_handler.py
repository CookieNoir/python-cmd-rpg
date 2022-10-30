from models.entity import Entity
from models.game_items.weapon import Weapon
from models.skills.skill import Skill
from models.skills.skill_step import SkillStep
from models.skills.skill_targets import SkillTargets
from models.skills.damage_types import DamageTypes


def get_possible_targets(casted_skill: Skill, allies: list, enemies: list) -> list:
    targets = []
    match casted_skill.targets:
        case SkillTargets.ENEMIES:
            targets += enemies
        case SkillTargets.ALLIES:
            targets += allies
        case SkillTargets.EVERYONE:
            targets += allies + enemies
    return targets


def split_targets(target: Entity or None, possible_targets: list) -> (Entity or None, list):
    if target is None:
        return None, possible_targets
    else:
        return target, [indirect_target for indirect_target in possible_targets if indirect_target != target]


def apply_skill(casted_skill: Skill,
                caster_weapon: Weapon,
                caster_entity: Entity,
                direct_target: Entity or None,
                indirect_targets: list) -> list:
    total_log = []
    buffed_damage = caster_entity.buff_weapon_damage(caster_weapon)
    caster_pierce = caster_entity.get_pierce()
    for i in casted_skill.skill_steps:
        step: SkillStep = i
        if casted_skill.is_direct and step.affects_target:
            total_log += apply_skill_step(step, buffed_damage, caster_pierce, caster_entity, [direct_target])
        else:
            total_log += apply_skill_step(step, buffed_damage, caster_pierce, caster_entity, [indirect_targets])
    return total_log


def apply_skill_step(caster_skill_step: SkillStep,
                     weapon_damage: int,
                     armor_pierce: int,
                     caster_entity: Entity,
                     targets: list) -> list:
    log = []  # returning value, contains tuples (from_entity, to_entity, damage_type, damage_value)
    step_damage = int(weapon_damage * caster_skill_step.damage_multiplier)
    total_reflection: int = 0
    for possible_target in targets:
        entity_target: Entity = possible_target
        damage_received, damage_reflected = entity_target.get_damaged(caster_skill_step.damage_type, step_damage,
                                                                      armor_pierce)
        log.append((caster_entity, entity_target, caster_skill_step.damage_type, damage_received))
        if entity_target != caster_entity:
            total_reflection += damage_reflected

    if total_reflection > 0:
        reflection_received, reflection_reflected = caster_entity.get_damaged(DamageTypes.REFLECTED,
                                                                              total_reflection, 0)
        log.append((caster_entity, caster_entity, DamageTypes.REFLECTED, reflection_received))
    return log
