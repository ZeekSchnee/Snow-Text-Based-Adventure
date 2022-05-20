import Prompt
import Battle
from config import player
from Prompt import end_of_prompt
from Prompt import tripper
from Prompt import player_ui
from Prompt import enough_money
from random import randint


class NPC:
    def __init__(self, name, cha, pwr, wis):
        self.name = name
        self.char = cha
        self.pwr = pwr
        self.wis = wis


ricker = NPC('Ricker', 12, 9, 8)
ricker_error = ['"Eh, what was that?"', '''"One more time, sonny? I'm hard of hearing."''',
                '"Come again?"', '''"I don't uh... What?"''']


def ricker1():
    battle = False
    contains_ui = True
    answer = ''
    drunk = 0
    while not battle:
        a1 = 'fine'
        a2 = 'no thanks'
        if answer == 'fine':
            player.gold -= 5
            print("*You pay 5 gold*.")
            drunk += 1
            if drunk > 1:
                print('''You feel a brilliant heat behind your back.
You're too drunk to save yourself from the Fire elemental.''')
                player.health = 0
                break
            else:
                print('''The innkeeper giggles slightly as he passes you the ale.
It's much too strong and tastes like shit.

"You want another?"''')
        elif answer == 'no thanks':
            print('''"Mmmm... Maybe you're smarter than ya look. HeHEeee!"''')
            battle = ricker2()
            return battle
        elif answer == 'quit':
            Prompt.quit_game()
            break
        if contains_ui:
            q = '"How does 5 gold for an ale sound?"'
            answer, contains_ui = end_of_prompt(q, a1, a2)
        else:
            q = ricker_error[randint(0, len(ricker_error) - 1)]
            answer, contains_ui = end_of_prompt(q, a1, a2)


def ricker2():
    battle = False
    contains_ui = True
    answer = ''
    while not battle:
        a1 = "Quests"
        a2 = "Bed"
        if answer == 'quests':
            print('''"Hmm, now lemme take a look at the bulletin bo-!"
        "Oh, holy shit! Well, there's your quest!!"
''')
            battle = True
            return battle
        elif answer == 'bed':
            battle = ricker3()
            return battle
        if contains_ui:
            q = '''"Well, whadidja come here for? We haven't much space for non-customers."'''
            answer, contains_ui = end_of_prompt(q, a1, a2)
        else:
            q = ricker_error[randint(0, len(ricker_error) - 1)]
            answer, contains_ui = end_of_prompt(q, a1, a2)


def ricker3():
    battle = False
    contains_ui = True
    answer = ''
    while not battle:
        a1 = "regular is fine"
        a2 = "I'm feeling fancy"
        if answer == 'regular is fine':
            pmt = 10
            if enough_money(pmt):
                print('''   *10 gold is removed from your inventory.*
The innkeeper leads you to a surprisingly cozy room and hands you a key.
    You hear screams coming from downstairs.
    As you wheel around the staircase, you come face to visage with a fire elemental! 
''')
                battle = True
                return battle
        if answer == "i'm feeling fancy" or answer == 'im feeling fancy':
            pmt = 30
            if enough_money(pmt):
                print('''   *30 gold is removed from your inventory.*
The innkeeper hands you a key garnished with gems, and points you to your room.
    Once you close yourself to your temporary quarters, the hustle of the inn fades into ominous silence.''')
                if player.wis > 13:
                    print("* Perhaps the inn has cast a silence spell on the door here. That's quite handy!")
                else:
                    print("* Quite curious, indeed. Maybe you'll have to ask to owner about that.")
                print('''
As you lay comfortably in your bed, the door may keep out the sound,
    but it does not keep out the smoke. You strap on your gear and head towards the door to investigate.''')
                input('''(Press Enter to continue) > ''')
                if player.pwr >= 15:
                    print('''   ***Crash***
The door swings open, but your reflexes act before your brain realizes what is standing before you.
    You are now face to face with a fire elemental...''')
                    battle = True
                    return battle
                else:
                    print(f'''   ***Smack***
A Fire Elemental swings the door open and cracks you in the face for {Battle.FireEle().dmg-3} damage''')
                    battle = True
                    return battle
            elif not enough_money(pmt):
                print('''"Huh, doesn't look like you've got the gold, kid."''')
                battle = ricker5()
                return battle
        if contains_ui:
            q = "We've got a couple of them. You want the regular room or the deluxe? 10g and 30g respectively."
            answer, contains_ui = end_of_prompt(q, a1, a2)
        else:
            q = ricker_error[randint(0, len(ricker_error) - 1)]
            answer, contains_ui = end_of_prompt(q, a1, a2)


def ricker5():
    battle = False
    tripped = False
    contains_ui = False
    answer = ''
    while not battle:
        a1 = '(yeah) *Shoulda checked my inv.*'
        a2 = 'no'
        if contains_ui:
            contains_ui = False
            tripped = tripper(tripped)
        elif not contains_ui:
            tripped = tripper(tripped)
            if answer == 'yeah':
                player.gold -= 10
                print('''   *10 gold is removed from your inventory.*
The innkeeper leads you to a surprisingly cozy room and hands you a key.
    You hear screams coming from downstairs.
    As you wheel around the staircase, you come face to visage with a fire elemental! 
                ''')
                battle = True
                return battle
            elif answer == 'no':
                battle = ricker1()
                return battle
            elif answer == 'quit':
                Prompt.quit_game()
                break
            if tripped:
                q = '"How about we settle for the nice regular bed instead, eh?"'
                answer = end_of_prompt(q, a1, a2)
                contains_ui = player_ui(answer)
            else:
                q = ricker_error[randint(0, len(ricker_error) - 1)]
                answer = end_of_prompt(q, a1, a2)
                tripped = tripper(tripped)
                contains_ui = player_ui(answer)

