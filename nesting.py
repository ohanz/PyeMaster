status = input("Do you have a 'ticket'? ").lower()

if status == "ticket":
    age = int(input("How old are you? "))
    
    if age >= 18:
        print("Entry granted!")
    else:
        print("You have a ticket, but you are too young for this event.")
else:
    print("No ticket, no entry!")