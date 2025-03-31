import random
from utilities import typingprint, typinginput, cards, clear, wait, instructions


def prepare_game_deck(num_players):
    total_cards = len(cards)
    cards_to_remove = 8
    available_cards = total_cards - cards_to_remove

    cards_per_player = max(1, available_cards // num_players)

    typingprint(f"Each player will get {cards_per_player}, cards.")

    deck = cards.copy()
    random.shuffle(deck)

    removed_cards = random.sample(deck, cards_to_remove)
    for card in removed_cards:
        deck.remove(card)

    game_deck = deck[:available_cards]

    return game_deck, cards_per_player


def create_players(num_players):
    players = []
    for i in range(num_players):
        name = typinginput(f"Enter the name of Player {i + 1}: ")
        players.append({"name": name, "deck": []})
    return players


def deal_cards(game_deck, players, card_per_player):
    for i in range(card_per_player):
        for player in players:
            if game_deck:
                card = game_deck.pop(0)
                player["deck"].append(card)
                player["deck"].sort()


def show_cards(player):
    typingprint(f"{player['name']}, I will show your cards in 5 seconds.")
    typingprint("Make sure all other players are looking away!")
    wait(5)
    typingprint(
        f"{player['name']}, Please view your cards. It may be useful to write them down on some paper."
    )
    print(player['deck'])
    typinginput("Press Enter/Return when you have memorised your cards.")
    clear()


def check_user_deck(player, card):
    if card in player["deck"]:
        return True

    else:
        typingprint("You do not have that card!")
        return False


def get_all_remaining_cards(players):
    return [card for player in players for card in player["deck"]]


def check_lowest_possible(players, played_card):
    remaining_cards = get_all_remaining_cards(players)
    if not remaining_cards:
        return True
    lowest_remaining = min(remaining_cards)
    return played_card == lowest_remaining


def play_card(player, card):
    player["deck"].remove(card)
    typingprint(f"{player['name']} has successfully played the card {card}.")
    return card


def game_loop(players):
    previous_card = None

    while True:
        if all(len(player["deck"]) == 0 for player in players):
            typingprint("Congratulations! You've successfully completed the game!")
            break

        if previous_card is not None:
            typingprint(f"Previous card played was: {previous_card}")
        else:
            typingprint("No cards have been played yet.")

        typingprint("Anyone can play a card at any time.")


        chosen_user = typinginput("Enter your name: ")
        chosen_card_input = typinginput("Choose a card to play: ")

        if not chosen_card_input.isdigit():
            typingprint("Please enter a valid card number!")
            continue
        chosen_card = int(chosen_card_input)

        player_found = False
        for player in players:
            if player["name"].lower() == chosen_user.lower():
                player_found = True
                if check_user_deck(player, chosen_card):
                    previous_card = play_card(player, chosen_card)
                    if check_lowest_possible(players, chosen_card):
                        typingprint(f"{player['name']} played {chosen_card} successfully!")

                    else:
                        remaining_cards = get_all_remaining_cards(players)
                        lowest_card = min(remaining_cards)
                        correct_player = "Unknown"
                        for p in players:
                            if lowest_card in p["deck"]:
                                correct_player = p["name"]
                                break
                        typingprint(f"Wrong move! {player['name']} played an incorrect card. Game over.")
                        typingprint(f"The correct card to play was {lowest_card}, and it should have been played by {correct_player}.")
                        return
                break

        if not player_found:
            typingprint("Player name not found. Please enter a valid name.")



def restart_game():
    answer = typinginput("Do you want to play again? (y/n): ").lower()
    if answer == "y":
        styled_start_game()  # Restart the game
    else:
        typingprint("Thanks for playing!")


def styled_start_game():
    clear()
    typingprint("{YELLOW}Welcome to The Mind{END}")
    typingprint("A card game made into a video game.")
    int_ask = typinginput("Would you like the instructions? (y/n): ").lower()

    if int_ask == "y":
        instructions()  # Show instructions
    clear()
    typingprint("Okay, let's start the game!")
    wait(1)  # Pause before game begins

    while True:
        num_players_input = typinginput(
            "Enter the number of players (between 2 and 4): ")
        if not num_players_input.isdigit() or not (2 <= int(num_players_input)
                                                   <= 4):
            typingprint(
                "Invalid input. Please enter a valid number of players between 2 and 4."
            )
        else:
            num_players = int(num_players_input)
            break

    game_deck, cards_per_player = prepare_game_deck(num_players)
    players = create_players(num_players)
    deal_cards(game_deck, players, cards_per_player)

    for player in players:
        show_cards(player)

    typinginput("Are you ready to begin? Press Enter to start the game...")
    game_loop(players)
    restart_game()


if __name__ == '__main__':
    styled_start_game()