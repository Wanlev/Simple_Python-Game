import random


def game():    #main game
    def show_result():    #shows both players moves
        print(f"""You: {p}
opponent: {q}""" )

    x = random.randint(1,3)    #random number from 1-3 with equal possibilities

#q = opponents move
    if x==1:
        q="PAPER"
    elif x==2:
        q="SCISSORS"
    elif x==3:
        q="ROCK"

#USER = users move
    USER = input("""PAPER : 1
SCISSORS : 2
ROCK : 3 """)

    if USER=="1":
        p="PAPER"
    elif USER=="2":
        p="SCISSORS"
    elif USER=="3":
        p="ROCK"

    try:
            if (int(USER)==x):    #same move
                print("TIE!")

            elif (x==1 and USER=="2") or (x==2 and USER=="3") or (x==3 and USER=="1"):    #user wins (3 ways to happen)
                print("You Win!")

            elif (x==2 and USER=="1") or (x==3 and USER=="2") or (x==1 and USER=="3"):    #user wins (3 ways to happen)
                print("You Lose!")

            show_result()
            print("---------------------------------------")

    except ValueError: #1

        print("""ERROR. Please enter known number commands only
Error code: 1""")
    except TypeError: #2
        print("""ERROR. Please enter known number commands only
Error code: 2 """)
    except Exception: #general
        print("""ERROR. Please enter known number commands only
Something went wrong!""")

while True:
    new_match = input("Would you like to start a new match? Y/N").upper()

    if new_match=="Y":  #starts the game
        game()
    elif new_match=="N":    #quits the whole program
        print("Goodbye!")
        break
    else:
        print("Unknown command. Please enter Y or N only.")    #unknown command for new_match