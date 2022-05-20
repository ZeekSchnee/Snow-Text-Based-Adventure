import config
from config import player
from random import randint
prompt_format = []


def prompt_question(question, ans1, ans2):
    print(question)
    print(f'({ans1})')
    print(f'({ans2})')
    response = input('> ').lower()
    print('')
    return response


def add_prompt(q, a1, a2):
    prompt_format.append(q)
    prompt_format.append(a1)
    prompt_format.append(a2)


def tripper(tripped):
    if tripped:
        tripped = False
        return tripped
    elif not tripped:
        tripped = True
        return tripped


def end_of_prompt(q, a1, a2):
    response = ''
    contains_ui = False
    while not contains_ui:
        add_prompt(q, a1, a2)
        response = (prompt_question(prompt_format[0], prompt_format[1], prompt_format[2]))
        prompt_format.clear()
        contains_ui = player_ui(response)
        return response, contains_ui


# def end_of_prompt(q, a1, a2):
    # add_prompt(q, a1, a2)
    # response = (prompt_question(prompt_format[0], prompt_format[1], prompt_format[2]))
    # prompt_format.clear()
    # return response


def player_ui(ans):
    ui_commands = []
    help_me = '''You can type:
"stat" - for information on your character.
"inv" - for information on what your character possesses.
"quit" - for... well... you know.'''
    stat = f'''-Name: {config.player.name}
-Player health: {player.health}
-Charisma: {player.char}, Strength: {player.pwr}, Wisdom: {player.wis}'''
    weapon_list = [config.weapons_inv()]
    inv = f'''  ***Inventory***
Player gold: {player.gold}
---Weapons---
{weapon_list}'''
    commands = ['help', 'stat', 'inv', 'quit']
    results = [help_me, stat, inv, quit_game()]
    row = len(commands)
    col = 1
    for i in range(row):
        ui_results = []
        for j in range(col):
            ui_results.append(commands[i])
            ui_results.append(results[i])
        ui_commands.append(ui_results)

    def display_cmd_result(__ans):
        _i = 0
        for command in commands:
            if __ans == command:
                print(f'''{ui_commands[_i][1]}''')
            else:
                _i += 1
    if ans in commands:
        contains_ui = True
        display_cmd_result(ans)
        input("(Enter) > ")
        print('')
        return contains_ui
    else:
        contains_ui = False
        return contains_ui


def enough_money(pmt):
    if player.gold >= pmt:
        player.gold -= pmt
        return True
    elif player.gold < pmt:
        return False


def quit_game():
    __goodbyes = ("Alright! See ya, boyo!", "Scared of a little fire guy?", "Bye, Fuck-o.",
                  "Not like I wanted you to play anyways")
    return __goodbyes[randint(0, 3)]


