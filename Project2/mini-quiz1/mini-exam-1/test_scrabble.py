"""Test cases for scrabble.py"""

import unittest
from typing import List
from scrabble import *

# Standard Scrabble Tile Values
BY_VALUE = {
    1: "AEIOULNSTR",
    2: "DG",  3: "BCMP",
    4: "FHVWY", 5: "K",
    8: "JX", 10: "QZ"
}

VALUES = {}
for value, letters in BY_VALUE.items():
    for letter in letters:
        VALUES[letter] = value

def scrabble_tile(letter: str) -> Tile:
    """Given a single letter, return a Tile object for that letter
    with the proper value by standard Scrabble rules.
    """
    return Tile(letter, VALUES[letter])

def tile_list(letters: str) -> List[Tile]:
    """Return a list of newly created Tile objects,
    one for each letter in letters.
    Every character in letters must be a capital letter
    of English (a legal tile letter in Scrabble).
    """
    return [Tile(l, VALUES[l]) for l in letters]


class Test_Tile(unittest.TestCase):
    """Very basic tests of the Tile object"""

    def test_tile(self):
        """Each tile object is distinct from other tiles"""
        t1 = Tile("X", 8)
        t2 = Tile("H", 4)
        self.assertEqual(t1.letter, "X")
        self.assertEqual(t2.letter, "H")
        self.assertEqual(t1.value, 8)
        self.assertEqual(t2.value, 4)


class Test_Tray_Has(unittest.TestCase):
    """Q1 requires the 'has' method to determine whether
    the tray contains a tile with a given letter.  This is
    a function returning a boolean and should not modify the
    contents of the tray.
    """

    def test_does_have(self):
        tray = Tray()
        tiles = tile_list("AJX")
        extra = scrabble_tile("M")
        for tile in tiles:
            tray.add_tile(tile)
        self.assertTrue(tray.has("J"))
        self.assertTrue(tray.has("A"))
        self.assertTrue(tray.has("X"))
        self.assertFalse(tray.has("M"))
        # And we haven't removed them
        self.assertTrue(tray.has("J"))

class Test_Word_Scores_Simple(unittest.TestCase):
    """Scoring words provided they have no duplicate letters
    (much easier than allowing for duplicate letters)
    """

    def test_score_present(self):
        """The tiles (A,1), (X,8), (E,1) are present to make AXE"""
        tray = Tray()
        for tile in tile_list("XWEAU"):
            tray.add_tile(tile)
        self.assertEqual(tray.would_score("AXE"), 10)

    def test_score_no_modify(self):
        """would_score should not remove letters from the tray!"""
        tray = Tray()
        for tile in tile_list("XWEAU"):
            tray.add_tile(tile)
        self.assertEqual(tray.would_score("AXE"), 10)
        # The A and E should still be present!
        self.assertEqual(tray.would_score("AWE"), 6)


    def test_score_missing(self):
        """There is no tile E to make AXE"""
        tray = Tray()
        for tile in tile_list("XWRAU"):
            tray.add_tile(tile)
        self.assertEqual(tray.would_score("AXE"), 0)



class Test_Word_Scores_Hard(unittest.TestCase):
    """Much more challenging when we must consider how
    many of each letter are present.
    """

    def test_has_enough_a(self):
        """We have two A to make AJAX"""
        tray = Tray()
        for tile in tile_list("XARAUJ"):
            tray.add_tile(tile)
        self.assertEqual(tray.would_score("AJAX"), 18)

    def test_not_enough_a(self):
        """Not enough A for AJAX"""
        tray = Tray()
        for tile in tile_list("XERAUJ"):
            tray.add_tile(tile)
        self.assertEqual(tray.would_score("AJAX"), 0)


if __name__ == "__main__":
    unittest.main()



