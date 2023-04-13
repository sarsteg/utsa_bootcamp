# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for x in range(len(candy_list)):
    print(f"{x+1}: {candy_list[x]}")

# Setup default answer user for input
answer = "yes"

while answer == "yes":
    selected = input("Which candy would you like to bring home? ")
    candy_cart.append(candy_list[int(selected)-1])
    answer = input("Would you like to make another selection? ('yes' or 'no') ")

# Print the candy cart
print("I brought home with me...")
for candy in candy_cart:
    print(candy)