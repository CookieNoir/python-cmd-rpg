from math import floor


class EntityStat:
    def __init__(self, base_addition: int = 0, base_multiplier: float = 1.0):
        self.base_addition = base_addition
        self.base_multiplier = base_multiplier
        self.addition_modifiers = {}
        self.multiplier_modifiers = {}
        self._recalculate_stat()

    def add_modifier(self, item_id: int, is_multiplier: bool, value: float):
        if is_multiplier:
            self.multiplier_modifiers[item_id] = value
            self._recalculate_multiplier()
        else:
            self.addition_modifiers[item_id] = int(value)
            self._recalculate_addition()

    def remove_modifier(self, item_id: int):
        self.addition_modifiers.pop(item_id)
        self.multiplier_modifiers.pop(item_id)
        self._recalculate_stat()

    def _recalculate_addition(self):
        total_addition = self.base_addition + sum(self.addition_modifiers.values())
        self.addition = total_addition

    def _recalculate_multiplier(self):
        total_multiplier = self.base_multiplier
        for i in self.multiplier_modifiers:
            total_multiplier *= self.multiplier_modifiers[i]
        self.multiplier = total_multiplier

    def _recalculate_stat(self):
        self._recalculate_addition()
        self._recalculate_multiplier()

    def get_linear_value(self) -> int:
        return int(self.addition * self.multiplier)

    def get_incoming_damage(self, damage: int, pierce: int) -> int:
        resisted = self.get_linear_value() - pierce
        return max(damage - resisted, 1)

    def get_damage_reflection(self, damage: int) -> int:
        return self.addition + floor(damage * (1.0 - 1.0/self.multiplier))
