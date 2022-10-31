from fighter import Fighter
from rpg.repositories.item_repository import ItemRepository
from rpg.repositories.skill_repository import SkillRepository
from rpg.controllers import console_input
from rpg.models.game_items.game_item_types import GameItemTypes
from rpg.models.game_items.weapon import Weapon
from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_targets import SkillTargets
from random import randrange
from skill_handler import apply_skill


def fight(allies: list, enemies: list, items: ItemRepository, skills: SkillRepository) -> bool:
    def get_total_speed() -> int:
        _total_speed = 0
        for in_fighter in fighters:
            _total_speed += in_fighter.step
            return _total_speed

    def team_is_alive(controllable: bool) -> bool:
        for in_fighter in fighters:
            if in_fighter.controllable == controllable:
                return True
        return False

    fighters = []
    fighters += [Fighter(ally_entity, True) for ally_entity in allies]
    fighters += [Fighter(enemy_entity, False) for enemy_entity in enemies]

    total_speed = get_total_speed()
    fighters_count = len(fighters)
    while team_is_alive(True) and team_is_alive(False):
        caster: Fighter = max(fighters)
        while caster.value < total_speed:
            for fighter in fighters:
                fighter.make_step()
            caster = max(fighters)

        _make_move(caster, fighters, items, skills)

        caster.end_turn(total_speed)
        fighters = [in_fighter for in_fighter in fighters if in_fighter.entity.is_alive()]
        if len(fighters) != fighters_count:
            total_speed = get_total_speed()
            fighters_count = len(fighters)
    return team_is_alive(True)


def _make_move(caster: Fighter, fighters: list, items: ItemRepository, skills: SkillRepository):
    weapon_id = caster.entity.get_item_from_slot(GameItemTypes.WEAPON)
    caster_weapon: Weapon = items.get_item(weapon_id)
    possible_skill_names = list(caster_weapon.get_skills())
    possible_skills = [skills.get_item(name) for name in possible_skill_names]
    selected_skill_index: int = -1
    if caster.controllable:
        # print all possible skills
        selected_skill_index = console_input.get_int_value(1, len(possible_skills)) - 1
    else:
        selected_skill_index = randrange(len(possible_skills))
    casted_skill: Skill = possible_skills[selected_skill_index]

    allies = [fighter.entity for fighter in fighters if fighter.controllable == caster.controllable]
    enemies = [fighter.entity for fighter in fighters if fighter.controllable != caster.controllable]
    targets = []
    match casted_skill.targets:
        case SkillTargets.ENEMIES:
            targets += enemies
        case SkillTargets.ALLIES:
            targets += allies
        case SkillTargets.EVERYONE:
            targets += allies + enemies

    target = None
    if casted_skill.is_direct:
        target_index: int = -1
        if caster.controllable:
            # show all possible targets
            target_index = console_input.get_int_value(1, len(targets)) - 1
        else:
            target_index = randrange(len(targets))
        target = targets[target_index]
        targets.remove(target)

    move_log = apply_skill(casted_skill, caster_weapon, caster.entity, target, targets)
    # caster casted skill
    # show move_log