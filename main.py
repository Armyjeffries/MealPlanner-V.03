# Lead: Chris 'CJ' Jeffries
# MealPlanner v.034 - Last Update: 17 August 2022
# Meal Planner will create a Meal Plan for a specified number of days by cycling through list of meals.
# Once the Meal Plan is set, the program will build a Grocery_List for the user containing the sum of the ingredients
# from the scheduled meals. -- > Complete v.03 Appx 27 May 2022 --> Program will successfully generate a Meal Plan without duplicates for
# up the number days up to the amount of menu items. It will also sum the ingredients of all the meals, and generate a
# grocery list. <-- Complete v.03 Appx 27 May 2022 <--
# ------
# More interaction w/ MealPlanner, ability to approve/modify plan. -- > Partial Complete v.031 --> Successfully loops for
# approval of the generated meal prompt, allowing user to re-roll a specific day. <--  Partial Complete v.031 <--
# ------
# If modify, re-roll entire list, or change individual items? Manually set items? Read available menu? Read available recipes?
# ------
# ------ Added ability to pick meal replacement, by displaying current menu, or random choice. ------ Version.033
# ------ Added prompt to write selections and grocery list to file "MealPlan.txt" stored on the root folder as the Parent
#_______
#_______ Added "Menu Loop" to allow adding display current Recipe Book, and exit options. _____ Version.034
#
# Ability to add/remove meals/ recipes to the menu?

import random

#Constructor to Create the Meal Plan, needs to know how many days to build, and meals to assign to the days
class MealPlan():
    #Class Attributes (Exist beyond the instance, but are part of the total MealPlan
    __groceryList = {"", ""}

#Constructor method, used to initialize the MealPlan and attributes
    def __init__(self, MealName, Days, ingredients):
        self.__MealName__ = MealName
        self.__Days__ = Days
        self.__ingredients__ = ingredients
        #self.__groceryList = {"",""}

#Accessor methods, used to Get- MealPlan's attributes
    def getMealName(self):
        return self.__MealName__
    def getDays(self):
        return self.__Days__
    def getIngredients(self):
        return self.__ingredients__
    #def getGroceryList(self):
        #return self.__groceryList

#Mutator methods, used to SET- MealPlan's  attributes
    def setMealName(self):
        self.__MealName__ = MealName
    def setDays(self):
        self.__Days__ = Days
    def setIngredients(self):
        self.__ingredients__ = ingredients
    #def setGroceryList(self):
        #self.__groceryList =

HoneyMustardChickenQuinoa = {
  "Chicken Breast":3,
  "Olive Oil (Tbsp)":5,
  "Dijon Mustard (Tbsp)":2,
  "Honey (Tbsp)":4,
  "Cucumber":1,
  "Roma Tomatoes":2,
  "Green Bell Pepper":1,
  "Onion (red)":0.5,
  "Corn (frozen)(bag)":1,
  "Lemon/Lime Juice (oz)":0.5,
  "Paprika (tsp)":0.5
}
Tacos = {
  "Ground Beef (lbs)" : 2,
  "Taco Seasoning (packet)" : 2,
  "Tortilla Chips (bag)":0.5,
  "Taco Shells (box)":1,
  "Black Olives (can)":1,
  "Romaine (head)":2,
  "Petite Dices Tomatoes (can)":1,
  "Shredded Cheddar (bag)":0.5
}
ChickenGreenBeanCass = {
  "Chicken Breast" : 2,
  "Green Beans (can)" : 2,
  "Cream of 'Shroom Soup" : 1,
  "Mayo (soup can)" : .5,
  "Curry (tsp)" : 1,
  "Cheddar Cheese (block)":1,
  "Parmesan Cheese (grated)(bottle)":0.25,
  "Blueberry Muffins (4pk)":2,
  "Cranberry Jelly (can)":1
}
CheeseburgersAndFries = {
  "Ground Beef (lbs)": 2,
  "Hamburger Buns (pkg)": 1,
  "Fries (crinkle/steak)(pkg)": 1,
  "Cheese Slices (asst)":1,
}
SpagAndMeatballs = {
  "Meatballs (frozen)(pkg)":1,
  "Spaghetti noodles (angel hair or other)":1,
  "Spaghetti Sauce (jar)":2,
}
TexMex = {
  "Ground Beef (lbs)":1,
  "Black Beans (can)":2,
  "Salsa-Mild (oz)":12,
  "Shredded Cheddar (bag)":0.5,
  "Tortilla Chips (bag)":0.25,
}
ChickenAndPeppers = {
  "Chicken Breast":3,
  "Cherry Tomatoes (pkg)":2,
  "Fuji Apples":10,
  "Bell Peppers (asst color)":6,
  "Italian Dressing (bottle)":2,
}
PhillyCheeseSteak = {
  "Flank Steak (lbs)":2.5,
  "Bell Peppers (asst color)":12,
  "Onion (yellow/ white)":1,
  "Soy Sauce (Tbsp)":2,
  "Provolone Cheese Slices (pkg)":2,
}
BalsamicChicken = {
  "Chicken Breast":2,
  "Salsa-Mild (oz)":16,
  "Balsamic Vinegar (cup)":0.5,
  "Bell Peppers (asst color)":2,
  "Onion (white)":1,
  "Rice":1,
}
CheeseDip = {
  "Cheese Melt (Velveeta)":1,
  "Ground Beef (lbs)":1,
  "Rotel (can)":1,
  "Tortilla Chips (bag)":0.5
}
Leftovers = {
  "Leftovers":1
}
ChickenEnchiladaSoup = {
  "Chicken Breast":2,
  "Olive Oil (Tbsp)":1,
  "Onion (yellow/ white)":1,
  "Garlic (glove)":3,
  "Chicken Broth (cup)":3,
  "Tomato Sauce (can)":1,
  "Black Beans (can)":1,
  "Petite Dices Tomatoes (can)":1,
  "Corn (frozen)(bag)":1,
  "Cumin (tsp)":1,
  "Oregano (tsp)":0.5,
  "Shredded Cheddar (bag)":0.5,
  "Tortilla Chips (bag)":0.5,
}
TurkeyTacoChili = {
  "Ground Beef (lbs)":3,
  "Onion (yellow/ white)":1,
  "Bell Peppers (asst color)":2,
  "Rotel (can)":1,
  "Corn (frozen)(bag)":1,
  "Kidney Beans (can)":1,
  "Tomato Sauce (can)":1,
  "Refried Beans (Fat Free)(can)":1,
  "Taco Seasoning (packet)":1,
  "Chicken Broth (cup)":2.5,
  "Tortilla Chips (bag)":0.5,
}
BBQChicken = {
  "Chicken Breast":3,
  "BBQ Sauce (bottle)":1
}

