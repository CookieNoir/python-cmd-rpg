from damage_types import DamageTypes as DTypes


class SkillStep:
    def __init__(self,
                 damage_type: DTypes,
                 affects_target: bool,
                 damage_multiplier: float):
        self.damage_type = damage_type
        self.affects_target = affects_target
        self.damage_multiplier = damage_multiplier
