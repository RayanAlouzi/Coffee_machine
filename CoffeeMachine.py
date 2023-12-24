class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0
        self.MENU = {
            "espresso": {
                "ingredients": {"water": 50, "coffee": 18},
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {"water": 200, "milk": 150, "coffee": 24},
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {"water": 250, "milk": 100, "coffee": 24},
                "cost": 3.0,
            }
        }

    def run(self):
        while True:
            prompt = self.get_input()
            if prompt == "off":
                print("Goodbye")
                break
            elif prompt == "report":
                self.print_report()
            else:
                self.make_coffee(prompt)

    def print_report(self):
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}")

    def make_coffee(self, order):
        if self.check_resources(self.MENU[order]["ingredients"]):
            total_input = self.get_money()
            if total_input < self.MENU[order]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = total_input - self.MENU[order]["cost"]
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {order}. Enjoy!")
                self.update_resources(order)

    def check_resources(self, ingredients):
        if ingredients.get("water", 0) > self.water:
            print("Sorry there is not enough water.")
            return False
        if ingredients.get("milk", 0) > self.milk:
            print("Sorry there is not enough milk.")
            return False
        if ingredients.get("coffee", 0) > self.coffee:
            print("Sorry there is not enough coffee.")
            return False
        return True

    def update_resources(self, order):
        ingredients = self.MENU[order]["ingredients"]
        self.water -= ingredients.get("water", 0)
        self.milk -= ingredients.get("milk", 0)
        self.coffee -= ingredients.get("coffee", 0)
        self.money += self.MENU[order]["cost"]

    def get_input(self):
        while True:
            answer = input("What would you like?: ")
            if answer in ["espresso", "latte", "cappuccino", "report", "off"]:
                return answer
            print("Please enter a valid input.")

    def get_money(self):
        total = 0
        for coin, value in [("quarters", 0.25), ("dimes", 0.1), ("nickels", 0.05), ("pennies", 0.01)]:
            while True:
                try:
                    count = int(input(f"How many {coin}?: "))
                    total += count * value
                    break
                except ValueError:
                    print("Please enter a valid input.")
        return total

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()