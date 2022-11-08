from rpg.input.game_input import GameInput


class ConsoleInput(GameInput):
    def __init__(self):
        super().__init__()

    def get_int_value(self, min_value: int, max_value: int) -> int:
        def _invalid_value():
            print("Please, enter a valid integer")

        value = 0

        while True:
            try:
                value = int(input(f"Enter an integer value in range [{min_value}, {max_value}]: "))
            except ValueError:
                _invalid_value()
                continue
            else:
                if min_value <= value <= max_value:
                    break
                else:
                    _invalid_value()
        return value
