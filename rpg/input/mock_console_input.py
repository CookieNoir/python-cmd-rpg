from rpg.input.game_input import GameInput
from random import randrange


class MockConsoleInput(GameInput):
    def __init__(self):
        super().__init__()

    def get_int_value(self, min_value: int, max_value: int) -> int:
        return randrange(min_value, max_value + 1)
