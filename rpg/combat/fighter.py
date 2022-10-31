from rpg.models.entities.entity import Entity


class Fighter:
    def __init__(self, fighter_entity: Entity, controllable: bool):
        self._step = fighter_entity.get_speed()
        self._value = 0
        self._controllable = controllable
        self.entity = fighter_entity

    @property
    def step(self) -> int:
        return self._step

    @property
    def value(self) -> int:
        return self._value

    @property
    def controllable(self) -> bool:
        return self._controllable

    def make_step(self):
        self._value += self._step

    def end_turn(self, step_back: int):
        self._value -= step_back

    @staticmethod
    def _is_valid(other):
        return hasattr(other, "value") and hasattr(other, "step")

    def __eq__(self, other):
        if not self._is_valid(other):
            return NotImplemented
        return (self.value == other.value) and (self.step == other.step)

    def __lt__(self, other):
        if not self._is_valid(other):
            return NotImplemented
        return (self.value < other.value) or (self.value == other.value and self.step < other.step)
