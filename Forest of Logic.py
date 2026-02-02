#We will combine our List (inventory) with a While Loop (game loop) and If/Else (choices).

inventory = [] # An empty backpack
hp = 100 # Player Health Points
playing = True # Game loop control

print("Welcome to the Forest of Logic!")

while playing and hp > 0:
    print(f"\nHP: {hp} | Inventory: {inventory}")
    choice = input("You see a 'cave' and a 'river'. Where do you go? ").lower()

    if choice == "cave":
        print("It's dark. You found a 'Torch'!")
        inventory.append("torch")
    elif choice == "river":
        print("The water is freezing! You lost 20 HP.")
        hp -= 20
    elif choice == "quit":
        playing = False
    else:
        print("Invalid choice.")

    # Game Over Check
    if hp <= 0:
        print("You fainted! Game Over.")

print("Thanks for playing!")