from math import ceil
from rpg.drawers.line_drawer import print_solid_line
from rpg.models.entities.entity import Entity
from rpg.models.skills.damage_types import DamageTypes

HEALTH_BAR_LENGTH = 10
HEALTH_FILLED = chr(ord('█'))
HEALTH_EMPTY = chr(ord('░'))


def get_health_bar(current_health: int, max_health: int) -> str:  # result example: [█████░░░░░] 17/40 HP
    if current_health > 0:
        bar = (HEALTH_FILLED * ceil(current_health / max_health * HEALTH_BAR_LENGTH)).ljust(HEALTH_BAR_LENGTH,
                                                                                            HEALTH_EMPTY)
        result = f"[{bar}] {current_health}/{max_health} HP"
    else:
        result = "DEAD"
    return result


def print_entities_info(allies: list, enemies: list):
    def print_team(team: list, team_name: str):
        for mate in team:
            print()
            print(mate.name)
            print("{:<10} {}".format(team_name, get_health_bar(mate.current_health, mate.max_health)))

    print("{:^32}".format("Fighters"))
    print_team(allies, "Ally")
    print_team(enemies, "Enemy")
    print_solid_line(32)


def print_target_names(targets: list, index_offset: int = 1):
    print("Select target:")
    print()
    for target in targets:
        print(f"{index_offset:<3} {target.name}")
        index_offset += 1


def print_skills(skills: list,
                 weapon_damage: int,
                 index_offset: int = 1):
    print("Select skill:")
    print()
    for skill in skills:
        damages = skill.get_skill_step_damages(weapon_damage)
        print(f"{index_offset:<3} {skill.name}")
        print(f"Description:    {skill.description.format(*damages)}")
        index_offset += 1


def print_caster_makes_move(caster: Entity):
    print(f"{caster.name} makes a move")


def print_log(caster: Entity, skill_name: str,
              move_log: list):  # move_log should contain tuples (Entity, DamageTypes, int)
    print("{} used the \"{}\" skill".format(caster.name, skill_name))
    output_format = None
    for target_info in move_log:
        match target_info[1]:
            case DamageTypes.PHYSICAL:
                output_format = "{0} received {1} PHYSICAL damage"
            case DamageTypes.MAGICAL:
                output_format = "{0} received {1} MAGICAL damage"
            case DamageTypes.PURE:
                output_format = "{0} received {1} PURE damage"
            case DamageTypes.HEALING:
                output_format = "{0} received {1} HEALING"
            case DamageTypes.REFLECTED:
                output_format = "{0} received {1} REFLECTED damage"
        print(output_format.format(target_info[0].name, target_info[2]))
