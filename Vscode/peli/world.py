import random

rooms = {
    "Grimhall village": {
        "description": (
            "You are in the quiet village of Grimhall. Smoke curls from chimneys, "
            "but an uneasy stillness hangs in the air, as if the villagers fear "
            "something lurking beyond the hills."
        ),
        "enemies": [],  # No enemies in the village
        "next": "Darkwood"
    },
    "Darkwood": {
        "description": (
            "As you leave the town, you enter a forest, which is dense and dark, shadows twisting between gnarled trees. "
            "Every rustle of leaves or snapping branch makes your heart race, as "
            "though unseen eyes follow your every move."
        ),
        "enemies": ["Goblin", "Forest Spider", "Wolf"],
        "next": "Cave"
    },
    "Cave": {
        "description": (
            "You spot a cave and decide to enter a fetid smelling hole where the air is damp and cold. Strange echoes "
            "bounce off the stone walls, and the sense of being watched gnaws at your nerves."
        ),
        "enemies": ["Cave Spider", "Bat Swarm", "Giant Rat"],
        "next": "Tundra"
    },
    "Tundra": {
        "description": (
            "You rise from the cave and enter a vast tundra. The tundra stretches endlessly, a frozen wasteland. The icy wind cuts like a blade, "
            "and snowdrifts conceal dangers that could strike without warning."
        ),
        "enemies": ["Ice Bear", "Frost Wolf", "Snow Spider"],
        "next": "Old Castle"
    },
    "Old Castle": {
        "description": (
            "You spot the ruins of an old castle before you. Shadows creep along crumbling walls, "
            "and the faint sound of chains dragging across stone sends chills down your spine."
        ),
        "enemies": ["Castle Guard", "Armored Knight", "Dark Archer"],
        "next": "Abandoned Dungeon"
    },
    "Abandoned Dungeon": {
        "description": (
            "Stairs to your left lead into a dungeon that has long been abandoned. The air is thick with mildew and the stench of decay. "
            "Darkness wraps around you like a living thing, and every step echoes in the oppressive silence."
        ),
        "enemies": ["Castle Lord 'Ironhand'"],  # Boss only
        "next": None
    }
}

# Helper to randomly pick an enemy from a room
def get_random_enemy(room_name):
    room = rooms[room_name]
    if not room["enemies"]:
        return None
    return random.choice(room["enemies"])
