# CLI Adventure Game - Marshall Ferguson - 6/2020

print("Welcome to the Command Line Adventure Game!")

name = input("Please enter your character's name:     ")
name = name.title()
print("Hello {}!".format(name))

# TODO - create a shop the player can buy things from and sell things to
    # Player will be able to pick buy things back if needed
    # Player will be able to regenerate the shop inventory if needed

shop_inventory = ["sword", "axe", "shield"]
player_inventory = []

print("Let's go to the shop!")
print("Here is the shopkeepers inventory:")
for x in shop_inventory:
    print(x.title())
purchase_answer = input("What would you like to purchase?     ")
if purchase_answer == "sword":
    print("A sword costs 50 gold.")
elif purchase_answer == "axe":
    print("An axe costs 50 gold.")
elif purchase_answer == "shield":
    print("A shield costs 50 gold.")
else:
    print("Oops! That wasn't a valid answer!")

# TODO - create a wilderness area that the player can explore
    # Player will be able to battle monsters to grind for xp/gold
    # Player will be able to unlock different areas of the wilderness
        # Player will have option of which part of wilderness to explore

# TODO - create an area where the player can battle other fighters
    # Player will be able to test themselves by battling fighters of increasing difficulty
    # Player will be able to battle warriors, archers, and mages
        # Player will not be able to choose between the three
