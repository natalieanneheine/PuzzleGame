import random

read_text = open("riddles.txt")
riddles = read_text.readlines()
read_text.close()

# index 0 and 1  store text infomantion, 2 has anwser, 3 tell it solved.
cipher_option = [
    [1,10,"2-10-1","unsolved"],
    [11,19,"1-13-3","unsolved"],
    [20,28,"4-10-2","unsolved"],
    [29,38,"3-9-1","unsolved"],
]


riddle_option_open = [
    [87,93,"candle","unsolved"],
    [94,100,"wrong","unsolved"]
]
riddle_text_multple_choice = [
    [39,48,"Teapot","unsolved"],
    [49,62,"Black","unsolved"],
    [65,76,"White","unsolved"],
    [77,85,"Coin","unsolved"],
]
# store what puzzle is assign to a item
room_puzzle ={

}

def cipher(item):
    gold = -1
    if item not in room_puzzle:#check to see is puzzle has been assign
         room_num =random.randrange(0, len(cipher_option))#assign puzzle
         room_puzzle[item] = cipher_option[room_num]
         cipher_option.pop(room_num)#remove puzzle option
    puzzle = room_puzzle[item]
    gold = solving(puzzle)
    return gold


def riddle_o(item):
    gold = -1
    if item not in room_puzzle:#check to see is puzzle has been assign
         room_num =random.randrange(0, len(riddle_option_open))#assign puzzle
         room_puzzle[item] = riddle_option_open[room_num]
         riddle_option_open.pop(room_num)#remove puzzle option
    puzzle = room_puzzle[item]
    gold = solving(puzzle)
    return gold

def riddle_mc(item):
    gold = -1
    if item not in room_puzzle:#check to see is puzzle has been assign
         room_num =random.randrange(0, len(riddle_text_multple_choice))#assign puzzle
         room_puzzle[item] = riddle_text_multple_choice[room_num]
         riddle_text_multple_choice.pop(room_num)#remove puzzle option
    puzzle_info = room_puzzle[item]
    anwser = puzzle_info[2]
    if puzzle_info[3] == "solved":
        print("You already solved this puzzle")
        gold = 0
    else:
        for num in range(puzzle_info[0],puzzle_info[1]):
            print(riddles[num])
        guess = input("Enter:")
        if guess == "back":
            gold = 0
        
        else:
            if anwser != guess:
                gold = 0
                print("Incorrect")
            else:
                gold = random.randrange(2,8)
                print(f"Correct! You found {gold} Gold.")
            puzzle_info.insert(3, "solved")
    return gold

    

def solving(puzzle_info):
    anwser = puzzle_info[2]
    if puzzle_info[3] == "solved":
        print("You already solved this puzzle")
        gold = 0
    else:
        for num in range(puzzle_info[0],puzzle_info[1]):
            print(riddles[num])
        guess = input("Enter:")
        while anwser != guess and guess != "back":
            print("Incorrect")
            guess = input("Enter:")
        if guess == "back":
            gold = 0
        elif guess == anwser:
            puzzle_info.insert(3, "solved")
            gold = random.randrange(2,8)
            print(f"Correct! You found {gold} Gold.")
        return gold

def test():# testing spacing
    for puzzle in cipher_option:
        for num in range(puzzle[0],puzzle[1]):
                print(riddles[num])
        print("------------------------")
    for puzzle in riddle_option_open:
        for num in range(puzzle[0],puzzle[1]):
                print(riddles[num])
        print("------------------------")
    for puzzle in riddle_text_multple_choice:
        for num in range(puzzle[0],puzzle[1]):
                print(riddles[num])
        print("------------------------")
