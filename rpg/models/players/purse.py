class Purse:
    def __init__(self, start_balance: int = 0):
        self._balance = start_balance

    def can_afford(self, price: int) -> bool:
        return self._balance >= price

    def give_money(self, value: int) -> int or ValueError:
        if value > self._balance:
            return ValueError
        self._balance -= value
        return value

    def earn_money(self, value: int):
        self._balance += value

    def get_balance(self):
        return self._balance
