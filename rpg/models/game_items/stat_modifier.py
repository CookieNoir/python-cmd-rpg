from stat_types import StatTypes


class StatModifier:
    def __init__(self, stat_type: StatTypes, is_multiplier: bool, value: float):
        self.stat_type = stat_type
        self.is_multiplier = is_multiplier
        self.value = value
