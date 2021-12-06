import pytest
from gameplay.game import Game

    
# Test that checks if draw_hangman return list
# Test that checks draw_hangman returned values depending from lives amount
    

def test_reduce_lives():
    game = Game('TEST')
    assert game.lives == 6
    
    game.reduce_lives()
    assert game.lives == 5

    # Cheking if it is the same like in code
def test_draw_hangman():
    game = Game('TEST')#Game object
    
    assert game.word == 'TEST'
    
        #return hangman picture (return list)
        
    hangman_drawing = game.draw_hangman()
    assert hangman_drawing == [
        "",
        "",
        "",
        "",
        "",
        "_____________"
    ]

    # Test hangman picture on 4 lives
    game.lives = 4
    hangman_drawing = game.draw_hangman()
    assert hangman_drawing == [
        "     ______",
        "   |",
        "   |",
        "   |",
        "   |",
        "_____________"
    ]
    

