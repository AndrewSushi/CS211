# Mini-exam 4: Translating Slyme Commands

Maybe you've used turtle graphics.  Maybe you thought they were
a little slow, a little crude.  Well, make way for snail graphics!

Just as turtle graphics move an imaginary pen across the page, 
snail graphics move an imaginary cursor across a grid of 
characters.  The cursor can move without making a mark (uninked), 
or move while making a mark (inked).  
File `slate.py` provides the basic `Slate` class
for the grid of characters and the `stroke` method that the
snail uses to move or draw. 

A snail always starts in the upper left corner of
its slate (row 0, column 0). Strokes on a slate 
(and therefore movements of the snail) can be
in one of 8 directions, defined in the `Dir` enumeration class
`slate.py`.  A stroke can be up to 15 units long in any of those
directions.  The cursor can be inked or uninked.  

If we use 4 bits to indicate the length of a stroke, 3 bits to
indicate the direction of the stroke, and 1 bit to indicate whether
the cursor is inked or not, then we can pack all the needed information
for one stroke into an 8-bit integer.  That 8 bit integer could then
be expressed as two hexadecimal digits.  So, for example, we could
give the commands for drawing a Z shape as `['BB', 'BE', 'C3']`. 
This notation is called "Slyme", for "snail language you might enjoy".

I have provided an encoder for the Slyme notation in `slate.py`. 
It uses the following layout to pack information about a stroke: 


bits        | information
---         | ---
bit 7       | 0 = move, 1 = draw
bits 3..6   | distance, 0..15 steps
bits 0..2   | direction index

Your task is to unpack the Slyme code to
guide a snail on its path through the grid.
Note that you will have to convert bit 7 to
a boolean value with the `bool` function,
which converts 0 to `False` and 1 to `True`.
You will have to convert the direction
indicator to to an element of the `Dir`
enumeration.  

The code you need to write is in `snail.py`. 
There is very little code to write.  If you understand
manipulation of binary values (shifting, masking, etc)
it may go very quickly.  If you get stuck, remember that
decoding Slyme notation should be basically backward from
creating Slyme, so the `encode_stroke` function
in `slate.py` may be a useful reference. 

When you are done, the test cases in `test_snail.py`
should all pass.  Then you can turn your attention
to building beautiful Slyme patterns of your own. 
