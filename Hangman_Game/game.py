import random
import string
from words import words
from visual import lives_visual_dict

def get_valid_word(words):
    word= random.choice(words)
    while " "in word or "-" in word:
        word= random.choice(words)

    return word.upper()

def main_game():
    print("************************Welcome to Hangman Game************************")
    print("Guess the word correctly to win")
    word= get_valid_word(words)
    word_letters= set(word)
    alphabets= set(string.ascii_uppercase) # Return all uppercase letters
    used_letter= set()
    lives= 10

    while len(word_letters) >0 and lives>0:
        if len(used_letter)>0:
            print("You have used these letters: ", " ".join(sorted(used_letter))) #shows the user what letters already been used

        word_list= [letter if letter in used_letter else '_' for letter in word] # shows the progress
        print("final_word: ", "".join(word_list))

        user_input= input("Guess a letter: ").upper().strip()
        if user_input in alphabets - used_letter:
            used_letter.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives= lives-1
                print(f'You have {lives} attempt left')
                print(lives_visual_dict[lives])
        elif user_input in used_letter:
            print("You have already used that letter! Try a different one.")
        else:
            print("Invalid input! Please Try again.")
        
    #word_list= [letter if letter in used_letter else '_' for letter in word] # shows the progress
    if lives<=0:
        print("You have lost!")
    else:
        print("You have Won!")
    print("final_word: ", word)

main_game()
