ROOMS = {
    "kylä": {
        "desc": "Pieni kylä metsän laidalla.",
        "north": "metsä"
    },
    "metsä": {
        "desc": "Tiheä metsä. Polku jatkuu itään.",
        "south": "kylä",
        "east": "luola",
        "enemy": True
    },
    "luola": {
        "desc": "Pimeä luola.",
        "west": "metsä",
        "east": "boss_huone",
        "enemy": True
    },
    "boss_huone": {
        "desc": "Luolan sydän – bossi odottaa.",
        "west": "luola",
        "boss": True
    }
}

def get_available_directions(room):
    return [d for d in ["north", "south", "east", "west"] if d in ROOMS[room]]

def move_player(room, direction):
    return ROOMS[room].get(direction, room)

def describe_room(room):
    print(f"\n📍 {ROOMS[room]['desc']}")
