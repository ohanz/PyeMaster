secret_password = "python123"
guess = ""

while guess != secret_password:
    guess = input("Enter the password: ")
    
    if guess == secret_password:
        print("Access Granted!")
    else:
        print("Wrong! Try again.")

# The "3 Attempts" Password Script
# 
secret_password = "magic"
attempts = 0  # Our counter starts at zero
max_attempts = 3

while attempts < max_attempts:
    guess = input(f"Enter password (Attempt {attempts + 1}/{max_attempts}): ")
    
    if guess == secret_password:
        print("🔓 Access Granted!")
        break  # This exits the loop immediately if you're right
    else:
        attempts = attempts + 1  # Add 1 to the counter
        print(f"❌ Wrong! You have {max_attempts - attempts} tries left.")

if attempts == max_attempts:
    print("🚫 System Locked. Too many failed attempts.")        