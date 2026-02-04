from classes import choose_class
from player import create_player
from combat import fight
from world import move_player, describe_room, get_available_directions, ROOMS
from boss import spawn_boss
import copy

ORIGINAL_ROOMS = copy.deepcopy(ROOMS)

print("🌲 VARJOJEN METSÄ 🌲")

stats = choose_class()
player = create_player(stats)

def start_game():
    current_room = "kylä"

    while True:
        while player["hp"] > 0:
            describe_room(current_room)
            room = ROOMS[current_room]

            if room.get("boss"):
                boss = spawn_boss()
                fight(player, is_boss=True, boss_data=boss)
                room["boss"] = False

            elif room.get("enemy"):
                fight(player)
                room["enemy"] = False

            directions = get_available_directions(current_room)
            print("Mahdolliset suunnat:", ", ".join(directions))
            cmd = input("Mihin mennään? (tai quit): ").lower()

            if cmd == "quit":
                return

            if cmd in directions:
                current_room = move_player(current_room, cmd)
            else:
                print("❌ Et voi mennä sinne.")

        print("\n💀 Kuolit!")
        choice = input("Aloitetaanko alusta? (k/e): ").lower()

        if choice == "k":
            stats = choose_class()
            new_player = create_player(stats)
            player.clear()
            player.update(new_player)

            ROOMS.clear()
            ROOMS.update(copy.deepcopy(ORIGINAL_ROOMS))
            current_room = "kylä"
        else:
            break

start_game()
print("💀 Peli päättyi.")
