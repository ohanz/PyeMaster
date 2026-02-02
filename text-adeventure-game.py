player_health = 100
inventory = [] # This is a List (a new concept!) # An empty backpack
game_running = True

print("You wake up in a dark forest. There is a path to the 'left' and 'right'.")


# Finding items
inventory.append("Rusty Sword")
inventory.append("Health Potion")
inventory.append("Mysterious Map")

print(f"In your bag: {inventory}")

if "Health Potion" in inventory:
    print("You drink the Health Potion and restore 20 health points.")
    player_health += 20
    inventory.remove("Health Potion")
if "Mysterious Map" in inventory:
    print("Got Map! You know the way to the Secret Cave!")
else:
    print("You are lost in the woods.")    
print(f"Your health: {player_health}")
print(f"In your bag now: {inventory}")
print("You see a wild beast ahead!")
print("Do you want to 'fight' or 'run'?")
print("To be continued...")
print("Thank you for playing!")
print("Goodbye!")
