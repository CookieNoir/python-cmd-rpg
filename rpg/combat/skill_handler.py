from rpg.models.entities.entity import Entity
from rpg.models.game_items.weapon import Weapon
from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.damage_types import DamageTypes


def apply_skill(casted_skill: Skill,
                caster_weapon: Weapon,
                caster_entity: Entity,
                direct_target: Entity or None,
                indirect_targets: list) -> list:
    total_log = []
    buffed_damage = caster_entity.buff_damage(caster_weapon.base_damage)
    caster_pierce = caster_entity.pierce()
    for step in casted_skill.skill_steps:
        if casted_skill.is_direct and step.affects_target:
            total_log += _apply_skill_step(step, buffed_damage, caster_pierce, caster_entity, [direct_target])
        else:
            total_log += _apply_skill_step(step, buffed_damage, caster_pierce, caster_entity, [indirect_targets])
    return total_log


def _apply_skill_step(caster_skill_step: SkillStep,
                      weapon_damage: int,
                      armor_pierce: int,
                      caster_entity: Entity,
                      targets: list) -> list:
    log = []  # returning value, contains tuples (from_entity, to_entity, damage_type, damage_value)
    step_damage = caster_skill_step.get_scaled_damage(weapon_damage)
    total_reflection: int = 0
    for entity_target in targets:
        damage_received, damage_reflected = entity_target.get_damaged(caster_skill_step.damage_type, step_damage,
                                                                      armor_pierce)
        log.append((entity_target, caster_skill_step.damage_type, damage_received))
        if entity_target != caster_entity:
            total_reflection += damage_reflected

    if total_reflection > 0:
        reflection_received, reflection_reflected = caster_entity.get_damaged(DamageTypes.REFLECTED,
                                                                              total_reflection, 0)
        log.append((caster_entity, DamageTypes.REFLECTED, reflection_received))
    return log
