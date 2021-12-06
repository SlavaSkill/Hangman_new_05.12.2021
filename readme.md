# Hangman

Hangman is a word guessing game written in Python. For ENG version random word API is used. 

## Initating

To start the game open hangman.py file.


## Required files

- data\words.txt
- gameplay\game.py
- scripts\split_difficulity.py
- hangman.py
- requirements.txt


## Game process, rules

Choose to play game in LV or ENG.
Chose you difficulty level. Game in ENG has only one difficulty level, but game in LV has 3 difficulty levels.
If you will chose ENG version of the game, you will be able to chose amount of rounds you want to play.
Enter your name.
After you entered name, game starts. 

On start you will see:
1.Picture of ground where will be gallows.
2.Hidden word.
3.Word lenght.
4.Amount of your lives.
5.Missed letters.
6.Missed words.

If you will guess the letter it will be shown in hidden word on the place where it is in word.
Accepted input are letters only.
You can guess one letter or whole word (here you will need word lenght, because if you will enter more than one symbol and your word length is different, programm will ask you to try again)
If you guess incorrectly 6 times, the game will show a message that you lost. If you guess the word by letters or whole word before that happens, You will get "Like" and message that you won. 



