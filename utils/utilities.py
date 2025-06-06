import time
import sys
import os


class color:
    # Colours
    BLUE = '\033[94m'        
    CYAN = '\033[96m'        
    GREEN = '\033[92m'       
    PURPLE = '\033[95m'      
    RED = '\033[91m'        
    YELLOW = '\033[93m'     

    # Dark Colours
    DARKBLUE = "\033[38;5;27m"  
    DARKCYAN = '\033[36m'        
    DARKPURPLE = "\033[38;5;54m" 

    # Accents
    BOLD = '\033[1m'            
    UNDERLINE = '\033[4m'        
    END = '\033[0m'             


_color_patterns = {}
_color_dict = {
    # Colours
    'BLUE': color.BLUE,
    'CYAN': color.CYAN,
    'GREEN': color.GREEN,
    'PURPLE': color.PURPLE,
    'RED': color.RED,
    'YELLOW': color.YELLOW,
    
    # Dark Colours
    'DARKBLUE': color.DARKBLUE,
    'DARKCYAN': color.DARKCYAN,
    'DARKPURPLE': color.DARKPURPLE,
    
    # Accents
    'BOLD': color.BOLD,          
    'UNDERLINE': color.UNDERLINE, 
    'END': color.END,
}


def apply_colors(text):
    for color_name, color_code in _color_dict.items():
        pattern = '{' + color_name + '}'
        if pattern in text:
            text = text.replace(pattern, color_code)
    return text + color.END


cards = list(range(1, 71))
lowest_card_playable = 1

_is_posix = os.name == 'posix'


def clear():
    os.system('clear' if _is_posix else 'cls')


def wait(seconds):
    time.sleep(seconds)

'''The functions with _nl mean that the function will not print a new line at the end of the function. Which can be used to make the different text statements appear on the same line.''' # remove in public