#Meal Ideas: Stir Fry, Black Bean Quinoa Chili Bowl, G'Ma's Mac'N'Cheese,
#Dictionary contain K,V pairs for "Selections">MealName; building link between "Selection">MealName>Ingredients
mealList = {"1":"Honey Mustard Chicken w/ Quinoa Salad","2":"Tacos","3":"Chicken Green Bean Casserole",
            "4":"Cheeseburgers and Fries","5":"Spaghetti and Meatballs","6":"Tex-Mex Casserole",
            "7":"Chicken and Peppers","8":"Philly Cheesesteak Peppers","9":"Balsamic Chicken","10":"Cheese Dip",
            "11":"Leftovers","12":"Chicken Enchilada Soup","13":"\"Turkey\" Taco Chili","14":"BBQ Chicken"}
#Dictionary containing K,V pairs for MealName>Ingredients; building link between "Selection">MealName>Ingredients
Meals = {
  "Honey Mustard Chicken w/ Quinoa Salad": HoneyMustardChickenQuinoa,
  "Tacos": Tacos,
  "Chicken Green Bean Casserole": ChickenGreenBeanCass,
  "Cheeseburgers and Fries": CheeseburgersAndFries,
  "Spaghetti and Meatballs": SpagAndMeatballs,
  "Tex-Mex Casserole": TexMex,
  "Chicken and Peppers": ChickenAndPeppers,
  "Philly Cheesesteak Peppers": PhillyCheeseSteak,
  "Balsamic Chicken": BalsamicChicken,
  "Cheese Dip": CheeseDip,
  "Leftovers": Leftovers,
  "Chicken Enchilada Soup": ChickenEnchiladaSoup,
  "\"Turkey\" Taco Chili": TurkeyTacoChili,
  "BBQ Chicken": BBQChicken
}
### The Program "starts" here
#Setting initial  menuSelection variable

