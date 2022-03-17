import game
import random

entrance = game.Room("Entrance")
entrance.set_description("Spacious entrance to the castle.")

hall = game.Room("Hall")
hall.set_description("A large room with ornate golden decorations on each wall.")
worm = game.Special_enemy("Underground worm", "A weak worm, you can't even hear his voice")
worm.set_conversation("... ... ...")
worm.set_weakness("underground")
hall.set_character(worm)
simple_sword = game.Weapon("Simple sword", random.randint(1, 3))
simple_sword.set_description("Not really powerfull one.")
hall.set_item(simple_sword)


left_corridor = game.Room("Short left corridor")
left_corridor.set_description("Long dark corridor with unpleasent smell.")
insect = game.Special_enemy("Angry bee", "Seems like regular bee, but it's the size of a ball")
insect.set_weakness("flying")
insect.set_conversation("You don't look like a flower!")
left_corridor.set_character(insect)

right_corridor = game.Room("Short right corridor")
right_corridor.set_description("Absolutely dark corridor with strange sounds.")
shark = game.Special_enemy("Peacefull shark", "To be honest, not really peacefull...")
shark.set_weakness("underwater")
shark.set_conversation("Don't you have some water? I'm really thirsty!")
right_corridor.set_character(shark)
small_aid = game.Heal("Pink potion", 5, "heal")
small_aid.set_description("Pink potion, that will heal your health by 5.")
right_corridor.set_item(small_aid)

left_tower = game.Room("Left tower")
left_tower.set_description("Old and tall tower.")
small_wizard = game.Special_enemy("Unsure wizard", "Not really understand, how spell works", min_max=(3, 7))
small_wizard.set_weakness(None)
small_wizard.set_conversation("You better stay away from me!")
left_tower.set_character(small_wizard)
normal_sword = game.Weapon("Simple sword", random.randint(3, 5))
normal_sword.add_random_buff()
normal_sword.set_description("Something more powerfull.")
left_tower.set_item(normal_sword)

right_tower = game.Room("Right tower")
right_tower.set_description("Old and tall tower.")
small_wizard = game.Special_enemy("Unsure wizard", "Not really understand, how spell works", min_max=(3, 7))
small_wizard.set_weakness(None)
small_wizard.set_conversation("You better stay away from me!")
right_tower.set_character(small_wizard)
normal_sword = game.Weapon("Simple sword", random.randint(3, 5))
normal_sword.add_random_buff()
normal_sword.set_description("Something more powerfull.")
right_tower.set_item(normal_sword)

storehouse = game.Room("Storehouse")
storehouse.set_description("Unexpected storehouse with barely open door. Something stange is happening inside.")
aid = game.Heal("Red potion", 5, "increase max health")
aid.set_description("Red potion, that will increase your max health by 5.")
storehouse.set_item(aid)

basement = game.Room("Basement")
basement.set_description("Cold dark basement. Someone is screaming inside.")
big_bee = game.Special_enemy("Really big bee", "Well, it wasn't a scream. It was a buzzz on really high pithes.", min_max=(3, 7))
big_bee.set_weakness("flying")
big_bee.set_conversation("Hi, honey!!!")
basement.set_character(big_bee)
basement.set_item(aid)

left_long_corridor = game.Room("Long left corridor")
left_long_corridor.set_description("Another long and not really cosy corridor.")
left_long_corridor.set_item(small_aid)


right_long_corridor = game.Room("Long right corridor")
right_long_corridor.set_description("Another long and not really cosy corridor.")
right_long_corridor.set_item(small_aid)

library = game.Room("Library")
library.set_description("Quite library full of strange empty books.")
big_wizard = game.Special_enemy("Confident wizard", "Really understand, how spell works", min_max=(5, 7))
big_wizard.set_weakness(None)
big_wizard.set_conversation("Come closer, give me a hug!")
library.set_character(big_wizard)
library.set_item(small_aid)


kithcen = game.Room("Kithcen")
kithcen.set_description("Spacious room with only one table and knife in it.")
spider = game.Special_enemy("Spider-Cook", "Spider-cook, spider-cook, cooks whatever, a spider hook.", min_max=(6, 8))
spider.set_weakness("underground")
spider.set_conversation("When I look in youe eyes... everything... feel... not quite normal.")
kithcen.set_character(spider)
normal_sword = game.Weapon("Simple sword", random.randint(5, 7))
normal_sword.add_random_buff()
normal_sword.set_description("Something more powerfull.")
kithcen.set_item(normal_sword)


bedroom = game.Room("Bedroom")
bedroom.set_description("Seems like someone dangerous was sleeping there.") 
boss = game.Special_enemy("Cactus", "Really? How can they even sleep?", min_max=(8, 10))
boss.set_weakness("underground")
boss.set_conversation("Can you pat my spikes, please?")
bedroom.set_character(boss)

entrance.link_room(hall, "north")
hall.link_room(left_corridor, "west")
hall.link_room(right_corridor, "east")
right_corridor.link_room(basement, "north")
right_corridor.link_room(right_tower, "east")
left_corridor.link_room(storehouse, "north")
left_corridor.link_room(left_tower, "west")
left_tower.link_room(left_long_corridor, "north")
left_long_corridor.link_room(library, "west")
left_long_corridor.link_room(bedroom, "east")
right_tower.link_room(right_long_corridor, "north")
right_long_corridor.link_room(kithcen, "east")
right_long_corridor.link_room(bedroom, "west")

current_room = entrance
player = game.Player(15)
print("Here's your journy begins!\nYou have to find boss in bedroom and win him.")
print("To check your stats, type: stats.")
while player.health>0:
    if not bedroom.get_character():
        print("Congratulations! You won!")
    print()
    current_room.get_details()
    item = current_room.get_item()
    if item is not None:
        print()
        item.describe()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        if current_room.move(command):
            current_room = current_room.move(command)
        else: print("No room there!")
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "take":
        if item is not None and not current_room.character:
            if isinstance(item, game.Weapon):
                print("You equiped", item.get_name())
                player.change_weapon(item)
            else:
                print("You put the " + item.get_name() + " in your backpack")
                print("To use it, type: heal")
                player.inv.append(item)
            current_room.set_item(None)
        elif current_room.character:
            print("You can't take item, until you kill an enemy!")
        else:
            print("There's nothing here to take!")
    elif command == "fight":
        if current_room.character:
            player.attack(inhabitant)
            if inhabitant.health<=0:
                print(f"You killed {inhabitant.name}")
                current_room.character = None
            if player.health<=0:
                print("Oops, you're not realy alive now.")
                print("That's the end of the game.")
        else: print("There is no one here to fight with")
    elif command == "heal":
        if not player.inv:
            print("Your backpack is empty!")
            continue
        print("Your inventory, type aid name to use:")
        for h_item in player.inv:
            print(h_item)
        aid = input("> ")
        healed = False
        for h_item in player.inv:
            if h_item.name == aid:
                h_item.heal(player)
                del player.inv[player.inv.index(h_item)]
                healed = True
        if not healed:
            print("No such aid in backpack")
    elif command == "stats":
        print("Your hp:", player.health)
        print("Your damage:", player.damage)
    else:
        print("Don't know, how to do it.")
