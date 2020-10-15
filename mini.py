# pizza cafe
# Lists to store the printing data for the itemised list in the end of the program!
l1 =[]
l2 = []

# -------Crust Base price List ---------#########
crust =  ['Thick','Thin','Wood Fire']
crust_base = [
    40,     # Thin
    65,     # Thick
    85,     # Wood Fire
]

# ###-----------List of Cheese Style Choices----#########

cheese_style = ['chedder',      #1
                'colby',        #2
                'edam',         #3
                'emmental',     #4
                'gruyere',      #5
                'mozzarella',   #6
                'provolone',    #7
                'ricotta'       #8
               ]
cheese_cost = 0.5  # cost of each cheese regardless of style

# #####----------Toppings Price List ----------#####
toppings = ['Tomato','Mushrooms','Pepperoni','Onions','Black Olives','Green Pepper','Anchovies','Garlic','Ham','Bacon']
topping_choices = [
    75,     # 1 tomato.
    75,     # 2 mushrooms.
    50,     # 3 pepperoni.
    25,     # 4 onions.
    75,     # 5 black olives.
    50,     # 6 green peppers.
    25,     # 7 anchovies.
    50,     # 8 garlic.
    150,     # 9 ham.
    125,     # 10 bacon.
]
totalAmount = 0     # Total payable bill amount.
MAX_CHEESE = 3  # maximum number of cheese per pizza.
MAX_TOPPINGS = 6  # maximum  number of toppings per pizza.
pizzaCount = 0     # looping variable equivalent to No. of pizza
crust_type = 'null'  # initially setting crust type to null.
loop_state = 1

# Getting the customer's name
customerName = input("Please enter your name to proceed with your order:")


# getting total number of pizzas from customer.
try:
    pizzaNum = int(input("Number Of Pizza:"))
except ValueError:
    print("Please enter your response in integers here in order to proceed with your order!")
    pizzaNum = int(input())

# Looping till pizzaNum = pizzaCount
while pizzaCount <= pizzaNum - 1:

    # getting crust type from the customer.
    try:
        crust_type=int(input("Which type of pizza crust would you like : (1)Thin , (2)Thick, (3)Wood Fire:"))
    except ValueError:
        print("Please enter your response in digits here in order to proceed with your order:")
        crust_type = int(input())

    # Checking for invalid integer input.
    while crust_type > 3 or crust_type < 1:
        print("Please enter a valid input:")
        crust_type = int(input("Which type of pizza crust would you like : (1)Thin , (2)Thick, (3)Wood Fire:"))

    # Storing item name and price on same index in two different lists.
    l1.append(crust[crust_type - 1])
    l2.append(crust_base[crust_type - 1])

    # Updating Total Amount after selecting crust for the pizza.
    totalAmount += crust_base[crust_type-1]

    # getting cheeseType from the customer
    cheeseType = 'null'  # initially setting cheeseType to null.
    cheeseCount = 0  # looping variable for getting cheeseTypes.
    try:
        cheeseNum = int(input("How many types of cheese would you like on your pizza:"
                      "(1)One, (2)Two, (3)Three:"))
    except ValueError:
        print("Please enter the digits 1,2 or 3 in order to proceed with desired option:")
        cheeseNum = int(input())

    while cheeseNum > 3 or cheeseNum < 1:
        print("Please enter a valid input here:")
        cheeseNum = int(input())

    # Checking the max No. of cheese condition and prompting until a valid response.
    while cheeseNum > MAX_CHEESE:
        print("You can add up maximum" + str(MAX_CHEESE) + "cheeses only!")
        cheeseNum = int(input("How many cheese would you like on your pizza:"))


    # getting Type/Flav for each cheese added.
    while cheeseNum - 1 >= cheeseCount:
        try:
            cheeseType = int(input("Which Style of cheese would you like:"
                        "(1)chedder, (2)colby, (3)edman, (4)emmental, (5)druyere, (6)mozzarella, (7)provolone, (8)ricotta:"))
        except ValueError:
            print("Please enter your response in form of digits to proceed:")
            cheeseType = int(input())
        # Checking for invalid Integer input.
        while cheeseType > 8 or cheeseType < 1:
            print("Please enter a valid response")
            cheeseType = int(input())

        cheeseCount += 1    # Incrementing the looping variable.
        l1.append(cheese_style[cheeseType - 1])
        l2.append(cheese_cost)

    # Updating total amount after selecting the cheese number and cheese type.
    totalAmount += cheese_cost * cheeseNum

    # Getting input for toppingNum from the customer.
    toppingType = 'null'    # initially setting topping type to null.
    toppingCount = 0    # looping variable for getting each topping.

    # Getting toppingNum including valueError exception handling.
    try:
        toppingNum = int(input("How many toppings would you like on your pizza?:"))
    except ValueError:
        print("Please enter the number of toppings  in digits.")
        toppingNum = int(input())

    # Checking the maximum number of toppings condition and prompting customer until valid response.
    while toppingNum > MAX_TOPPINGS:
        print("You can have maximum " + str(MAX_TOPPINGS) + " toppings per pizza!")
        toppingNum = int(input("How many toppings would you like on your pizza:"))

    # Getting toppings from the customer.
    while toppingCount <= toppingNum - 1:
        try:
            topping = int(input ("Which topping would you like on your pizza:"
                        "(1)Tomato, (2)Mushrooms, (3)Pepperoni, (4)Onions, (5)Black Olives, (6)Green Peppers, (7)Anchovies,"
                        "(8)Garlic, (9)Ham, (10)Bacon:"))
        except ValueError:
            print("Please enter your response in digits only:")
            topping = int(input())

        while topping > 10 or topping < 1:
            print("Please enter a valid response:")
            topping = int(input())

        l1.append(toppings[topping - 1])
        l2.append(topping_choices[topping - 1])

        # Updating total amount after selection of each topping.
        totalAmount += topping_choices[topping - 1]
        if toppingCount == toppingNum - 1:
            print("Done with you pizza no: "+str(pizzaCount+1)+" let's move on to next pizza")
            print("-----------------------------------------------------------------------")
        toppingCount += 1  # Incrementing the looping variable.

    # Incrementing pizzaCount for next iteration.
    pizzaCount += 1


# printing the itemised list and the total charge
print("     The order of:    ",customerName)
for i in range (0,len(l1) - 1):
    print("     "+l1[i]+"   "+str(l2[i]) )
print("     Total No. of Pizza:  "+str(pizzaNum))
print("     The total charge:    "+str(totalAmount))


