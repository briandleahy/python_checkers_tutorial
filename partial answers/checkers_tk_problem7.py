"""
Here you will make a checkers board. We'll start with the board itself,
which can do some basic things on a board -- be a board, add pieces to
the board, remove pieces from the board, and move pieces on the board.
However the board object for now won't know any rules of checkers.

You will do this with Tk, which is a
GUI (graphical user interface) package. I'll set up the Tk stuff but you
can definitley look at it if you want.

I've planned this out as some very bite-sized methods to implement.
In order, you will:

1. Create a minimal Tk widget. Understand how a class works.
2. Create a red canvas
3. Create a checkerboard pattern -- i.e. a picture of a blank checkers board.
4. Write a function that translates from board coordinates ('A1') to a
    position on the board.
5. Create a function that draws one piece on the board.
6. Create a function that draws many / all the pieces on the board.
7. Create a function that _removes_ pieces from the board.
8. Create a function that moves a piece from one location to another.
9. Modify your draw_piece function and draw_pieces function to draw
   different pieces for kings and regular soldiers.
10. Advanced, part 1: Add a functionality to click on a piece and 
    highlight it
11. Advanced, part 2: Add a functionality to click on a piece and move
    it to a new location. If you'd like you can add a right-click
    or keyboard functionality to delete the piece or to undo a move

The way that I've done this is to create 1 big class with many methods.
You'll basically implement the methods one-by-one until the whole thing 
is complete. I've already implemented this first, but I haven't checked
the test module and I haven't thought too much about the structure. If you think of a better way to lay out this code then let me know!

To do this, you'll need to use Tkinter, which is a module that does GUI
stuff for Python. You can find several tutorials online (if I recall effbot
has a good one), or you can look at the documentation here:
http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf

TKinter is a _huge_ package, so rather than have you drown in it I'll try to
point out the things that are useful.

Where are we going / would we be going if we were making this bigger?
Well, I'd make a "game" class that would somehow know the rules and
check if moves are valid. Then I would make a "player" class that 
provides moves when prompted. For a human the player would be related
to this GUI below, but for an AI this might be something more 
complicated.

"""

import Tkinter as tk  # imports the Tk package

# Defining some colors for the board and pieces. Use these when you
# create the board and pieces:
BOARD_RED = '#D04040'
BOARD_BLACK = '#808080'
PIECE_BLACK = '#000000'
PIECE_RED = '#701010'
PIECE_LINE = '#C0C0C0'

