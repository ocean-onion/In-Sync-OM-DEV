from utilities import typingprint, typinginput, cards, random, clear, wait

def prepare_game_deck(num_players, desired_cards_per_player=8):
    total_cards_needed = num_players * desired_cards_per_player
    if total_cards_needed > len(cards):
        cards_per_player = len(cards) // num_players
        total_cards_needed = num_players * cards_per_player
        typingprint(f"Not enough cards for {desired_cards_per_player} each. Using {cards_per_player} cards per player instead.")
    else:
        cards_per_player = desired_cards_per_player
    deck = cards.copy()
    random.shuffle(deck)
    game_deck = deck[:total_cards_needed]
    return game_deck, cards_per_player

def create_players(num_players):
    players = []
    for i in range(num_players):
        name = typinginput(f"Enter name for player {i+1}: ")
        players.append({"name": name, "deck": []})
    return players

def deal_cards(game_deck, players, cards_per_player):
    for i in range(cards_per_player):
        for player in players:
            if game_deck:
                card = game_deck.pop(0)
                player["deck"].append(card)

def show_cards(player):
    typingprint(f"{player['name']}, I will show your cards in 5 seconds.")
    typingprint("Make sure all other players are look away!")
    wait(5)
    typingprint(f"{player['name']}, please view your cards:")
    print(player['deck'])
    typinginput("Press Enter when you've memorized your cards...")
    clear()

def check_user_deck(player, card):
    if card in player["deck"]:
        return True
    else:
        typingprint("You do not have that card!")
        return False

def check_lowest_possible(players, played_card):
    remaining_cards = []
    for player in players:
        remaining_cards.extend(player["deck"])
    if not remaining_cards:
        return True
    lowest_remaining = min(remaining_cards)
    return played_card == lowest_remaining

def play_card(player, card):
    player["deck"].remove(card)
    typingprint(f"{player['name']} has successfully played the card {card}.")

def game_loop(players):
    while True:
        if all(len(player["deck"]) == 0 for player in players):
            typingprint("Congratulations! You've successfully completed the game!")
            break
        for player in players:
            typingprint(f"{player['name']}'s turn.")
            chosen_card_input = typinginput("Choose a card to play: ")
            if not chosen_card_input.isdigit():
                typingprint("Please enter a valid number.")
                continue
            chosen_card = int(chosen_card_input)
            if not check_user_deck(player, chosen_card):
                continue
            if check_lowest_possible(players, chosen_card):
                play_card(player, chosen_card)
                typingprint(f"{player['name']} played {chosen_card} successfully!")
            else:
                remaining_cards = []
                for p in players:
                    remaining_cards.extend(p["deck"])
                lowest_card = min(remaining_cards)
                correct_player = None
                for p in players:
                    if lowest_card in p["deck"]:
                        correct_player = p["name"]
                        break
                typingprint(f"Wrong move! {player['name']} played an incorrect card. Game over.")
                typingprint(f"The correct card to play was {lowest_card}, and it should have been played by {correct_player}.")
                return

def restart_game():
    answer = typinginput("Do you want to play again? (y/n): ").lower()
    if answer == "y":
        start_game()
    else:
        typingprint("Thanks for playing!")

def start_game():
    clear()
    typingprint("Welcome to The Mind!")
    num_players_input = typinginput("Enter the number of players: ")
    if num_players_input.isdigit():
        num_players = int(num_players_input)
    else:
        typingprint("Invalid input. Defaulting to 2 players.")
        num_players = 2
    game_deck, cards_per_player = prepare_game_deck(num_players, desired_cards_per_player=8)
    players = create_players(num_players)
    deal_cards(game_deck, players, cards_per_player)
    for player in players:
        show_cards(player)
    typinginput("Are you ready to begin? Press Enter to start the game...")
    game_loop(players)
    restart_game()

if __name__ == '__main__':
    start_game()
