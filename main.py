# Lead: Chris 'CJ' Jeffries
# MealPlanner v.03 - Last Update: 27 May 2022
# Meal Planner will create a Meal Plan for a specified number of days by cycling through list of meals.
# Once the Meal Plan is set, the program will build a Grocery_List for the user containing the sum of the ingredients
# from the scheduled meals. -- > Complete v.03 Appx 27 May 2022 --> Program will successfully generate a Meal Plan without duplicates for
# up the number days up to the amount of menu items. It will also sum the ingredients of all the meals, and generate a
# grocery list.
# ------
# More interaction w/ MealPlanner, ability to approve/modify plan. If modify, re-roll entire list, or change individual
# items? Manually set items? Read available menu? Read available recipes?
# ------
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
  "Chicken Breast (lbs)":2,
  "Olive Oil (Tbsp)":4.5,
  "Dijon Mustard (Tbsp)":1,
  "Honey (Tbsp)":2,
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
  "Parmesan Cheese (grated)(bottle)":0.25
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
  "Black Beans (can)":1,
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
mealList = {"1":"Honey Mustard Chicken w/ Quinoa Salas","2":"Tacos","3":"Chicken Green Bean Casserole",
            "4":"Cheeseburgers and Fries","5":"Spaghetti and Meatballs","6":"Tex-Mex Casserole",
            "7":"Chicken and Peppers","8":"Philly Cheesesteak Peppers","9":"Balsamic Chicken","10":"Cheese Dip",
            "11":"Leftovers","12":"Chicken Enchilada Soup","13":"\"Turkey\" Taco Chili","14":"BBQ Chicken"}
#Dictionary containing K,V pairs for MealName>Ingredients; building link between "Selection">MealName>Ingredients
Meals = {
  "Honey Mustard Chicken w/ Quinoa Salas": HoneyMustardChickenQuinoa,
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
Days = int(input("The number of days to build the Meal Plan for: "))
groceryList = {"Ingredient": "\t\t\t\t\tAmount"}
selectionList = [0]
for r in range(Days):
    selection = str(random.randint(1,14))
    while selection in selectionList:
        selection = str(random.randint(1,14))
    MealName = mealList.get(selection)
#    MealName = mealList.get(str(random.randint(1,14)))
    ingredients = Meals.get(MealName)
    myMealPlan = MealPlan(MealName, Days, ingredients)
    #groceryList.update(ingredients)
    for x,y in ingredients.items():
        if x in groceryList:
            z = groceryList[x]
            groceryList.update({x:y+z})
        else:
            groceryList.update({x:y})
    selectionList.append(selection)
#    print("Day",r+1,myMealPlan.getMealName(),selectionList[r+1]) #Alternate Print line to INCLUDE meal Selection Number
    print("Day",r+1,myMealPlan.getMealName()) #Alternate Print line to EXCLUDE meal Selection Number
    #print(myMealPlan.getIngredients())
print("_____"*7)


print("Grocery List for the above meals:")
for x,y in groceryList.items():
    print(x,y)
