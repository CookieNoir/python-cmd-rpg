from rpg.combat.fighter import Fighter
from rpg.combat.skill_handler import apply_skill
from rpg.repositories.item_repository import ItemRepository
from rpg.repositories.skill_repository import SkillRepository
from rpg.models.game_items.game_item_types import GameItemTypes
from rpg.models.game_items.weapon import Weapon
from rpg.combat.skill_selectors.skill_selector import SkillSelector
from rpg.drawers import fighting_drawer


def fight(allies: list, enemies: list, allies_skill_selector: SkillSelector, enemies_skill_selector: SkillSelector,
          items: ItemRepository, skills: SkillRepository) -> bool:
    def get_total_speed() -> int:
        _total_speed = 0
        for in_fighter in fighters:
            _total_speed += in_fighter.step
            return _total_speed

    def team_is_alive(controllable: bool) -> bool:
        for in_fighter in fighters:
            if in_fighter.is_ally == controllable:
                return True
        return False

    fighters = []
    fighters += [Fighter(ally_entity, True) for ally_entity in allies]
    fighters += [Fighter(enemy_entity, False) for enemy_entity in enemies]

    total_speed = get_total_speed()
    fighters_count = len(fighters)
    while team_is_alive(True) and team_is_alive(False):
        fighting_drawer.print_entities_info(allies, enemies)
        caster: Fighter = max(fighters)
        while caster.value < total_speed:
            for fighter in fighters:
                fighter.make_step()
            caster = max(fighters)

        if caster.is_ally:
            skill_selector = allies_skill_selector
        else:
            skill_selector = enemies_skill_selector
        _make_move(caster, fighters, skill_selector, items, skills)
        caster.end_turn(total_speed)
        fighters = [in_fighter for in_fighter in fighters if in_fighter.entity.is_alive()]
        if len(fighters) != fighters_count:
            total_speed = get_total_speed()
            fighters_count = len(fighters)
    return team_is_alive(True)


def _make_move(caster: Fighter, fighters: list, skill_selector: SkillSelector, items: ItemRepository,
               skills: SkillRepository):
    fighting_drawer.print_caster_makes_move(caster.entity)
    weapon_id = caster.entity.get_item_from_slot(GameItemTypes.WEAPON)
    caster_weapon: Weapon = items.get_item(weapon_id)
    possible_skill_names = caster_weapon.skills
    possible_skills = [skills.get_item(name) for name in possible_skill_names]
    casted_skill, direct_target, indirect_targets = skill_selector.select_skill_and_targets(caster, possible_skills,
                                                                                            caster_weapon, fighters)
    move_log = apply_skill(casted_skill, caster_weapon, caster.entity, direct_target, indirect_targets)
    fighting_drawer.print_log(caster.entity, casted_skill.name, move_log)
