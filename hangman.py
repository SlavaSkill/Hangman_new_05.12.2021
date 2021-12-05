from gameplay.game import Game
from scripts.split_difficulty import Dificulty
import random
import requests

# Player must choose a language of the words that will be guessed.
# Only LV or ENG are valid options, otherwise an error message will be printed.
while True:
    language = input("Please, choose language (LV/ENG) : ").upper()

    if language == "LV" or language == "ENG":
        break
    else:
        print("You can only choose LV or ENG")
        continue

# If LV option was selected, play the standard version of the game, which uses words.txt file.
if language == "LV":

    if_new_words = Dificulty()
    if_new_words.diff()
    
    print(
        "Hello! There are 3 difficulty levels:\n",
        "1st - without lenght marks and softening marks and more than 6 letters\n"
        "2nd - with lenght marks and softening marks and more than 6 letters\n"
        "3rd - with lenght marks and softening marks and less than 6 letters"   
    )
    
    # Select difficulty from 3 options - easy, medium, hard.
    # Depending on which option was selected, read the correct file.
    while True:
        difficulty = input("Please, chose your game difficulty level (easy/medium/hard) : ")
        if difficulty == 'easy':
            try:
                with open('data/easy_words.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    break
            except FileNotFoundError:
                print(f'File was not found. Please check the file and start again!')
                exit(1)
        elif difficulty == 'medium':
            try:
                with open('data/medium_words.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    break
            except FileNotFoundError:  
                print(f'File was not found. Please check the file and start again!')
                exit(1)
        elif difficulty == 'hard':
            try:
                with open('data/hard_words.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    break
            except FileNotFoundError:
                print(f'File was not found. Please check the file and start again!')
                exit(1)
        else:
            print("Invalid input!")
            continue

    # Get words for selected difficulty.
    words = list(file_contents.split("\n"))
    random.shuffle(words)

    # Start the game.
    while True:
        word = words.pop()
        
        game = Game(word)
        game.play()
        
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again == "y": 
            continue
        else: 
            break

# If ENG option is selected, get words in english from API.
elif language == "ENG" :
    
    url = 'https://random-word-api.herokuapp.com/word?number=1'
    
    while True:
        response = requests.get(url)
        json_response = response.json()
        word = json_response[0].upper()
        
        game = Game(word)
        game.play()
        
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again == "y": 
            continue
        else: 
            break
