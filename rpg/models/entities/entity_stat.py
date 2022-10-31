class EntityStat:
    def __init__(self, base_addition: int = 0, base_multiplier: float = 1.0):
        self._base_addition = base_addition
        self._base_multiplier = base_multiplier
        self._addition_modifiers = {}
        self._multiplier_modifiers = {}
        self._recalculate_stat()

    def add_modifier(self, item_id: int, is_multiplier: bool, value: float):
        if is_multiplier:
            self._multiplier_modifiers[item_id] = value
            self._recalculate_multiplier()
        else:
            self._addition_modifiers[item_id] = int(value)
            self._recalculate_addition()

    def remove_modifier(self, item_id: int):
        self._addition_modifiers.pop(item_id)
        self._multiplier_modifiers.pop(item_id)
        self._recalculate_stat()

    def _recalculate_addition(self):
        total_addition = self._base_addition + sum(self._addition_modifiers.values())
        self.addition = total_addition

    def _recalculate_multiplier(self):
        total_multiplier = self._base_multiplier
        for i in self._multiplier_modifiers:
            total_multiplier *= self._multiplier_modifiers[i]
        self.multiplier = total_multiplier

    def _recalculate_stat(self):
        self._recalculate_addition()
        self._recalculate_multiplier()

    def get_total_value(self) -> int:
        return int(self.addition * self.multiplier)
