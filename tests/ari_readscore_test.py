"""
test air read score lab
"""

import pytest
from air_readscore import Book

def testbookmake():
    pathn = '/home/chris/proj/ari/books/The_Fall_of_the_House_of_Usher.txt'
    tast1 = Book(name='FoU', path=pathn)
    assert tast1.name != None
    assert tast1.name == 'FoU'
    assert tast1.path != 'llamas'
    assert tast1.path == pathn
    empyf = (tast1.the_clean_text, tast1.char_count,
             tast1.word_count, tast1.sent_count, tast1.content)
    for feald in empyf:
        assert feald == None


def testprosses():
    pathn = '/home/chris/proj/ari/books/The_Fall_of_the_House_of_Usher.txt'
    test2 = Book('FoU.txt', pathn)
    test2.open_book()
    assert isinstance(test2.content, str), 'this is not a str'
    test2.clean_text()
    test2.prosses_text()
    new_test2 = test2.get_readability()
    assert isinstance(new_test2, list), 'needs to be list'
    assert new_test2 == ['FoU', 14.316623958269048]


