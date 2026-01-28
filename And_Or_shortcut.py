has_ticket = True
age = 20

if has_ticket and age >= 18:
    print("Welcome in!")
else:
    print("Access denied.")

is_vip = True
has_ticket = False

if is_vip or has_ticket:
    print("Come on in, one of those is good enough!")

isStaff = True
hasTicket = False
if isStaff or hasTicket:
    print("Access granted.")

has_ticket = False
is_vip = True

if (has_ticket or is_vip) and age >= 18:
    print("You're good to go!")
else:
    print("Something is missing...")
print(has_ticket, is_vip, age) 
print(f"our current values: {has_ticket}, {is_vip}, {age}.")   