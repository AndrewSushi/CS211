"""A slate is a very simple surface for drawing character graphics on a grid.
"""

from enum import Enum
from typing import Tuple, List


# Named directions. The values of the Direction Enum (e.g., Direction.NORTH.value)
# are indices to the DIR_VEC list, so for example DIR_VEC[Direction.NORTH.value]
# is (-1, 0), the direction vector for moving in the north direction.
#
class Dir(Enum):
    value: int
    NORTHWEST = 0      # (-1, -1)
    NORTH = 1       # (-1, 0)
    NORTHEAST = 2      # (-1, 1)
    EAST = 3       # (0, 1)
    SOUTHEAST = 4      # (1, 1)
    SOUTH = 5       # (1, 0)
    SOUTHWEST = 6      # (1, -1)
    WEST = 7       # (0, -1)


# From integers 0..7 to direction vectors.  Corresponds to
# the named directions above.
#
DIR_VEC = [
    (-1, -1),  # 0 -> NORTHWEST, up and to the left
    (-1, 0),  # 1 -> NORTH, up
    (-1, 1),  # 2 -> NORTHEAST, up and to the right
    (0, 1),  # 3 -> EAST, right
    (1, 1),  # 4 -> SOUTHEAST, down and to the right
    (1, 0),  # 5 -> SOUTH, down
    (1, -1),  # 6 -> SOUTHWEST, down and to the left
    (0, -1)  # 7 -> WEST, left
    ]

# Ink colors
BLACK = 1
WHITE = 0

# INKS map integer color identifiers (white and black)
# to the marks we will use for them in the printed slate.
# The spaces make vertical and horizontal spacing more even
# when printed.
INKS = [" - ", " # "]


class Slate:
    """A very simple character graphics canvas represented
    as a grid of characters, ' - ' for white and ' # ' for black.
    The grid is indexed by (row, col) integers, i.e., (0,0)
    is the upper left corner.
    """
    def __init__(self, rows=8, cols=8):
        """Initially the slate is blank (all white)
        with the cursor placed at cell (0, 0), the upper
        left row and column.
        """
        assert rows > 0, "Slates must have at least 1 row"
        assert cols > 0, "Slates must have at least 1 column"
        self.cells = []
        for row_i in range(rows):
            row = []
            for col_i in range(cols):
                row.append(INKS[WHITE])
            self.cells.append(row)
        self.cursor = (0, 0)
        self.pen_color = BLACK

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.cells)

    def set_color(self, color: int):
        self.pen_color = color

    def mark(self):
        """Make a mark at (row, col) with the selected ink;
        no effect if row or column are off the slate.
        """
        row, col = self.cursor
        if row < 0 or row >= len(self.cells):
            return       # Off the slate, no mark
        if col < 0 or col >= len(self.cells[0]):
            return      # Off the slate, no mark
        self.cells[row][col] = INKS[self.pen_color]

    def stroke(self, direction: Dir, dist: int, inked=True):
        """Draw a stroke from current cursor with
        current pen color in the designated direction
        for the designated distance, placing cursor
        just beyond the end of the stroke.
        """
        row, col = self.cursor
        d_row, d_col = DIR_VEC[direction.value]
        for i in range(dist):
            if inked:
                self.mark()
            row += d_row
            col += d_col
            self.cursor = row, col


def encode_stroke(direction: Dir, dist: int, inked: bool) -> str:
    """Encode a stroke command as a pair of hexadecimal
    digits.
    """
    # slyme format 8-bit encoding:
    # bit 7:  0 = move, 1 = draw
    # bits bits 3..6: distance, 0..15 steps
    # bits 0..2:  direction index
    assert 0 <= dist < 16
    ink_bit = 0
    if inked:
        ink_bit = 1 << 7
    byte = ink_bit | (dist << 3) | direction.value
    hex_digits = "0123456789ABCDEF"
    return hex_digits[byte >> 4] + hex_digits[byte & 15]


def slyme_encode(commands: List[Tuple[Dir, int, bool]]) -> List[str]:
    """Encode a series of (direction, dist, ) commands into a
    list of strings containing two-digit hex numbers
    """
    result = []
    for command in commands:
        direction, dist, inked = command
        result.append(encode_stroke(direction, dist, inked))
    return result

###
#  Example encoded snail graphics.
#  The snail must decode the command lists we build here.
###


def ox_example() -> List[str]:
    """An example sequence of drawing commands
    translated to hex
    """
    return slyme_encode([
        # Outer ring
        (Dir.EAST, 7, True), (Dir.SOUTH, 7, True), (Dir.WEST, 7, True), (Dir.NORTH, 7, True),
        # X through the middle
        (Dir.SOUTHEAST, 7, True), (Dir.WEST, 7, True), (Dir.NORTHEAST, 7, True), (Dir.NORTH, 0, True)
    ])


def z_example() -> List[str]:
    """Snail graphics commands for creating
    a Z shape.
    """
    return slyme_encode([(Dir.EAST, 7, True), (Dir.SOUTHWEST, 7, True), (Dir.EAST, 8, True)])


def s_example() -> List[str]:
    """Snail graphics commands for creating
    an s shape
    """
    return slyme_encode([
        (Dir.EAST, 7, False), (Dir.WEST, 7, True),      # Back to upper left
        (Dir.SOUTH, 3, True), (Dir.EAST, 7, True), (Dir.SOUTH, 4, True),
        (Dir.WEST, 8, True)
    ])


def concentric_example() -> List[str]:
    """Snail graphics for drawing an o inside an O"""
    return slyme_encode([
        # Outer O
        (Dir.EAST, 7, True), (Dir.SOUTH, 7, True), (Dir.WEST, 7, True), (Dir.NORTH, 7, True),
        # Now we need to move to the inner ring
        (Dir.SOUTHEAST, 2, False),
        # And draw the inner ring
        (Dir.EAST, 4, True), (Dir.SOUTH, 4, True), (Dir.WEST, 4, True), (Dir.NORTH, 4, True)
    ])

def make_test_cases():
    print(f"ox example: {ox_example()}")
    print(f"z example: {z_example()}")
    print(f"s example: {s_example()}")
    print(f"concentric example: {concentric_example()}")


def main():
    make_test_cases()
    # Ring
    slate = Slate()
    slate.stroke(Dir.EAST, 7)
    slate.stroke(Dir.SOUTH, 7)
    slate.stroke(Dir.WEST, 7)
    slate.stroke(Dir.NORTH, 7)
    print(slate)
    print()

    # Add an X through the middle
    # slate = Slate()
    slate.stroke(Dir.SOUTHEAST, 7)
    slate.stroke(Dir.WEST, 7)
    slate.stroke(Dir.NORTHEAST, 7)
    print(slate)
    print()

    # Labyrinth
    slate = Slate()
    for swath in range(5):
        slate.stroke(Dir.EAST, 7)
        slate.stroke(Dir.SOUTH, 2)
        slate.stroke(Dir.WEST, 7)
        slate.stroke(Dir.SOUTH, 2)
    print(slate)
    print()


if __name__ == "__main__":
    main()
