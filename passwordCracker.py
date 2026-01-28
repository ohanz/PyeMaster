secret_password = "python123"
guess = ""

while guess != secret_password:
    guess = input("Enter the password: ")
    
    if guess == secret_password:
        print("Access Granted!")
    else:
        print("Wrong! Try again.")