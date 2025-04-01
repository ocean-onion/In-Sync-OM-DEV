
# In Sync Game Development History

## Introduction
This document tracks the progress of "In Sync" card game implementation in Python, from initial drafts to the current implementation. Each version includes key changes and improvements, with a link to the complete code for each version.

## [The Game Concept](https://github.com/ocean-onion/In-Sync-OM-DEV/blob/main/docs/plan.md)

## Utils
### Logo printer (logo.py)
- Logo functions

### Developer commands (tools.py)
- Developer functions

### Utility functions (utilities.py)
- Styling functions
- Pacing functions
- Count down function

## Draft 1

### 0.1.0
---

#### Key improvements:

1. **Basic Game Mechanics:** Implemented core gameplay elements
2. **Player Creation:** Added functionality to create and manage players
3. **Card Dealing:** Implemented card distribution system
4. **Game Loop:** Created turn-based play system
5. **Card Validation:** Added basic validation for card plays
6. **Game Over Conditions:** Implemented win/loss detection

**Key Issues:**
- Players could see their own cards during gameplay
- Limited error handling
- No privacy between players when viewing cards

### Complete Code for Draft 1:

<details>
<summary>View Code</summary>

[Draft 1](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.1.*/draft1.py)

</details>

## Draft 2

### 0.1.1
---

#### Key improvements:

1. **Improved Input Validation:** Added stronger validation for user inputs with better error handling
2. **Fixed Game Over Logic:** Enhanced game over conditions to properly identify when the game ends 
3. **Error Message Improvements:** Added more detailed error messages for better user feedback
4. **Better Player Identification:** Improved logic to correctly identify which player should play the lowest card
5. **Code Structure:** More consistent organization of functions and game flow
6. **Restart Functionality:** Enhanced the restart game function for better user experience
7. **Conditional Statements:** Improved conditional logic for better control flow

### Complete Code for Draft 2:

<details>
<summary>View Code</summary>

[Draft 2](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.1.*/draft2.py)

</details>

## Draft 3

### 0.1.2
---

#### Key improvements:

1. **Player Privacy Implementation:** Added a 5-second wait timer before showing cards to ensure other players can look away
2. **Enhanced Card Viewing:** Improved the card viewing experience with clearer instructions
3. **Wait Functionality:** Implemented the wait() function for better timing control
4. **User Experience:** Added more descriptive messages for players to follow
5. **Privacy Prompts:** Clear prompts for players to ensure privacy when viewing cards
6. **Reduced Card Visibility:** Removed showing cards during turns to maintain game integrity
7. **Clearer Instructions:** Improved instructions for players about looking away during card viewing

### Complete Code for Draft 3:

<details>
<summary>View Code</summary>

[Draft 3](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.1.*/draft3.py)

</details>

## Draft 4

### 0.1.3
---

#### Key improvements:

1. **Added Helper Function:** Created `get_all_remaining_cards()` function to simplify code and improve readability
2. **Enhanced Input Validation:** Improved validation for card inputs, rejecting negative or zero values
3. **Code Documentation:** Added detailed comments to explain function purposes and logic
4. **Error Handling:** More robust error handling for user inputs
5. **Fixed Typos:** Corrected the "looking away" message and other minor text issues
6. **Improved Code Structure:** More logical organization of functions and cleaner code flow
7. **Input Validation Enhancement:** Added checks for negative numbers and non-digit inputs

### Complete Code for Draft 4:

<details>
<summary>View Code</summary>

[Draft 4](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.1.*/draft4.py)

</details>

## Draft 5

### 0.1.4
---

#### Key improvements:

1. **Player Count Validation:** Added validation to ensure between 2-4 players
2. **Enhanced Card Distribution:** Changed approach to card distribution with reserved cards
3. **Improved User Interface:** Added coloured text formatting with {YELLOW} and {END} markers
4. **Instructions Support:** Added option to view game instructions before starting
5. **Error Message Enhancement:** Better error messages for invalid player counts
6. **Player Name Feedback:** Added welcome message for each player
7. **Improved Card Memorization:** Better guidance for players to memorize or write down their cards
8. **Wait Time Implementation:** Added strategic wait times between game phases

### Complete Code for Draft 5:

<details>
<summary>View Code</summary>

[Draft 5](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.1.*/draft5.py)

</details>

## Draft 6 

### 0.2.0
---

#### Key improvements:

1. **Real-time Game System:** Fundamentally changed from turn-based to real-time play where any player can play at any time
2. **Card Sorting:** Added automatic sorting of player cards for easier management
3. **Previous Card Tracking:** Added tracking of previously played cards for reference
4. **Enhanced Player Interface:** Improved player identification with name input
5. **Player Selection:** Added ability for any player to make a move without fixed turn order
6. **Clearer Instructions:** Better instructions for real-time gameplay approach
7. **Game State Display:** Added display of previous card played
8. **Improved Clear Screen Usage:** Better use of clear screen for game flow

### Complete Code for Draft 6:

<details>
<summary>View Code</summary>

[Draft 6](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.2.*/draft6.py)

</details>

## Draft 7

### 0.2.1
---

#### Key improvements:

