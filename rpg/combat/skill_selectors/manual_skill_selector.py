from rpg.combat.skill_selectors.skill_selector import SkillSelector
from rpg.combat.fighter import Fighter
from rpg.models.skills.skill import Skill
from rpg.models.game_items.weapon import Weapon
from rpg.models.entities.entity import Entity
from rpg.drawers import fighting_drawer
from rpg.input.game_input import GameInput


class ManualSkillSelector(SkillSelector):
    def __init__(self, game_input: GameInput):
        super().__init__()
        self._input = game_input

    def select_skill(self, caster: Fighter, possible_skills: list, weapon: Weapon, fighters: list) -> Skill:
        weapon_damage = caster.entity.buff_damage(weapon.base_damage)
        fighting_drawer.print_skills(possible_skills, weapon_damage, 1)
        selected_skill_index = self._input.get_int_value(1, len(possible_skills)) - 1
        selected_skill: Skill = possible_skills[selected_skill_index]
        return selected_skill

    def select_direct_target(self, indirect_targets: list) -> Entity:
        fighting_drawer.print_target_names(indirect_targets, 1)
        target_index = self._input.get_int_value(1, len(indirect_targets)) - 1
        target = indirect_targets[target_index]
        return target