def typingprint(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
def typingprint_nl(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def colourprint(text):
    text = apply_colors(text)
    print(text)
    print()

def colourprint_nl(text):
    text = apply_colors(text)
    print(text)

def typinginput(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    return input()

def colourinput(text):
    text = apply_colors(text)
    return input(text)

def typingintructions(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


def countdown(seconds):
    ascii_numbers = {
        1:
        """░░███╗░░
░████║░░
██╔██║░░
╚═╝██║░░
███████╗
╚══════╝""",
        2:
        """██████╗░
╚════██╗
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝""",
        3:
        """██████╗░
╚════██╗
░█████╔╝
░╚═══██╗
██████╔╝
╚═════╝░""",
        4:
        """░░██╗██╗
░██╔╝██║
██╔╝░██║
███████║
╚════██║
░░░░░╚═╝""",
        5:
        """███████╗
██╔════╝
██████╗░
╚════██╗
██████╔╝
╚═════╝░""",
        6:
        """░█████╗░
██╔═══╝░
██████╗░
██╔══██╗
╚█████╔╝
░╚════╝░""",
        7:
        """███████╗
╚════██║
░░░░██╔╝
░░░██╔╝░
░░██╔╝░░
░░╚═╝░░░""",
        8:
        """░█████╗░
██╔══██╗
╚█████╔╝
██╔══██╗
╚█████╔╝
░╚════╝░""",
        9:
        """░█████╗░
██╔══██╗
╚██████║
░╚═══██║
░█████╔╝
░╚════╝░""",
        10:
        """░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░██║░░██║
╚═╝██║░░██║░░██║
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        11:
        """░░███╗░░░░███╗░░
░████║░░░████║░░
██╔██║░░██╔██║░░
╚═╝██║░░╚═╝██║░░
███████╗███████╗
╚══════╝╚══════╝""",
        12:
        """░░███╗░░██████╗░
░████║░░╚════██╗
██╔██║░░░░███╔═╝
╚═╝██║░░██╔══╝░░
███████╗███████╗
╚══════╝╚══════╝""",
        13:
        """░░███╗░░██████╗░
░████║░░╚════██╗
██╔██║░░░█████╔╝
╚═╝██║░░░╚═══██╗
███████╗██████╔╝
╚══════╝╚═════╝░""",
        14:
        """░░███╗░░░░██╗██╗
░████║░░░██╔╝██║
██╔██║░░██╔╝░██║
╚═╝██║░░███████║
███████╗╚════██║
╚══════╝░░░░░╚═╝""",
        15:
        """░░███╗░░███████╗
░████║░░██╔════╝
██╔██║░░██████╗░
╚═╝██║░░╚════██╗
███████╗██████╔╝
╚══════╝╚═════╝░""",
        16:
        """░░███╗░░░█████╗░
░████║░░██╔═══╝░
██╔██║░░██████╗░
╚═╝██║░░██╔══██╗
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        17:
        """░░███╗░░███████╗
░████║░░╚════██║
██╔██║░░░░░░██╔╝
╚═╝██║░░░░░██╔╝░
███████╗░░██╔╝░░
╚══════╝░░╚═╝░░░""",
        18:
        """░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░╚█████╔╝
╚═╝██║░░██╔══██╗
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        19:
        """░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░╚██████║
╚═╝██║░░░╚═══██║
███████╗░█████╔╝
╚══════╝░╚════╝░""",
        20:
        """██████╗░░█████╗░
╚════██╗██╔══██╗
░░███╔═╝██║░░██║
██╔══╝░░██║░░██║
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        21:
        """██████╗░░░███╗░░
╚════██╗░████║░░
░░███╔═╝██╔██║░░
██╔══╝░░╚═╝██║░░
███████╗███████╗
╚══════╝╚══════╝""",
        22:
        """██████╗░██████╗░
╚════██╗╚════██╗
░░███╔═╝░░███╔═╝
██╔══╝░░██╔══╝░░
███████╗███████╗
╚══════╝╚══════╝""",
        23:
        """██████╗░██████╗░
╚════██╗╚════██╗
░░███╔═╝░█████╔╝
██╔══╝░░░╚═══██╗
███████╗██████╔╝
╚══════╝╚═════╝░""",
        24:
        """██████╗░░░██╗██╗
╚════██╗░██╔╝██║
░░███╔═╝██╔╝░██║
██╔══╝░░███████║
███████╗╚════██║
╚══════╝░░░░░╚═╝""",
        25:
        """██████╗░███████╗
╚════██╗██╔════╝
░░███╔═╝██████╗░
██╔══╝░░╚════██╗
███████╗██████╔╝
╚══════╝╚═════╝░"""
    }

    for i in range(seconds, 0, -1):
        clear()
        if i <= 25 and i in ascii_numbers:
            colourprint(f"{color.RED}{ascii_numbers[i]}{color.END}")
        wait(1)
    clear()

acceptabled = ["doom", "mfdoom", "onebeer", "rapper", "mm..food", "mmfood", "doomsday", "allcap", "madvillian", "supervillian", "kinggeedorah", "viktorvaughn", "kmd", "dangerdoom", "mfgrim"] # Remove in public

acceptableuk = ["knucks", "knuckles", "knuckle", "alphahouse", "alphahouse", "badman", "boybetterknow", "bbk", "sketpa", "jme", "wasteman", "toomanyman", "atum", "dave", "aj", "ajtracey", "shutdown", "sainte", "rushy"] # Remove in public

acceptablel = ["liam", "mackenzie", "lmackenzie", "cs", "cscience", "computerscience"] # Remove in public

def instructions():
    wait(0.05)
    clear()
    typingprint(f"{color.DARKBLUE}{color.BOLD}Game Instructions:")
    typingintructions(
        f"{color.BLUE} 1. {color.END}{color.CYAN}Each player receives a set of randomly numbered cards.{color.END}"
    )
    typingintructions(
        f"{color.BLUE} 2. {color.END}{color.CYAN}The goal is to play the cards in ascending order without speaking."
    )
    typingintructions(
        f"{color.BLUE} 3. {color.END}{color.CYAN}Players must rely on intuition and teamwork to decide when to play.{color.END}"
    )
    typingintructions(
        f"{color.BLUE} 4. {color.END}{color.CYAN}If a player plays a card out of order, the game ends.{color.END}"
    )
    typingintructions(
        f"{color.BLUE} 5. {color.END}{color.CYAN}If all cards are played in the correct order, you win!{color.END}"
    )
    typingprint(f"{color.DARKBLUE}{color.BOLD}\n Tips:{color.END}")
    typingintructions(
        f"{color.BLUE}  - {color.END}{color.CYAN}{color.UNDERLINE}Stay focused and try to sense the right timing.{color.END}"
    )
    typingintructions(
        f"{color.BLUE}  - {color.END}{color.CYAN}{color.UNDERLINE}If unsure, wait a moment before playing a card.{color.END}"
    )
    typinginput(f"{color.BLUE}\nPress Enter to continue...{color.END}")
    clear()
    return


def plain_instructions():
    print("Game Instructions:")
    print("1. Each player receives a set of randomly numbered cards.")
    print(
        "2. The goal is to play the cards in ascending order without speaking."
    )
    print(
        "3. Players must rely on intuition and teamwork to decide when to play."
    )
    print("4. If a player plays a card out of order, the game ends.")
    print("5. If all cards are played in the correct order, you win!")
    print("\nTips:")
    print("- Stay focused and try to sense the right timing.")
    print("- If unsure, wait a moment before playing a card.")
    input("\nPress Enter to continue...")
    return

'''These functions put these print statements in a for loop to create a loading screen effect.''' # remove in public
    
def loading_screen():
    for i in range(1, 4):
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game.{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game..{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Game...{color.END}")
        wait(0.5)
        clear()

def shuffle_screen():
    for i in range(1, 4):
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Shuffling Cards{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Shuffling Cards.{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Shuffling Cards..{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Shuffling Cards...{color.END}")
        wait(0.5)
        clear()

def loading_files_screen():
    for i in range(1, 4):
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Files{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Files.{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Files..{color.END}")
        wait(0.5)
        clear()
        colourprint_nl(f"{color.BLUE}{color.BOLD}Loading Files...{color.END}")
        wait(0.5)
        clear()

