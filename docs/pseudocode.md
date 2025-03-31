#### Function: check_lowest_possible(players, card)
```
START
  FUNCTION check_lowest_possible(players, card)
    remaining_cards = get_all_remaining_cards(players)
    IF remaining_cards is empty THEN
      RETURN True
    END IF
    lowest_card = minimum value in remaining_cards
    RETURN card equals lowest_card
  END FUNCTION
END
```

#### Function: game_loop(players)
```
START
  FUNCTION game_loop(players)
    previous_card = 0
    played_cards = []

    WHILE True
      IF all players have empty hands THEN
        OUTPUT "Congratulations! Game completed successfully!"
        BREAK
      END IF

      OUTPUT "Anyone can play a card at any time."
      INPUT player_name

      IF player_name starts with "!?" THEN
        execute_dev_command(player_name, players, played_cards)
        CONTINUE
      END IF

      player = get_valid_player(players, player_name)
      IF player is None THEN
        CONTINUE
      END IF

      card = get_valid_card(player)
      IF card is None THEN
        CONTINUE
      END IF

      IF check_lowest_possible(players, card) THEN
        play_card(player, card)
        previous_card = card
        played_cards.append(card)
        OUTPUT successful play message
      ELSE
        remaining_cards = get_all_remaining_cards(players)
        lowest_card = minimum value in remaining_cards
        correct_player = find_correct_player(players, lowest_card)
        OUTPUT game over message
        OUTPUT correct card information
        RETURN
      END IF
    END WHILE
  END FUNCTION
END
```