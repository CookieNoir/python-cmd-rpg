def get_int_value(min_value: int, max_value: int) -> int:
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
