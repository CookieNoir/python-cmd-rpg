from rpg.combat.fighter import Fighter
from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.game_items.weapon import Weapon
from rpg.models.entities.entity import Entity


class SkillSelector:
    def __init__(self):
        pass

    def select_skill_and_targets(self, caster: Fighter, possible_skills: list, weapon: Weapon, fighters: list) -> (
            Skill, Entity or None, list):
        selected_skill = self.select_skill(caster, possible_skills, weapon, fighters)
        indirect_targets = self._get_possible_targets(fighters, selected_skill.targets, caster.is_ally)
        direct_target = None
        if selected_skill.is_direct:
            direct_target = self.select_direct_target(indirect_targets)
            indirect_targets.remove(direct_target)
        return selected_skill, direct_target, indirect_targets

    @staticmethod
    def _get_possible_targets(fighters: list, skill_targets: SkillTargets, is_ally: bool) -> list:
        targets = None
        match skill_targets:
            case SkillTargets.ENEMIES:
                targets = [fighter.entity for fighter in fighters if fighter.is_ally != is_ally]
            case SkillTargets.ALLIES:
                targets = [fighter.entity for fighter in fighters if fighter.is_ally == is_ally]
            case SkillTargets.EVERYONE:
                targets = [fighter.entity for fighter in fighters]
        return targets

    def select_skill(self, caster: Fighter, possible_skills: list, weapon: Weapon, fighters: list) -> Skill:
        pass

    def select_direct_target(self, indirect_targets: list) -> Entity:
        pass
