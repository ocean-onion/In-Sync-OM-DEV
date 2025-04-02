from utils.utilities import color, clear, wait, typingprint, typinginput, colourprint, wait
from utils.tools import execute_dev_command

BLUE = color.BLUE
CYAN = color.CYAN
GREEN = color.GREEN
PURPLE = color.PURPLE
RED = color.RED
YELLOW = color.YELLOW
'''Dark Colours'''  # remove in public
DARKBLUE = color.DARKBLUE
DARKCYAN = color.DARKCYAN
DARKPURPLE = color.DARKPURPLE
'''Accents'''  # remove in public
BOLD = color.BOLD
UNDERLINE = color.UNDERLINE
END = color.END

def create_players(num_players):
    players = []
    typingprint(f"{DARKBLUE}Let's get to know the players!{END}")
    wait(0.3)

    for i in range(num_players):
        while True:
            wait(0.3)
            clear()
            name = typinginput(f"{BLUE}Enter the name of Player {i + 1}: {END}")

            if name.startswith("!?"):  # remove in public
                command = name[2:]
                execute_dev_command(command, [], players) 
                continue

            if not name.strip():
                typingprint(f"{RED}{BOLD}Invalid input! Name cannot be empty.{END}")
                continue

            if name in [player["name"] for player in players]:
                typingprint(f"{RED}{BOLD}Name already taken!{END}")
                continue

            break

        clear()
        typingprint(f"{GREEN}Welcome to the game, {name}!{END}")
        players.append({"name": name, "deck": []})
        wait(0.8)

    return players
