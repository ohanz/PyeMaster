# 1. Ask the user for input
item_name = input("What are you buying? ")
price = input("How much does it cost? ")
quantity = input("How many are you getting? ")

# 2. IMPORTANT: input() always gives you TEXT (strings). 
# We have to turn price and quantity into NUMBERS to do math.
total = float(price) * int(quantity)

# 3. Print the result
print(f"\nYour total for {quantity} {item_name}(s) is ${total:.2f}")