# Simple_Python-Game
**A simple Rock-Paper-scissors game made by using Python.**

## How it works:
This code works with 2 functions, 4 if/elif/else lines, 1 loop, 2 inputs and try/except statements.



**OPPONENT'S POSIBILITIES**

1:

    import random

2:

    x = random.randint(1,3)

3:

    if x==1:
        q="PAPER"
    elif x==2:
        q="SCISSORS"
    elif x==3:
        q="ROCK"


First code is the library that gives us access to randomize opponents move.
Second code is for the random value of x
Last code shows us what the value of the x gives us as a command (game movement)



**STARTING MATCH LOOP**

    while True:
        new_match = input("Would you like to start a new match? Y/N").upper()
        if new_match=="Y":
            game()
        elif new_match=="N":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please enter Y or N only.")


this code will ask the user to start a new match every time he plays a round.
Y (Yes) will start a new match
N (No) will stop the whole program
Unknown commands are handled with the else statement



**USERS MOVE**

    USER = input("""PAPER : 1
    SCISSORS : 2
    ROCK : 3 """)

    if USER=="1":
        p="PAPER"
    elif USER=="2":
        p="SCISSORS"
    elif USER=="3":
        p="ROCK"
This code helps the user to interact with the game freely



**WIN/LOSE/TIE AND TRY/EXCEPT**

1:

    try:
            if (int(USER)==x):
                print("TIE!")

            elif (x==1 and USER=="2") or (x==2 and USER=="3") or (x==3 and USER=="1"):
                print("You Win!")

            elif (x==2 and USER=="1") or (x==3 and USER=="2") or (x==1 and USER=="3"):
                print("You Lose!")

            show_result()
            print("---------------------------------------")
            
2:

    except ValueError: #1
        print("""ERROR. Please enter known number commands only Error code: 1""")

    except TypeError: #2
        print("""ERROR. Please enter known number commands only Error code: 2 """)

    except Exception: #general
        print("""ERROR. Please enter known number commands only Something went wrong!""")

First code decides the winner
Win: 3 ways to happen
Lose: 3 ways to happen 
tie: happens when both players pick the same move
Second code handles all the errors (especially (int(USER)==x):)




__Where can be improved:__

The game resets all the time. Instead, scores can be added to save the wins.
Except exception is too general, more except commands can be added.
This is terminal only since i still dont know how GUI works. GUI can be added in the future
