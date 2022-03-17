import random
class Room():
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {"south": None,
                             "north": None, "west": None, "east": None}
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_room(self, room, direction):
        opposite_directions = {"south": "north",
                               "north": "south", "west": "east", "east": "west"}
        self.linked_rooms[direction] = room
        room.linked_rooms[opposite_directions[direction]] = self

    def get_details(self):
        print(self.name)
        print("-"*20)
        print(self.description)
        for room_direction in self.linked_rooms:
            if self.linked_rooms[room_direction]:
                print(
                    f"The {self.linked_rooms[room_direction].name} is {room_direction}")

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def move(self, direction):
        return self.linked_rooms[direction]

    def set_item(self, item):
        self.item = item
    def get_item(self):
        return self.item


class Enemy():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def describe(self):
        print(self.name+" is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def talk(self):
        print(f"[{self.name} says]: "+self.conversation)

    def fight(self, fight_with):
        return fight_with == self.weakness

    def get_defeated(self):
        return None


class Item():
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f"The [{self.name}] is here - "+self.description)

    def get_name(self):
        return self.name

class Special_enemy(Enemy):
    def __init__(self, name, description, min_max=(1, 3)):
        super().__init__(name, description)
        self.damage=random.randint(*min_max)
        self.health=random.randint(*min_max)
    def describe(self):
        super().describe()
        print(f"Stats: {self.damage} damage and {self.health} hp.")

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
        self.buffs = None
    def add_random_buff(self):
        enemy_type = random.choice(["flying", "underwater", "underground", "boss"])
        self.buffs = (enemy_type, random.choice([1.2]*10+[1.5]*6+[1.75]*4+[2]*2+[3]))
    def describe(self):
        super().describe()
        if self.buffs: buffs = f"{self.buffs[1]}X damage to {self.buffs[0]} enemies."
        else: buffs = "-"
        print(f"{self.name} - deals {self.damage} damage. Buff: {buffs}")

class Heal(Item):
    def __init__(self, name, heal_power, h_type):
        super().__init__(name)
        self.heal_power = heal_power
        self.h_type = h_type
    def heal(self, other):
        if self.h_type == "heal":
            other.health = min(other.max_health, self.heal_power+other.health)
            print(f"Your healt now: {other.health}")
        else:
            other.max_health+=self.heal_power
            print(f"Your max health now is {other.max_health}")
    def __repr__(self):
        return f"{self.name} - {self.h_type} by {self.heal_power}"
    
class Player():
    def __init__(self, health):
        self.max_health = health
        self.health = health
        self.inv = []
        self.weapon = None
        self.armor = None
        self.damage = 1
    def change_weapon(self, weapon):
        self.weapon = weapon
        self.damage = 1 + weapon.damage
    def attack(self, other):
        damage = self.damage
        if self.weapon and self.weapon.buffs:
            if other.weakness == self.weapon.buffs[0]:
                damage *= self.weapon.buffs[1]
        other.health -= damage
        print(f"You dealt {damage} damage to {other.name}")
        self.health -= other.damage
        print(f"{other.name} dealt {other.damage} to you")
        print(f"Your hp: {max(self.health, 0)}, enemy hp: {max(other.health, 0)}")

