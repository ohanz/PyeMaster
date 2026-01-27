name = "Future Coder"
print("Hello, " + name + "!")

# This asks the user for their name and stores it in a variable
user_name = input("What is your name? ")

# This prints a personalized greeting
print("Welcome to the world of coding, " + user_name + "!")

age = input("How old are you? ")

# We convert the input (text) into an integer (number)
age = int(age)

if age >= 18:
    print(f"You are {age}. You're old enough to build professional apps!")
else:
    print(f"You are {age}. Great start! You'll be a pro before you're 20.")


price = 10
quantity = 3
print(f"The total cost is: ${price * quantity}")

