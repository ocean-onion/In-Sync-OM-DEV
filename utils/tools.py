import sys
from utils.utilities import color, colourinput, colourprint, typingprint, clear, typinginput


def execute_dev_command(command, players, played_cards):
    if command == "players":
        players_list(players)
    elif command == "cards":
        show_cards(players)
    elif command == "played":
        show_played_cards(played_cards)
    elif command == "all":
        show_all_info(players, played_cards)
    elif command == "clear":
        clear()
    elif command == "exit":
        sys.exit(0)
    elif command == "help":
        show_help()
    elif command == "about":
        about()
    else:
        typingprint(f"{color.RED}Unknown dev command: {command}{color.END}")
        typingprint(
            f"{color.RED}Type '!?help' for a list of available commands.{color.END}"
        )


def players_list(players):
    colourprint(f"{color.CYAN}Players:{color.END}")
    for player in players:
        colourprint(
            f"{color.BLUE}{player['name']} - {len(player['deck'])} cards{color.END}"
        )
    print()
    typinginput(f"{color.DARKCYAN}Press Enter to continue...{color.END}")
    clear()

def show_cards(players):
    colourprint(f"{color.CYAN}Cards per player:{color.END}")
    for player in players:
        card_list = ", ".join(
            [f"{color.YELLOW}{card}{color.END}" for card in player["deck"]])
        colourprint(f"{color.BLUE}{player['name']}: {color.END}{card_list}")
    print()
    typinginput(f"{color.DARKCYAN}Press Enter to continue...{color.END}")
    clear()


def show_played_cards(played_cards):
    if not played_cards:
        colourprint(f"{color.YELLOW}No cards have been played yet.{color.END}")
        return

    cards_display = ", ".join(
        [f"{color.YELLOW}{card}{color.END}" for card in played_cards])
    colourprint(f"{color.CYAN}Cards played so far:{color.END} {cards_display}")
    print()
    typinginput(f"{color.DARKCYAN}Press Enter to continue...{color.END}")
    clear()


def about():
    colourprint(f"{color.DARKCYAN}In-Sync Dev is a cooperative card game where players attempt to play cards in ascending order without communicating.{color.END}")
    colourprint(f"{color.RED}Watch tutorial: https://youtu.be/dQw4w9WgXcQ{color.END}")
    print()
    typinginput(f"{color.DARKCYAN}Press Enter to continue...{color.END}")
    clear()


def show_all_info(players, played_cards):
    players_list(players)
    show_cards(players)
    show_played_cards(played_cards)
    print()
    typinginput(f"{color.DARKCYAN}Press Enter to continue...{color.END}")
    clear()


def show_help():
    clear()
    colourprint(f"{color.GREEN}{color.BOLD}=== Available Dev Commands ==={color.END}")
    print()
    colourprint(
        f"{color.BLUE}!?players{color.END} - Show list of players and their card count"
    )
    colourprint(f"{color.BLUE}!?cards{color.END} - Show all players' cards")
    colourprint(
        f"{color.BLUE}!?played{color.END} - Show cards that have been played")
    colourprint(f"{color.BLUE}!?all{color.END} - Show all game information")
    colourprint(f"{color.BLUE}!?clear{color.END} - Clear the screen")
    colourprint(f"{color.BLUE}!?exit{color.END} - Exit the game")
    colourprint(f"{color.BLUE}!?about{color.END} - Show about the message")
    colourprint(f"{color.BLUE}!?help{color.END} - Show this help information")
    print()
    typinginput(f"{color.DARKCYAN}Press Enter to continue...{color.END}")
    clear()
