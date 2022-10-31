from stat_types import StatTypes


class StatModifier:
    def __init__(self, stat_type: StatTypes, is_multiplier: bool, value: float):
        self._stat_type = stat_type
        self._is_multiplier = is_multiplier
        self._value = value

    @property
    def stat_type(self) -> StatTypes:
        return self._stat_type

    @property
    def is_multiplier(self) -> bool:
        return self._is_multiplier

    @property
    def value(self) -> float:
        return self._value
