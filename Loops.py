# This will count from 0 to 4
for i in range(5):
    print(f"Ohanz is on lap number {i}")

health = 3

while health > 0:
    print(f"You are still standing! Current health: {health}")
    health = health - 1  # Taking "damage"

print("Game Over!")
