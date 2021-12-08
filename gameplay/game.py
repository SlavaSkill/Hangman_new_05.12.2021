class Game:
    """Summary of class - what is what.

    Provides building blocks of the Hangman game.

    Attributes
    Typical usage example

    """
    
    def __init__(self, word):
        """ 
        Initializes the attributes
        
        """
        self.word = word.upper()
        self.word_progress = list(len(word) * "-")
        self.lives = 6
        self.word_is_guessed = False
        self.guessed_letters = set()
        self.missed_letters = set()
        self.missed_words = set()
        
    def reduce_lives(self):
        self.lives -= 1


    def get_input(self):

# We input letters or words and delete if there is space we delete it with strip()
        guess = input("Please try and guess a letter: ").upper().strip()
        if len(guess) == 0:
            raise EOFError("Please, enter at least 1 letter!")
        elif not guess.isalpha():
            raise TypeError("Please, use only letters!")

        return guess

    def play(self):
        self.user_name = input("Please, enter your name: ")
        
        while self.lives > 0 and self.word_is_guessed == False:
            print()
            self.print_list(self.draw_hangman())
            self.print_status()
            print()
            
            try:
                guess = self.get_input()
            except (TypeError, EOFError) as err:
                print(err)
                continue

          
            if len(guess) == 1:

                if guess in self.guessed_letters or guess in self.missed_letters:
                    print("You already tried this letter\n")
                    continue
                
                if guess in self.word:
                    print("Correct you guessed a letter")
                    self.guessed_letters.add(guess)
                    # Open correctly guessed letter
                    for index, letter in enumerate(self.word):
                        if letter in self.guessed_letters:
                            self.word_progress[index] = letter
                    # Cheking if word is guessed
                    if self.word == ''.join(self.word_progress):
                        self.word_is_guessed = True
                else:
                    print("Wrong! Please try guessing another letter")
                    self.missed_letters.add(guess)   
                    self.lives -= 1       
            else:
                # If entered more than one simbol
                if len(guess) != len(self.word):
                    print("Word lenght in not correct try again\n")
                    continue
                
                if guess in self.missed_words:
                    print("You already tried this word\n")
                    continue
                    
                if self.word == guess:
                    self.word_is_guessed = True
                else:
                    print("Wrong word") 
                    self.missed_words.add(guess)
                    self.lives -= 1    
        
        self.print_game_over_message()
        
    # Function that shows information to user            
    def print_status(self):
        print(f"Word: {''.join(self.word_progress)}")
        print("Word leght:", len(self.word))
        print("Lives: ", self.lives * "♥")
        print(f"Missed letters: {', '.join(self.missed_letters)}")
        print(f"Missed words: {', '.join(self.missed_words)}")
        
    def print_game_over_message(self):
        print("\nGame over!")
        if self.word_is_guessed:
            print(" ░░░░░░░░░░░░░░░░░░░░▄████▄░░░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░░██░░░██░░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░░▄█▀░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░░▄█▀░░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░░░██░░░░░░░██░░░░░░░░░░░░\n",
            "░░░░░░░░░░░░░░░▄█▀░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀██▄\n",
            "▄███████████████▀░░░░░░░░░░░░░░░░░░░░░██\n",
            "██░░░░░░░░░░█▀░░░░░░░░░░░░░░░░░░░░░░▄▄█▀\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░██░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░▄██░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░▀█░░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░▄█░░\n",
            "██░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░███░░\n",
            "██░░░░░░░░░░█▄░░░░░░░░░░░░░░░░░░░░░▄█▀░░\n",
            "██░░░░░░░░░░████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██▀░░░\n",
            "▀████████████▀░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░░░\n")            
            print(f"Congrats {self.user_name} You WON! Word: {self.word}")
            
        else:
            self.print_list(self.draw_hangman())
            print(f"You Lost {self.user_name}! Correct word: {self.word}")
    
    # Pictures of hangman            
    def draw_hangman(self):
        if self.lives == 6:
            return [
                "",
                "",
                "",
                "",
                "",
                "_____________"
            ]
      
        elif self.lives == 5:
            return [
                "    _",
                "   |",
                "   |",
                "   |",
                "   |",
                "_____________"
            ]
        elif self.lives == 4:
            return [
                "     ______",
                "   |",
                "   |",
                "   |",
                "   |",
                "_____________"
            ]
        elif self.lives == 3:
            return [
                "     ______",
                "   |      0",
                "   |",
                "   |",
                "   |",
                "_____________"
            ]
        elif self.lives == 2:
            return [
                "     ______",
                "   |      0",
                "   |      █",
                "   |      █",
                "   |",
                "_____________"
            ]
        elif self.lives == 1:
            return [
                "     ______",
                "   |      0",
                "   |     /█\ ",
                "   |      █",
                "   |",
                "_____________"
            ]
        elif self.lives == 0:
            return [
                "     ______",
                "   |      0",
                "   |     /█\ ",
                "   |      █",
                "   |     / \ ",
                "_____________"
            ]
    # take list as argument and print every list element in new line            
    def print_list(self, list_to_print):
        # make it to str
        list_of_strings = map(str, list_to_print)
        print("\n".join(list_of_strings))
