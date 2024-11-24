import random

# Constants
DUNGEON_SIZE = 5
START_HEALTH = 100

# Dungeon generation
def generate_dungeon(size):
    dungeon = [[None for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            dungeon[i][j] = random.choice(["Empty", "Monster", "Trap", "Treasure"])
    exit_x, exit_y = random.randint(0, size - 1), random.randint(0, size - 1)
    dungeon[exit_x][exit_y] = "Exit"
    return dungeon

# Display status
def display_status(position, health, inventory):
    print(f"\nYou are in Room {position}.")
    print(f"Health: {health}")
    print(f"Inventory: {inventory}\n")

# Handle events
def handle_event(event, health, inventory):
    if event == "Monster":
        print("You encountered a Monster!")
        action = input("Do you want to [fight] or [flee]? ").lower()
        if action == "fight":
            damage = random.randint(10, 30)
            print(f"You fought the Monster and lost {damage} health.")
            health -= damage
        else:
            print("You fled from the Monster!")
    elif event == "Trap":
        damage = random.randint(5, 20)
        print(f"You triggered a trap and lost {damage} health.")
        health -= damage
    elif event == "Treasure":
        loot = random.choice(["Potion", "Gold"])
        print(f"You found a treasure: {loot}!")
        inventory.append(loot)
    elif event == "Exit":
        print("You found the Exit! You win!")
        return health, inventory, True
    else:
        print("This room is empty.")
    return health, inventory, False

# Main game loop
def main():
    dungeon = generate_dungeon(DUNGEON_SIZE)
    player_position = [0, 0]
    health = START_HEALTH
    inventory = []

    print("Welcome to Dungeoneering!")
    print("Find the Exit to win. Watch out for traps and monsters!\n")

    while health > 0:
        display_status(player_position, health, inventory)
        move = input("Enter a direction (north, south, east, west): ").lower()

        # Move player
        if move == "north" and player_position[0] < DUNGEON_SIZE - 1:
            player_position[0] += 1
        elif move == "south" and player_position[0] > 0:
            player_position[0] -= 1
        elif move == "east" and player_position[1] < DUNGEON_SIZE - 1:
            player_position[1] += 1
        elif move == "west" and player_position[1] > 0:
            player_position[1] -= 1
        else:
            print("You can't move in that direction!")
            continue

        # Trigger event
        x, y = player_position
        event = dungeon[x][y]
        dungeon[x][y] = "Visited"
        health, inventory, won = handle_event(event, health, inventory)
        if won:
            break

    if health <= 0:
        print("You have run out of health. Game over!")

# Run the game
if __name__ == "__main__":
    main()