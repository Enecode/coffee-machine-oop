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
    
    def report(self):
        """Print the current profit"""
        print(f"Money: {self.CURRENCY} {self.profit} ")
    
    def process_coins(self):
        """Return the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_recieved += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_recieved
        
    