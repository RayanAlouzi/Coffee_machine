

def main(): 
    water = 300
    milk = 200
    coffee = 100
    money = 0
    MENU = { 
        "espresso":{
            "ingredients":{
                "water":50,
                "coffee":18,
        },
            "cost":1.5,
        },
        "latte":{
            "ingredients":{
                "water":200,
                "milk":150,
                "coffee":24,
        },
            "cost":2.5,
        },
        "cappuccino":{
            "ingredients":{
                "water":250,
                "milk":100,
                "coffee":24,
        },
            "cost":3.0,
        }
    }
    while True: 
        prompt = getinput()
        if prompt == "off":  # shut off the machine
            print("Goodbye")
            exit()
        elif prompt == "report":  # print report
            print("Water: " + str(water) + "ml" + "\nMilk: " + str(milk) + "ml" + "\nCoffee: " + str(coffee) + "g" + "\nMoney: $" + str(money))
        else:  # make coffee
            # check if there are enough resources
            if checkresources(MENU[prompt]["ingredients"], water, milk, coffee) == True:  
                totalInput = getmoney()
                if totalInput < MENU[prompt]["cost"]:
                    print("Sorry that's not enough money. Money refunded")
                else:
                    if totalInput > MENU[prompt]["cost"]:
                        print("Here is $" + str(round(totalInput - MENU[prompt]["cost"],2)) + " in change")
                    print("Here is your " + prompt + ". Enjoy!")
                    water -= MENU[prompt]["ingredients"]["water"]
                    milk -= MENU[prompt]["ingredients"]["milk"]
                    coffee -= MENU[prompt]["ingredients"]["coffee"]
                    money += MENU[prompt]["cost"]

def checkresources(ingredients, water, milk, coffee):
    if ingredients["water"] > water:
        print("Sorry there is not enough water")
    elif ingredients["milk"] > milk:
        print("Sorry there is not enough milk")
    elif ingredients["coffee"] > coffee: 
        print("Sorry there is not enough coffee")
    else: 
        return True
    return False
    

def getinput():
    answer = input("What would you like?: ")
    if answer not in ["espresso", "latte", "cappuccino","report","off"]:
        # EDIT LATER: ask if input is the word closest to the input provided
        # if yes, return the word
        # if no, ask prompt again
        print("Please enter a valid input")
        answer = getinput()
    return answer

def getmoney(): 
    while True: 
        try: 
            quarters = int(input("How many quarters?: "))
            break
        except: 
            print("Please enter a valid input")
            continue
    while True: 
        try: 
            dimes = int(input("How many dimes?: "))
            break
        except: 
            print("Please enter a valid input")
            continue 
    while True:
        try: 
            nickels = int(input("How many nickels?: "))
            break
        except: 
            print("Please enter a valid input")
            continue
    while True:
        try: 
            pennies = int(input("How many pennies?: "))
            break
        except: 
            print("Please enter a valid input")
            continue

    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
if __name__ == "__main__":
    main()