from rpg.models.skills.damage_types import DamageTypes
from math import ceil


class SkillStep:
    def __init__(self,
                 damage_type: DamageTypes,
                 affects_target: bool,
                 damage_multiplier: float):
        self._damage_type = damage_type
        self._affects_target = affects_target
        self._damage_multiplier = damage_multiplier

    @property
    def damage_type(self) -> DamageTypes:
        return self._damage_type

    @property
    def affects_target(self) -> bool:
        return self._affects_target

    @property
    def damage_multiplier(self) -> float:
        return self._damage_multiplier

    def get_scaled_damage(self, weapon_damage: int) -> int:
        return ceil(weapon_damage * self._damage_multiplier)
