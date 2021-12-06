# TODO: Aktivizēt virtual env, pip install pytest, pip freeze > requirements.txt
import pytest
from gameplay.game import Game

    
# tests kur pārbauda vai draw_hangman atgriež listu
# tests kur pārbauda draw_hangman atgrieztās vērtības attiecīgi no dzivību daudzuma
    

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

    # Notestēt hangman zīmējumu pie 4, 2, 0 dzīvībām
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
    

