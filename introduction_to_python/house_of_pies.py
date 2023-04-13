pies_list = [
    "Pecan", 
    "Apple Crisp", 
    "Bean", 
    "Banoffee", 
    "Black Bun", 
    "Blueberry", 
    "Buko", 
    "Burek"
]

# Print list of Pies
print("Our pie selection for today:")
for x in range(len(pies_list)):
    print(f"{x+1}: {pies_list[x]}")

# Setup default answer user for input
answer = "yes"
cart = []

while answer == "yes":
    selected = input("Which pie would you like to bring home? ")
    cart.append(pies_list[int(selected)-1])
    answer = input("Would you like to make another selection? ('yes' or 'no') ")


# Print cart
if len(cart) > 1:
    print(f"You have bought {len(cart)} pies... ")
    for pie in cart:
        print(pie)
else: 
    print("You have bought 1 pie... ")
    for pie in cart:
        print(pie)

print("Thank you for your purchase!")