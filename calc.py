print("--- Simple Python Calc ---")

# 1. Get the numbers (convert to float so we can use decimals)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Get the operation
print("Options: + , - , * , /")
op = input("Choose an operation: ")

# 3. Perform the logic
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    # Check if dividing by zero (which breaks computers!)
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid Operation"

# 4. Show the result
print(f"Result: {result}")