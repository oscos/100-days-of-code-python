rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#### PEDAC
"""
| Objective            | Step                 | Description                               |
|----------------------|----------------------|-------------------------------------------|
| Process the Problem  | Understand the       | - Identify expected input and output      |
|                      | Problem              | - Make the requirements explicit          |
|                      |                      | - Identify rules                          |
|                      |                      | - Mental model of the problem (optional)  |
|                      |                      |                                           |
|                      | Examples/Test Case   | Validate understanding of the problem     |
|                      |                      |                                           |
|                      | Data Structure       | How we represent data that we will work   |
|                      |                      | with when converting the input to output. |
|                      |                      |                                           |
|                      | Algorithm            | Steps for converting input to output      |
|                      |                      |                                           |
| Code with Intent     | Code                 | Implementation of Algorithm               |
|                      |                      |                                           |

Problem: Create a Rock Paper Scissors Game
  - Input: String
    - Player will be asked to enter a selection
  - Output: String
    - Message indicating who won
Rules:
  - Two Players can only play at a time
  - Players have only 3 options to choose from: rock, paper, scissors
  - Winning
    - Paper beats Rock
    - Rock beats Scissors
    - Scissors beats Paper
  - Tie
    player1 options matches player2 option
  - Lose
    -Not Winning or Tie
Examples:
  Player 1 rock, Player 2 rock => Tied
  Player 1 rock, Player 2 scissors => Player1 Wins
  Player 2 rock, Player 2 paper = Player1 loses
  
Mental MOdel:
  Player1 and Player 2 each chose from one of three options: rock, paper, scissors
  Winner is selected based on Winning Rules
Data Structure: List, Dictionary
  - List to Hold Options
  - Dictionary to Hold Winning Rules
Algorithm:
  - Player1 is asked to select between: rock, paper, scissors
    - if entry is not one of the selected items, output message, "Invalid Entry"
  - Player2 randomly generates a selection between the three items
  - Use the selection from Player 1 to retrieve the corresponding winning pair
    to compare against to determine who wins
    - If player1 selection matches player1 selection:
      output message: "You Tied!"
    - If player1 selection matches first item and player2 matches second item,
      output message, "You win!"
      else: "You lose!"
  # - Ask the player if they would like to play again
  #   - if yes, restart game
  #     else: output message, "Thanks for playing"
Code with Intent
"""

import random

OPTIONS = ['rock', 'paper', 'scissors']
WINNER_RULES = [['paper','rock'],['rock','scissors'],['scissors','paper']]

player1_choice = input("chose from one of three options: rock, paper, scissors:\n").lower()
player2_choice = OPTIONS[random.randint(0,2)]


if OPTIONS.count(player1_choice) > 0:
  print(player2_choice)
  if player1_choice == player2_choice:
    print("You Tied")
  elif (
    (WINNER_RULES[0][0] == player1_choice and WINNER_RULES[0][1] == player2_choice) or
    (WINNER_RULES[1][0] == player1_choice and WINNER_RULES[1][1] == player2_choice) or
    (WINNER_RULES[2][0] == player1_choice and WINNER_RULES[2][1] == player2_choice)
  ):
    print("You Win!")
  else:
    print("You lose!")
else:
  print("Invalid Entry")

