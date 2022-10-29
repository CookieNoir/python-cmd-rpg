from entity_stat_types import EntityStatTypes as ESTypes


class StatModifier:
    def __init__(self, stat_type: ESTypes, is_multiplier: bool, value: float):
        self.stat_type = stat_type
        self.is_multiplier = is_multiplier
        self.value = value
