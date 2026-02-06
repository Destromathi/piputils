# main.py
from world import rooms
from player import Player
from enemies import create_enemy
from fight import fight
import random

# Keep track of bosses that appear only once
spawned_bosses = set()

# Define enemies per zone (except Abandoned Dungeon which has only Ironhand)
zone_enemies = {
    "Grimhall village": [],  # no enemies
    "Darkwood": ["Goblin", "Wolf", "Forest Spider"],
    "Cave": ["Giant Rat", "Bat Swarm", "Cave Spider"],
    "Tundra": ["Ice Bear", "Frost Wolf", "Snow Spider"],
    "Old Castle": ["Castle Guard", "Armored Knight", "Dark Archer"],
    "Abandoned Dungeon": ["Castle Lord 'Ironhand'"]
}

def main():
    print("🎮 Welcome to Grimhall!")
    name = input("What is your name? ")
    player = Player(name)
    current_room = "Grimhall village"

    while player.is_alive():
        room = rooms[current_room]
        print("\n" + room["description"])

        if room["enemies"]:
            enemies_in_zone = zone_enemies.get(current_room, [])
            for _ in range(3):  # 3 fights per zone
                if not enemies_in_zone:
                    break  # no enemies
                enemy_name = random.choice(enemies_in_zone)

                # Skip boss if already spawned
                if enemy_name in spawned_bosses:
                    continue

                enemy = create_enemy(enemy_name)

                # Boost boss stats
                if enemy_name == "Castle Lord 'Ironhand'":
                    enemy.max_hp = 200
                    enemy.hp = 200
                    enemy.defense += 2
                    enemy.min_dmg += 2
                    enemy.max_dmg += 2
                    spawned_bosses.add(enemy_name)

                if not fight(player, enemy):
                    print("💀 You have died. Game over.")
                    return

        if room["next"] is None:
            print("🏆 You have conquered Grimhall!")
            return

        input("Press Enter to continue...")
        current_room = room["next"]

if __name__ == "__main__":
    main()
