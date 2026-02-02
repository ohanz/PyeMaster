while True:
    print("\n--- Calculator Menu ---")
    num1 = float(input("Enter first number: "))
    op = input("Operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Can't divide by zero!")
    
    # The Exit Hatch
    quit_choice = input("Calculate again? (y/n): ").lower()
    if quit_choice == "n":
        print("Goodbye!")
        break