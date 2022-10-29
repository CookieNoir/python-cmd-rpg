from skill_targets import SkillTargets


class Skill:
    def __init__(self,
                 name: str,
                 is_direct: bool,
                 targets: SkillTargets,
                 skill_steps: list,
                 description: str):
        self.name = name
        self.targets = targets
        self.is_direct = is_direct
        self.skill_steps = skill_steps
        self.description = description