while True:
    print("\n\n*** Main Menu ***\nWhat would you like to do? Please enter a number for your selection: ")
    try:
        menuChoice = input("1: Display Recipe Book\n2: Build a Meal Plan\n3: Exit\n : ")    
        while menuChoice == "1":
            print("\n\n*** Recipe Book ***\nCurrent Meals:")
            for x,y in mealList.items():
                print(x,":",y)    
            print("\n\nWould you like to edit the Recipe Book?")
            editChoice = input("Y/N : ")
            try:
                if editChoice in ("Y","y","Yes","yes","YES"):
                    print("*** Editing Recipe Book ***\nWould you like to : ")
                    editChoice = input("1: Add a recipe\n2: Block a recipe from meal selection\n3: Edit a recipe\n4: Exit\n : ")
                    if editChoice == "1":
                        print("Feature coming Soon")
                        editChoice = "4"
                    elif editChoice == "2":
                        print("Feature coming Soon")
                        editChoice = "4"
                    elif editChoice == "3":
                        print("Feature coming Soon")
                        editChoice = "4"
                    elif editChoice == "4":
                        print("Exit to Main Menu")
                        pass
                    else:
                        raise ValueError
            except Exception as e:
                print(e)
                pass
            menuChoice = input("1: Display Recipe Book\n2: Build a Meal Plan\n3: Exit\n : ")
        while menuChoice == "2":
            while True:    
                try:
                    Days = int(input("\n\nPlease enter the number of days for the Meal Plan: "))
                    if Days > 14:
                        raise ValueError
                    elif Days < 1:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("Sorry, at this time we can only accommodate Meal Plans up to " + str(
                    len(mealList)) + " days (due to not repeating meals)")
                    pass
            groceryList = {"Ingredient": "\t\tAmount"}

            selectionList = []
            for r in range(Days):
                selection = str(random.randint(1,len(mealList)))
                while selection in selectionList:
                    selection = str(random.randint(1,len(mealList)))
                selectionList.append(selection)

            while True:
                for s in range(len(selectionList)):
                    MealName = mealList.get(selectionList[s])
                    ingredients = Meals.get(MealName)
                    myMealPlan = MealPlan(MealName, Days, ingredients)
                    print("Day",s+1,myMealPlan.getMealName())
                print("________"*7)
                approve = input("Do you wish to keep this meal plan? Y/N: ")
                if approve in ("Y","y","Yes","yes","YES"):
                    break
                if approve in ("N","n","No","no","NO"):
                    newDay = int(input("Which day would you like to change? ")) - 1
                    MealName = mealList.get(selectionList[newDay])
                    print("Day", newDay + 1, MealName, )
                    approve = input("Is this the meal you want to change? Y/N ")
                    if approve in ("N", "n", "No", "no", "NO"):
                        pass
                    if approve in ("Y","y","Yes","yes","YES"):
                        approve = int(input("Do you want to select a meal from the Menu, or let me pick?\n1: Manual Meal Select\n2: Pick for me\n:"))
                        try:
                            if approve == 1:
                                for x,y in mealList.items():
                                    print(x,":",y)
                                selection = input("Which Meal would you like to put in for Day "+str(newDay+1)+"? : ")
                                while int(selection) not in range(1,len(mealList)):
                                    raise ValueError
                                selectionList[newDay] = selection
                            elif approve == 2:
                                while selection in selectionList:
                                    selection = str(random.randint(1, len(mealList)))
                                else:
                                    selectionList[newDay] = selection
                                    pass
                        except ValueError:
                            print("Must pick a Meal from the Menu. 1-"+str(len(mealList))+": ")
                            pass
                if approve in ("N", "n", "No", "no", "NO"):
                    pass
            for s in range(len(selectionList)):
                MealName = mealList.get(selectionList[s])
                ingredients = Meals.get(MealName)
                myMealPlan = MealPlan(MealName, Days, ingredients)
                for x, y in ingredients.items():
                    if x in groceryList:
                        z = groceryList[x]
                        groceryList.update({x: y + z})
                    else:
                        groceryList.update({x: y})
            #    print("Day",s+1,myMealPlan.getMealName(),selectionList[s]) #Alternate Print line to INCLUDE meal Selection Number
                print("Day", s + 1, myMealPlan.getMealName())
            print("_____" * 7)

            print("Grocery List for the above meals:")
            for x,y in groceryList.items():
                print(x,"\t",y)
            print("_____" * 7)
            approve = input("Do you want to write this list to a file (to print)? ")

            if approve in ("Y","y","Yes","yes","YES"):
                file = open("MealPlan.txt", "w")
                for s in range(len(selectionList)):
                    MealName = mealList.get(selectionList[s])
                    ingredients = Meals.get(MealName)
                    myMealPlan = MealPlan(MealName, Days, ingredients)
                    file.write(str("\nDay "+str(s + 1)+" "+myMealPlan.getMealName()))  # Alternate Print line to EXCLUDE meal Selection Number
                file.write("\n"+("_____"*7))
                file.write("\nGrocery List for the above meals:")
                for x, y in groceryList.items():
                    file.write("\n"+str(x)+" "+str(y))
                file.write("\n"+("_____" * 7))
            menuChoice = "1"
        while menuChoice == "3":
            menuChoice = "0"
            break
    except Exception as e:
        print(e)
        pass
    if menuChoice == "0":
        break
