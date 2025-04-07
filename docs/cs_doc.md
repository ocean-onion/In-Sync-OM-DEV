
# In Sync Game - Project Plan
### *****All files in this file are required for the game to run properly*****

## 1. Project Pitch

### Game Idea
"In Sync" is a cooperative card game where players work together to play their cards in ascending order, without communicating. Each player is handed cards with numbers ranging from 1 to 70. Before the game begins, a random selection of cards is removed from the deck, making it impossible to know exactly which numbers are in play. Players must rely on intuition and timing to play their cards in the correct order without discussing their hands or giving any hints.

### Rules
1. Players are dealt cards from a deck numbered 1-70 (with some cards randomly removed)
2. Players must play their cards in ascending order
3. No communication allowed between players about their cards
4. If a card is played out of order, the game ends
5. If all cards are played in the correct order, players win

### Objective
Successfully play all cards in ascending numerical order without talking.

### Core Features
- Create and shuffle a deck of cards (1-70) with random cards removed
- Deal cards to 2-4 players
- Allow players to play cards in real-time (any player can play at any time)
- Check if cards are played in the correct order
- Track played cards
- Determine win/loss conditions
- Privacy mechanisms for viewing cards with a countdown
- Colour-coded messages and styling
- Developer commands for testing and debugging

### Stretch Goals
- Team mode
- Add difficulty levels with more cards
- Implement a system where teams have lives mistakes are allowed but if a mistake is make a life is subtracted at the end
- Add a scoring system
- Create visual cards
- Blind mode (no confirmation of card values)
- Speed mode (time limit for decisions)

## 2. Timeline

### Project Timeline (Mar 10 - Apr 7) (Based on Gantt Chart - some finals details have differed from plans)

- ***Week 5**:
   - Game Planning (Finished)
   - Core Mechanics (Finished)
   - Game Structure (Finished)
   - Utility Functions (Finished)
   - Pseudocode Creation (Finished)
   - Player Setup (Finished)
   - Start Deck Management

- **Week 6**:
   - Deck Management (Finished)
   - Card Distribution (Finished)
   - Turn System (Changed to real-time system)
   - Start Game Validation

- **Week 7**:
   - Game Validation (Finished)
   - Testing & Debugging (Finished)

- **Week 8**:
   - Game Optimization (Finished)
   - Final Refinements (Finished)
   - Playtesting (Finished)
   - Project Submission (Finished)
   - Debugging (Finished)
   - Start Game Flow testing

- **Week 9**:
   - Game Flow testing (Finished)
   - Submissions (Finished)

## 3. Design

### Main Functions

1. **styled_start_game()**: Initialize the game, get player count, create deck
2. **create_players(num_players)**: Create player objects with names and empty hands
3. **prepare_game_deck(num_players)**: Create and shuffle deck, determine cards per player
4. **deal_cards(deck, players, cards_per_player)**: Distribute cards to players
5. **game_loop(players)**: Main game loop handling real-time play and win/loss conditions
6. **check_lowest_possible(players, card)**: Check if played card is the lowest in all hands
7. **play_card(player, card)**: Remove card from player's hand and add to played cards
8. **find_correct_player(players, card)**: Find which player has a specific card
9. **get_all_remaining_cards(players)**: Get all cards remaining in players' hands
10. **show_cards(player)**: Display a player's cards with privacy controls
11. **play_turn()**: Processes a player's turn, validates the move, and updates or ends the game

## 4. Development

The game has been implemented in Python with the following structure:

1. **Main Game Versions**:
   - Plain text version (plaingame.py)
   - Styled version with colours (styledgame.py)

2. **Utility Functions**:
   - Text styling and formatting
   - Timing controls (countdown, typing effects)
   - Screen clearing
   - Developer commands

3. **Game Evolution**:
   - Started with a basic turn-based system
   - Changed to real-time play, where any player can make a move
   - Added privacy features with countdowns
   - Enhanced with card history tracking
   - Implemented developer commands for testing
   - Rebranded Game to own original naming

4. **Current Features**:
   - Real-time gameplay
   - Privacy mechanisms when viewing cards
   - Card history display
   - colour-coded messages
   - Developer mode for testing
   - Extended card deck with random removal

## 5. Tests

Plan:
1. Unit test each function individually (**Finished**)
2. Integration test combinations of functions (**Finished**)
3. Full game testing with different player counts (**Finished**)
4. User testing with actual players (**Finished**)

Actual:
- The tests went smoothly for the most part. There were some issues with circular imports when trying to route instructions in ```utilities``` back to the ```styledgame```, which was an interesting challenge to solve.

## 6. Evaluation

1. **What worked well?**
- Creating the players and dealing the cards worked well. Once I organized the code more clearly, the game started to make more sense. The real-time gameplay also worked well in the end, especially after I separated things better.

2. **What was challenging?**
- One of the biggest challenges was checking for the correct cards and players. It made the code messy and hard to understand at first, but I was able to organise it better eventually by splitting it up more. Making the real-time gameplay was also difficult at the beginning.

3. **Did you follow your plan successfully?**
- I didn’t follow my plan completely. I realized that my game wouldn’t work in a turn-based format, which led me to completely overhaul a lot of the game. This was because my game relies heavily on the idea that some people have the two next-lowest cards, which is meant to confuse the players and raise the stakes. Switching to real-time gameplay, where users can play their cards whenever they want, worked much better.

4. **What would you do differently if you started over?**
- If I started over, I would do user testing earlier. I would also add more comments in the code to help myself stay on track, because I often found myself getting lost in it.

5. **How confident are you now with functions and lists?**
- I now feel confident using lists and functions, as I used them somewhat effectively in my program. There’s still room for improvement in my code, but I’m happy with where it is now compared to where it started.


## 8. Tools Required

- Python 3.11
- Built-in Python libraries:
  - random (for shuffling)
  - time (for typing effect and countdown)
  - sys (for display functions)
  - os (for clearing the screen)

## 9. Documentation
- [Full Documents Folder](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/docs)
- [Overview](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/README.md)
- [Fixes](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/fixes/fixes.md)
- [Game Development](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/game_development.md)
- [Gantt Chart](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/gantt_chart.md)
- [Pseudocode](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/pseudocode.md)
- [Project Structure](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/structure.md)
- [Test Table](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/test_table.md)

## 10. License
- [MIT License](https://github.com/ocean-onion/In-Sync-OM/blob/main/LICENSE)