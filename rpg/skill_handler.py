from models.entity import Entity
from models.game_items.game_item_types import GameItemTypes
from services.skill_repository import SkillRepository
from services.item_repository import ItemRepository
from models.game_items.weapon import Weapon
from models.skills.skill_step import SkillStep
from models.skills.skill_targets import SkillTargets
from models.skills.damage_types import DamageTypes


def apply_skill(skill_name: str,
                caster: Entity,
                allies: list,
                target: Entity or None,
                enemies: list) -> list:
    log = []
    weapon_id = caster.get_item_from_slot(GameItemTypes.WEAPON)
    caster_weapon: Weapon = ItemRepository.get_item_by_id(weapon_id)
    caster_pierce: int = caster.get_pierce()
    casted_skill = SkillRepository.get_skill_by_name(skill_name)
    buffed_damage = caster.get_skill_damage(caster_weapon, casted_skill)

    possible_targets = []
    match casted_skill.targets:
        case SkillTargets.ENEMIES:
            possible_targets += enemies
        case SkillTargets.ALLIES:
            possible_targets += allies
        case SkillTargets.EVERYONE:
            possible_targets += allies + enemies

    qty = len(casted_skill.skill_steps)
    total_reflection: int = 0

    def _deal_damage(in_entity_target: Entity, in_step: SkillStep, damage: int) -> int:
        damage_received, damage_reflected = in_entity_target.get_damaged(in_step.damage_type, damage,
                                                                         caster_pierce)
        log.append((caster.name, in_entity_target.name, in_step.damage_type, damage_received))
        if in_entity_target != caster:
            return damage_reflected
        else:
            return 0

    for i in range(0, qty):
        step: SkillStep = casted_skill.skill_steps[i]
        if casted_skill.is_direct:
            if step.affects_target:
                entity_target: Entity = target
                total_reflection += _deal_damage(entity_target, step, buffed_damage[i])
            else:
                for possible_target in possible_targets:
                    entity_target: Entity = possible_target
                    if entity_target != target:
                        total_reflection += _deal_damage(entity_target, step, buffed_damage[i])
        else:
            for possible_target in possible_targets:
                entity_target: Entity = possible_target
                total_reflection += _deal_damage(entity_target, step, buffed_damage[i])
        if total_reflection > 0:
            reflection_received, reflection_reflected = caster.get_damaged(DamageTypes.REFLECTED, total_reflection, 0)
            log.append((None, caster.name, DamageTypes.REFLECTED, reflection_received))
    return log
