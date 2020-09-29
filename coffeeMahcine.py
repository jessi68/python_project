# Write your code here



#may be need unitCapacity variable at next stage

 # user don't need to know


money = 550






class coffeeMachine:
    units = {"water" : "ml", "milk" : "ml", "coffee beans" : "grams"}
    unitCapacity = {"water" : 200, "milk" : 50, "coffee beans" : 15}
    coffeeRecipes = {"espresso": {"water": 250, "coffee beans" : 16},
                    "latte": {"water": 350, "milk" : 75, "coffee beans": 20},
                    "cappuccino": {"water": 200, "milk": 100, "coffee beans": 12}}
    costs = {"espresso": 4, "latte": 7, "cappuccino": 6}

    def __init__(self):
        self.capacities = {"water" : 400, "milk" : 540, "coffee beans" : 120}
        self.ingredients = self.capacities.keys()
        self.requiredCoffees = 9
        self.money = 550
    def canBuying(self, coffeetype):
        capacities = self.capacities

        recipe = self.coffeeRecipes[coffeetype]
        for ingredient in recipe.keys():
            if capacities[ingredient] < recipe[ingredient]:
                print("Sorry, not enough water!")
                return False

        return True

    def buy(self, recipe, coffeeType):

        print("I have enough resources, making you a coffee!")

        for ingredient in recipe.keys():


            self.capacities[ingredient]-= recipe[ingredient]

        self.money += self.costs[coffeeType]
        self.requiredCoffees -= 1




    def fill(self):
        # I think we add code that add expenditure of ingredient costs
        # or decrease net profit(순이익)
        print()

        for ingredient in self.ingredients:
            amount = int(input(f"Write how many {self.units[ingredient]} of {ingredient} do you want to add:\n"))
            self.capacities[ingredient]+= amount

        self.requiredCoffees+= int(input('Write how many disposable cups of coffee do you want to add:\n'))



    def detailsInfo(self):
        machineInfo = f"The coffee machine has:"

        for ingredient in self.ingredients:
            machineInfo+= f"\n{self.capacities[ingredient]} of {ingredient}"

        machineInfo+= f"\n{self.requiredCoffees} of disposable cups"
        machineInfo+= f"\n${self.money} of money\n"
        print(machineInfo)

    def takeMoney(self):
        self.money -= 564

        if self.money < 0:
            self.money = 0

robot = coffeeMachine()

while True:
    task = input("Write action (buy, fill, take, remaining, exit):\n")

    if task == "buy":
        coffee = {1: "espresso", 2: "latte", 3: "cappuccino"}
        
        num = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if num == "back":
            continue
        else:
            num = int(num)

        coffeeType = coffee[num]
        recipe = robot.coffeeRecipes[coffeeType]

        if robot.canBuying(coffeeType):
            robot.buy(recipe, coffeeType)
        else:
            pass


    elif task == "fill":
        robot.fill()

    elif task == "take":
        print(f"\nI gave you $564")
        robot.takeMoney()
        
    elif task == "remaining":
        print()
        robot.detailsInfo()
        continue
    else:
        break

    print()

#print(f'''For {coffee_nums} cups of coffee you will need:
#{coffee_nums * 200} ml of water
#{coffee_nums * 50} ml of milk
#{coffee_nums * 15} g of coffee beans''')


