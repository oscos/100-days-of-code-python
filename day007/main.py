
"""

Created: 04/1/2024
Updated:
Udemy - 100 Days of Code: The Complete Python Pro Bootcamp By Angela Yu
Day 7 - Hangman

Instructions:

Solution:

"""

import random

# artwork from: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
WORDS = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').upper().split()

# WORDS = ('doggie ').upper().split()
# print(WORDS)

ALPHABET = list(map(chr, range(ord('A'), ord('Z') + 1)))
# print(ALPHABET)

user_input_letter_list = []


def get_hangman_pic(number_of_attempts):

    return HANGMANPICS[number_of_attempts]


def pick_random_word():

    return random.sample(WORDS,1)[0].upper()


def encrypt_word(random_word, selected_letters):
    result = ''

    for j in random_word:
        if j in selected_letters:
            result += j # .upper()
        else:
            result += '_'

    return result


def is_letter_previously_chosen(letter, letter_list):
    if letter in letter_list:
        return True
    return False

def is_letter_found(letter, letter_set):
    if letter in letter_set:
        return True
    return False

def is_letter_invalid(letter):
    if letter in ALPHABET:
        return False
    return True

# def find_letter_match_set(letter_set, letter_list):
#     letters_only_in_set = letter_set.intersection(letter_list)
#     return letters_only_in_set

def calc_remaining_attempts(max_wrong_attempts, wrong_attempts):
    result = max_wrong_attempts - wrong_attempts
    return result

# Write Program Here:
print("Welcome to the famous Hangman Game!")
print("")

random_word = pick_random_word()
# print(f"random_word: {random_word}")

random_letter_set = set(sorted(random_word))
# print(f"random_word_letter_set: {random_letter_set}")

encrypted_word = encrypt_word(random_word, user_input_letter_list)
print(f"Encrypted Word: {encrypted_word}")


incorrect_attempt_count = 0
correct_attempt_count = 0
max_incorrect_attempt_count = len(HANGMANPICS)

while incorrect_attempt_count < max_incorrect_attempt_count:

    user_input_letter = input("Pick a letter from the alphabet (case insensitive): ").upper()
    print(user_input_letter)

    if is_letter_invalid(user_input_letter):
        print(f"You selected an invalid character: {user_input_letter}")
        print("Please try again.")
        print("")
        continue

    if is_letter_previously_chosen(user_input_letter, user_input_letter_list):
        print(f"You previously selected this letter: {user_input_letter_list}")
        print("Please try again.")
        print("")
        continue

    if is_letter_found(user_input_letter, random_letter_set):
        print(f"Correct guess! The letter {user_input_letter} is found within the random word.")
        print("")
        correct_attempt_count += 1

        if correct_attempt_count == len(random_letter_set):
            print(f"You win! The random word was {random_word}")
            break
    else:
        print(f"Incorrect guess! The letter {user_input_letter} is NOT found within the random word.")
        print(get_hangman_pic(incorrect_attempt_count))
        print("")
        incorrect_attempt_count += 1

        if incorrect_attempt_count == max_incorrect_attempt_count:
            print(f"You lose! The random word was {random_word}")
            break

    user_input_letter_list.append(user_input_letter)
    # print(f"Previously Selected Letters: {user_input_letter_list}")

    encrypted_word = encrypt_word(random_word, user_input_letter_list)
    print(f"Encrypted Word: {encrypted_word}")

    remaining_attempt_count = calc_remaining_attempts(max_incorrect_attempt_count, incorrect_attempt_count)
    print(f"Number of Remaining Attempts: {remaining_attempt_count}")
