import room


def read_out(lists):
    for item in diction:
        print(item, end=", ")
    print("")
def stat_check():#update if they are able to continue
    if energy <= 0:
        exploritng = False 
        

    else:
        print(f"Energy:{energy}")
        print(f"Gold:  {gold}")
#Introduction
introction = open("script.txt")
intro = introction.read()
print(intro)
#Start
exploritng = True
energy = 15
in_room = "Entrance"
last = "exit"
gold =0

while exploritng:
    stat_check()
    control = input("What would you like to do:")
    cost = 0
    if control =="exit":#leave or quit
        exploritng = False
        continue
    elif control =="seach":#look around the room
        gold += room.seach(in_room)

    elif control == "move":#move to different room
        hold = in_room
        in_room = room.neighbor_room(in_room, last)
        last = hold
        if in_room == "exit":#different way of leaving
            energy=0
        energy -= 1
    elif control == "reveiw":#check infomation
        print(intro)
    elif control == "test":#behind the sean check
        room.test()
    else:
        print("That is not a value direction. Please try again.")

    
print(f"Thanks for playing")#end text
print(f"You collected {gold} Gold")