# FIXME should this be an inheritance or a composition issue?
# Probably composition..... we'll stick to inheritance for now
# because the tutorial does.
class CheckersGUI(tk.Frame):
    def __init__(self, master=None, boardsize=400):
        """
        The __init__ is called when a new object of the class is created
        (i.e. it's a class constructor). Here, we use the __init__ to set up
        our file. I'm using the __init__ to just call other functions
        that do the work. For now, don't edit the __init__, since I'm using
        it to check how much you've completed.

        You should document your headers, like this...

        Parameters
        ----------
        master : {Tk.Frame, None}, optional
            A master frame to embed the checkers game in.
        boardsize : Int, optional
            The size of the (square) board, in pixels.
        """
        # For now don't worry about these next 2 lines
        tk.Frame.__init__(self, master)
        self.grid()

        # PROBLEM 1. What do these lines do?
        self.boardsize = boardsize
        self.squaresize = self.boardsize / 8
        self.piecesize = self.boardsize / 9

        # To make this easier for me to check your work, I'm calling
        # the functions one-by-one through a function
        # _initialize that does most of the constructor's work.
        self._initialize()
        # FIXME? adding a position dict:
        self.pos_dict = {k:['empty', 'empty', 'empty'] for k in [c+n for
            c in 'ABCDEFGH' for n in '12345678']}
    def _initialize(self):
        # PROBLEM 1. We create a minimal Tk widget.
        self.create_quit_button()

        # PROBLEM 2: Creat a red canvas
        self.create_canvas()

        # PROBLEM 3: Create a checkerboard pattern.
        self.create_checkerboard()

        # PROBLEM 4: Write a function that translates from board
        # coordinates ('A1') to a position on the board. See the
        # method _charpos_to_xypos below

        # PROBLEM 5: Create a function that draws one piece on the board
        # -- see the function draw_piece below

        # PROBLEM 6: Create a function that draws many pieces on the board
        # -- see the function draw_pieces below.
        
        # PROBLEM 7: Create a function that _deletes_ a piece from the
        # board
        # -- see the function delete_piece below

        # Problem 8: Create a function that moves a piece from one square
        # to another.
        # -- see the function move_piece below
        
        # PROBLEM 9: Modify your draw_piece functino and draw_pieces
        # function to draw different pieces for kings and regular 
        # soldiers. Depending on how you do this, you may need to modify
        # delete_piece as well.

    def create_quit_button(self):
        # PROBLEM 1: Create an attribute quit_button which quits the
        # application when clicked on. make it say "Quit".
        # This is basically the ``minimal application`` in the Tk tutorial,
        # page 4:
        # http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf
        #
        # In addition, I have two questions that you should answer:
        #   (a) Why does this function take ``self`` as an argument??
        #   (b) What does the next line (raise NotImplementedError) do?
        #       should you leave it in?
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()

    def create_canvas(self):
        # PROBLEM 2: Draw a red canvas, of the same size as the
        # ``boardsize`` passed to the class constructor (__init__)
        # Hint 0: You'll want the tk.Canvas function. Look at its
        #       documentation. What is the master Frame here?
        # Hint 1: What did the line in the __init__ do:
        #       self.boardsize = boardsize
        # Hint 2: TKinter uses a canvas. You'll want to keep the canvas
        #       to use later. I kept it by defining a self.canvas attribute.
        #
        # Make the board the color BOARD_RED defined in the module
        # level variable at the top of the file.
        self.canvas = tk.Canvas(self, height=self.boardsize,
                width=self.boardsize, background=BOARD_RED)
        self.canvas.grid()  # FIXME does this need to be here? Or at the end of the init?

    def create_checkerboard(self):
        # PROBLEM 3: Draw a checkerboard, i.e. draw the black squares on
        # the canvas. Make sure that the lower-left square is black, and
        # that the checkerboard occupies the entire canvas. Color the
        # black squares using the BOARD_BLACK color defined at the
        # beginning of the module
        # HINT 0: You'll probably want the create_rectangle method of
        #       a Tk.Canvas object.
        # HINT 1: You'll need to do some math here to find where the
        #       squares should be.
        # HINT 2: You're drawing a whole bunch of squares on a regular
        #       grid. What is the best way to do this? Should you hard-
        #       code all 32 square's positions or is there a better way?
        make_square = lambda i, j: (i % 2) + (j % 2) == 1
        ss = self.squaresize
        for a in xrange(8):
            for b in xrange(8):
                if make_square(a, b):
                    self.canvas.create_rectangle(ss * a, ss * b,
                            ss * (a+1), ss * (b+1), fill=BOARD_BLACK)

    def _charpos_to_xypos(self, charpos):
        """
        Translates a alphanumeric code to an (x,y) position on the canvas
        corresponding to the lower-left corner of the square ``charpos``.

        Parameters
        ----------
        charpos : String
            Length-2 string to evaluate the xy-position as, e.g. 'A1'

        Returns
        -------
        x, y : Int
            The (horizontal, vertical) position on the canvas.
            Note that (x, y) = (0,0) is the upper-left-most pixel on 
            the canvas, while A1 is the lower-left-most pixel on the
            canvas.
        """
        # PROBELM 4: Implement this function. Make it follow what is
        # stated in the documentation above
        # HINT: The canvas uses "image coordinates". A point (i, j) is
        # the pixel that is j pixels _down_ from the top left corner
        xb = 'ABCDEFGH'.index(charpos[0])
        yb = 8 - '12345678'.index(charpos[1])
        return xb * self.squaresize, yb * self.squaresize

    def draw_piece(self, position, color, king=False):
        """
        Draws a piece on the checkers board.

        Parameters
        ----------
        position : String
            Length-2 string of the coordinates of the piece, e.g. 'A1'
            for the lower-left corner.
        color : {'red', 'black'}
            The color of the piece, either red or black only.
        """
        # PROBLEM 5: Draw a piece at this position. Make the black pieces
        # the PIECE_BLACK color and the red pieces the PIECE_RED color.
        # Make their outline the PIECE_LINE color
        # Hint: You'll want the Tk.Canvas's create_oval method
        # PROBLEM 9: Modify this to draw different pieces for kings and
        # regular soldiers. Have it take an optional boolean argument 
        # `king`, with a default of False
        pt = self._charpos_to_xypos(position)
        col = {'red':PIECE_RED, 'black':PIECE_BLACK}[color]
        shift = (self.squaresize - self.piecesize) / 2
        id = self.canvas.create_oval(pt[0] + shift, pt[1] - shift -
                self.piecesize, pt[0] + shift + self.piecesize, pt[1] - 
                shift, fill=col, outline=PIECE_LINE)
        # Then we update the piece:
        self.pos_dict[position] = [id, color, king]

    def draw_pieces(self, positions, colors):
        """
        Draws multiple pieces on the checkers board.

        Parameters
        ----------
        positions : List of strings
            A list of alphanumeric positions (e.g. 'A1') at which to draw
            the pieces.
        Colors : List of {'red', 'black'}
            A list of colors for the pieces, each element must be either
            `'red'` or `'black'`. Must have the same number of elements
            as `positions`.

        See Also
        --------
        draw_piece : Draws 1 piece.
        """
        # PROBLEM 6: Draw many pieces!
        # Hint 0: This is now super easy since you've done problem #5.
        #       Just call that function many times.
        # Hint 1:You might want to look at the Python zip function
        for p, c in zip(positions, colors):
            self.draw_piece(p, c)

    def delete_piece(self, position):
        """Delete the piece at the alphanumeric position"""
        # PROBLEM 7: Delete a piece. This is a trickier problem because
        #       you need to "remember" which piece to delete.
        # Hint 0: You'll want to use the `delete` method of a canvas
        # Hint 1: The delete method needs the id of the object to delete,
        #       but you'll only supply the position. I worked around this
        #       by adding an extra attribute which is a dictionary of
        #       all the pieces drawn on the canvas, at each position.
        #       Then when I needed to look up which object to delete I
        #       just reference the key `position`. You can do this what-
        #       ever way you want though.
        # Hint 2: Things can get confusing later. I like to raise an
        #       error if someone tries to delete a piece at a blank
        #       position.
        id = self.pos_dict[position][0]
        if id == 'empty':
            msg = "Cannot delete piece from empty square:\t{}".format(position)
            raise ValueError(msg)
        else:
            self.canvas.delete(id)
            self.pos_dict[position] = ['empty', 'empty', 'empty']

    def move_piece(self, old_position, new_position):
        """Moves a piece from old_position to new_position"""
        # Hint 0: Moving a piece is the same as deleting it and re-adding
        #       it at a new location.
        # Hint 1: ... but you need to remember / get the color
        raise NotImplementedError

