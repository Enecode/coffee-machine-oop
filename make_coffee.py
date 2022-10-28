class CoffeeMaker:
    """Model of machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    def report(self):
        """Print all available resources"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
    
    def is_resources_surfficient(self, drink):
        """Returns True when order can be made and false if ingredients is not enough"""
        can_make_coffee = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make_coffee = False
        return can_make_coffee
    
    