1. **Renamed Main Function:** Changed `start_game()` to `styled_start_game()` for better clarity
2. **Consistency in Naming:** Improved function naming consistency throughout code
3. **Minor Code Improvements:** Small optimizations and readability improvements
4. **Function Structure:** Better organization of function calls and sequences
5. **Improved Styling:** Enhanced text formatting approach
6. **Game Flow:** Smoother transitions between game phases

### Complete Code for Draft 7:

<details>
<summary>View Code</summary>

[Draft 7](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.2.*/draft7.py)

</details>

## Draft 8

### 0.2.2
---

#### Key improvements:

1. **Two Game Versions:** Split into separate plain and styled versions:
   - Plain version (`plaingame.py`): Focused on functionality with detailed comments
   - Styled version (`styledgame.py`): Enhanced with colour formatting for better experience
2. **colour Constants:** Added local colour constant definitions for easier maintenance
3. **Enhanced Card Display:** Improved card display with colour-coded player names
4. **Better Empty Name Handling:** Added validation to prevent empty player names
5. **Card Count Display:** Added display of remaining cards per player
6. **Code Organization:** Improved function organization with clearer responsibilities
7. **Better Error Messages:** Enhanced error messages with colour formatting
8. **Card History Visualization:** Better visualization of card play history

### Complete Code for Draft 8:

<details>
<summary>View Code</summary>

[Draft 8](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.2.*/draft8.py)

</details>

## Draft 9

### 0.2.3
---

#### Key improvements:

1. **Developer Commands:** Added `execute_dev_command()` function for game testing and debugging
2. **Extended Card Deck:** Increased available cards with random removal (15-45 cards removed)
3. **Countdown Function:** Replaced wait() with interactive countdown() function
4. **Development Tools:** Added support for developer commands prefixed with "!?"
5. **Card History Tracking:** Improved display of all played cards
6. **Better Visualization:** Enhanced card display with colour coding
7. **Command Processing:** Added ability to execute developer commands during gameplay
8. **Code Structure:** Better separation of game logic and utility functions
9. **Randomized Game Setup:** More variability in card distribution

### Complete Code for Draft 9:

<details>
<summary>View Code</summary>

[Draft 9](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.2.*/draft9.py)

</details>

## Draft 10 

### 0.3.0
---


#### Key improvements:

1. **Bug Fixes:** Fixed critical bugs, including the TypeError in the play_turn function where `players['name']` was incorrectly used instead of `player['name']`
2. **Improved Function Organization:** Broke down the game loop into smaller, more focused functions like `play_turn()`, `get_valid_player()`, and `get_valid_card()`
3. **Streamlined Game Flow:** Reorganized the game flow with clearer separation of responsibilities between functions
4. **Enhanced Input Handling:** Improved input validation with dedicated functions for getting valid player names and card selections
5. **Reduced Wait Time:** Decreased the wait time after player creation from 3 seconds to 0.5 seconds for a better gameplay experience
6. **Simplified Card History Display:** Simplified the card history display to show only when necessary rather than after every turn
7. **New Input Functions:** Added `colourinput` function instead of just `typinginput` for player interactions
8. **Cleaner Game Loop:** Completely refactored the main game loop with logic extracted into separate functions

### Complete Code for Draft 10:

<details>
<summary>View Code</summary>

[Draft 10](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.2.*/draft10.py)

</details>

## Draft 11

### 0.3.1
---

#### Key improvements:

1. **Refactored Developer Tools**: Moved developer commands from `utils.dev` to `utils.tools` module for better organization
2. **File Structure Improvement**: Reorganized utility functions into more appropriately named modules
3. **Code Maintainability**: Better separation of concerns with development tools in a dedicated module

### Complete Code for Draft 11

<details>
<summary>View Code</summary>

[Draft 11](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.3.*/draft11.py)

</details>

## Draft 12

### 0.3.2
---

#### Key improvements:

1. **Improved Game flow**: Created new function `typingprint_nl` to improve readabilty and speed of the gameplay
2. **Remove Developer Tools**: Removed vdeveloper tools from public game to clean it up a bit more

### Complete Code for Draft 12

<details>
<summary>View Code</summary>

[Draft 12](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.3.*/draft12.py)

</details>

## Draft 13

### 0.3.3
---

#### Key improvements:

1. **Improved Dev Tools**: Created new `about` function. Improved accessability of Dev commands through out the game
2. **Improved Game Flow**: Changed timing for different prompts

### Complete Code for Draft 13

<details>
<summary>View Code</summary>

[Draft 13](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.3.*/draft13.py)

</details>

## Draft 14

### 0.3.4
---

#### Key improvements:

1. **Improved Dev Tools**: Improved accessability of Dev commands through out the game
2. **Improved Game Flow**: Changed timing for different prompts
3. **Improved Game Start**: Added Better welcome and loading screens

### Complete Code for Draft 14

<details>
<summary>View Code</summary>

[Draft 14](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.3.*/draft14.py)

</details>

## Draft 15

### 0.4.0
---

#### Key improvements:

1. **Improved Game Flow**: Changed timing for different prompts, and removed unnecessary typing
2. **Improved Game Start**: Added Better welcome and loading screens and added an introduction function

### Complete Code for Draft 15

<details>
<summary>View Code</summary>

[Draft 15](https://github.com/ocean-onion/In-Sync-OM-DEV/tree/main/drafts/0.4.*/draft15.py)

</details>