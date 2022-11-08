from rpg.combat.skill_selectors.skill_selector import SkillSelector
from rpg.combat.fighter import Fighter
from rpg.models.skills.skill import Skill
from rpg.models.game_items.weapon import Weapon
from rpg.models.entities.entity import Entity
from random import randrange


class AutomaticSkillSelector(SkillSelector):
    def __init__(self):
        super().__init__()

    def select_skill(self, caster: Fighter, possible_skills: list, weapon: Weapon, fighters: list) -> Skill:
        selected_skill_index = randrange(len(possible_skills))
        selected_skill: Skill = possible_skills[selected_skill_index]
        return selected_skill

    def select_direct_target(self, indirect_targets: list) -> Entity:
        target_index = randrange(len(indirect_targets))
        target = indirect_targets[target_index]
        return target
