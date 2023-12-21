

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
        if prompt == "off": 
            print("Goodbye")
            exit()
        elif prompt == "report":
            print("Water: " + str(water) + "ml" + "\nMilk: " + str(milk) + "ml" + "\nCoffee: " + str(coffee) + "g" + "\nMoney: $" + str(money))
        else: 
            if checkresources(MENU[prompt]["ingredients"], water, milk, coffee) == True:
                # ask for money
                
            else: 
                # tell them what is insufficient

def checkresources(ingredients, water, milk, coffee):
    if ingredients["water"] < water and ingredients["milk"] < milk and ingredients["coffee"] < coffee: 
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

if __name__ == "__main__":
    main()