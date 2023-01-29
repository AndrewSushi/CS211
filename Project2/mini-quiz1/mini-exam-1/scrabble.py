class Tile:
    def __init__(self, letter: str, value: int):
        self.letter = letter
        self.value = value

    def __str__(self) -> str:
        """Looks like ('X', 8)"""
        return f"('{self.letter}',{self.value})"

    def __repr__(self) -> str:
        """Looks like Tile('X', 8)"""
        return f"Tile('{self.letter}', {self.value})"

class Tray:
    def __init__(self):
        self.tiles = []

    def add_tile(self, tile: Tile):
        """Add to the  collection of tile in this tray"""
        self.tiles.append(tile)

    def __str__(self) -> str:
        """Looks like ('A', 1),('X', 8),('E', 1)"""
        return ",".join([str(t) for t in self.tiles]
)
    def __repr__(self):
        """Looks like Tray(('A', 1),('X', 8),('E', 1))"""
        return f"Tray({str(self)})"

    def has(self, letter: str) -> bool:
        for tile in self.tiles:
            if letter == tile.letter:
                return True
        return False

    def would_score(self, word:str) -> int:
        score = 0
        tray_letters = [i.letter for i in self.tiles]
        letter_vals = [i.value for i in self.tiles]
        for l in word:
            if l in tray_letters:
                idx = tray_letters.index(l)
                score += letter_vals[idx]
                del tray_letters[idx], letter_vals[idx]
            else:
                return 0
        return score