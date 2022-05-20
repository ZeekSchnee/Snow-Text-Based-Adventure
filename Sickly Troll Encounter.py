import Battle
import NPCEncounters
import Prompt
from NPCEncounters import ricker_error
from config import player
from Prompt import end_of_prompt
from Prompt import tripper
from Prompt import player_ui
from Battle import FireEle
from random import randint

enemies = ['']
# Intro stuff
player_name = input("What's your name?: ")
player.name = player_name
print('''*Hey, I'm the voice in your head. Type "help" for a list of commands.*''')
print(f'''Alright, {player.name}... Let's start your adventure! (Type "Start" to continue)''')

# Holy shit, great job on all of that prompt work!! Everything works the way you want it too!! Amazing!
# Now for the next step! Should be easy, let's make a disobedience/pissed function for NPC like Ricker

cont = False
contains_ui = False
disobedience = 0
while not cont:
    answer = input("> ").lower()
    contains_ui = player_ui(answer)
    if answer == 'start':
        cont = True
    elif answer == 'quit':
        print("*** Naaaah, jk. You don't wanna quit. You just started! ***")
        input('''Press Enter to continue. > ''')
        cont = True
    else:
        print('''*Can't really follow directions, but fuck you, it's my game. Type "Start".*
''')
        disobedience += 1
        if disobedience > 2:
            print("Ok, ok fine. You win fuck head. Enjoy the thing I MADE for you. Jesus Christ...")
            input('''Press Enter to continue. > ''')
            print('')
            cont = True
print('''You stumble your way through the brush after a long hike, and find your way into a run down tavern.
The bartender greets you.''')

battle = False
contains_ui = True
answer = ''
while not battle:
    a1 = 'yes'
    a2 = 'no'
    if answer == 'yes':
        battle = NPCEncounters.ricker1()
        break
    elif answer == 'no':
        battle = NPCEncounters.ricker2()
        break
    elif answer == 'quit':
        Prompt.quit_game()
        break
    if contains_ui:
        q = '''"Greetings, adventurer! Welcome to the Sickly Troll!
    Name's Ricker. Have you coin for a drink?"'''
        answer, contains_ui = end_of_prompt(q, a1, a2)
    else:
        q = ricker_error[randint(0, len(ricker_error) - 1)]
        answer, contains_ui = end_of_prompt(q, a1, a2)
if battle:
    input("(Press Enter to battle!) > ")
    enemies = Battle.appear(FireEle(), 1)

if player.health <= 0:
    print('''
    YOU DIED.''')
elif player.health > 0 and enemies == []:
    print('''
    YOU SURVIVED!''')
