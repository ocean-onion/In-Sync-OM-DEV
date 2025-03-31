
# Test Table

## Core Functions Tests

| Test ID | Test Description | Example Input | Expected Result | Actual Result |
|---------|------------------|---------------|-----------------|---------------|
| T01 | 2-4 player game | '3' | "Each player will get (random int) cards" | ```Each player will get {card_per_player} cards``` 
| T02 | Play invalid lowest card | '12' | "Wrong move! (player_name) played an incorrect card. Game over." | ```Wrong move! {player['name']} played an incorrect card. Game over.```  
| T03 | Game completion | (final_card) | Congratulations! You've successfully completed the game! | ```Congratulations! You've successfully completed the game!``` 
| T04 | Invalid player count | '7' | "Invalid input. Please enter a valid number of players between 2 and 4." | ```Invalid input. Please enter a valid number of players between 2 and 4``` 