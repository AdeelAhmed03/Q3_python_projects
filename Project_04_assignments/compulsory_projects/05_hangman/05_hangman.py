import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # Get a random word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) # If the word contains a hyphen or space, get another word
        return word
    
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_uppercase) # Set of all lowercase letters
    used_letters = set() # Letters guessed by the user

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) => 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (i.e. W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() # Convert user input to uppercase
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) # Add the letter to the set of used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1 
                print('Letter is not in word. ')

        elif user_letter in used_letters:
            print('You have already used that letter. Please Try again.')
        else:
            print('Invalid character. Please try again.')

# gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died. Sorry. The word was', word) # User ran out of lives
    else:
        print('Congratulations! You guessed the word!', word, '!!') # User guessed the word correctly

hangman()


user_input = input("Guess a letter: ") # Get user input and convert to uppercase
print(user_input)