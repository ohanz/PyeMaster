# 1. Ask the user for their status
status = input("Do you have a 'ticket', are you 'VIP', or are you 'staff'? ").lower()

# 2. Logic Check
if status == "vip":
    print("Welcome, VIP! Please head to the lounge.")
elif status == "staff":
    print("Good morning. Head to the back entrance, please.")
elif status == "ticket":
    print("Ticket verified. Enjoy the show!")
else:
    print("Sorry, you need a ticket to enter.")