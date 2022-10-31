from skill_targets import SkillTargets


class Skill:
    def __init__(self,
                 name: str,
                 is_direct: bool,
                 targets: SkillTargets,
                 skill_steps: list,
                 description: str):
        self._name = name
        self._is_direct = is_direct
        self._targets = targets
        self._skill_steps = skill_steps
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_direct(self) -> bool:
        return self._is_direct

    @property
    def targets(self) -> SkillTargets:
        return self._targets

    @property
    def skill_steps(self) -> list:
        return self._skill_steps

    @property
    def description(self) -> str:
        return self._description

    def get_skill_step_damages(self,
                               weapon_damage: int) -> list:
        result = []
        for step in self.skill_steps:
            result.append(step.get_scaled_damage(weapon_damage))
        return result
