import random
import puzzle
#text file with all description

read_text = open("description.txt")
desript = read_text.readlines()
read_text.close()
room_list =  [
    "Dinner room",
    "Bed room",
    "Office",
    "Living room",
    "Kitchen",
    "Library"
]
room_item = {
    "Entrance" :["Coathanger"],
    "Dinner room":["Cabinet", "Table"],
    "Bed room":["Bed","Closet"],
    "Office":["Desk","File box"],
    "Living room":["Coffee Table","Cupboard", "Couches"],
    "Kitchen":["Counter","Fridge"],
    "Library":["BookShelf","Study Desk"],
}

room_info = {}
# index 0 and 1 are the text description and 2 is the puzzle type.
item_desription = {
    "Coathanger":[0,4,4],
    "Cabinet":[18,22,1],
    "Table":[36,40,3],
    "Bed":[40,44,3],
    "Closet":[4,8,4],
    "Desk":[23,28,1],
    "File box":[28,32,1],
    "Coffee Table":[44,48,3],
    "Cupboard":[32,36,1],
    "Couches":[8,12,4],
    "Counter":[48,52,3],
    "Fridge":[13,18,4],
    "BookShelf":[53,59,2],
    "Study Desk":[60,66,2]

}

# check surronding room
def neighbor_room(current_room, last_room):
    if current_room not in room_info:# check to see if neighbor_room as been assign
        door_count =random.randrange(1, 4)#generate connecting room
        if door_count > len(room_list):
            door_count = len(room_list)
        room_conect = [last_room]#inclueds the room that they came from
        for door in range(door_count):
            room_num =random.randrange(0, len(room_list))
            room_conect.append(room_list[room_num])
            room_list.pop(room_num)
            room_info[current_room] = room_conect#remove room from list to prvent repeating rooms
     # Read out the rooms
    room_paths =room_info[current_room]
    for door in room_paths:
        print(door, end=", ")
    print("\n\n")
    new_room = input("Enter one room:")
    while new_room not in room_paths:#get what room they are moving to 
        new_room = input("invalid answer please enter one of the door:")

    return new_room #move to room

def read_out(lists):
    for item in lists:
        print(item, end=", ")
    print("")


def seach(current_room):
    items = room_item[current_room]#find item
    read_out(items)
    gold = -1
    while gold == -1:
        print("Enter 'back' it you want to do something else \n \n")
        look_at =input("Enter what would you like to look at:")#what item to investigate
        while (look_at not in items) and (look_at != "back"):
            look_at = input("Not valid input please try again:")
        if look_at == "back":
            item_info = [0,0,0] 
        else:
            item_info = item_desription[look_at]
        for num in range(item_info[0],item_info[1]):
            print(desript[num])
        if item_info[2] == 1:# final index detrmine puzzle type
            gold = puzzle.cipher(look_at)
        elif item_info[2] == 2:
            gold = puzzle.riddle_o(look_at)
        elif item_info[2] == 3:
            gold = puzzle.riddle_mc(look_at)
        else:
            gold = 0
    return gold
def test():#Test text alignment
    for item in item_desription.values():
        for num in range(item[0],item[1]):
            print(desript[num])
        print("======================")

    puzzle.test()     
        
