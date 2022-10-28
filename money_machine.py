from locale import currency


class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "pennies": 0.01,
        "dimes": 0.10,
        "quarters": 0.25,
        "nickles": 0.05
    }

    def __init__(self) -> None:
        self.profit = 0
        self.money_recieved = 0
        
    