import Tkinter as tk
import os
curdir = os.path.dirname(__file__)
# OK I'm getting an outline. 
# TK board, rectangles that just stay on there
# dict of 64 elements with pieces; they get set to either the int handle
# of the TK piece or to a nan label.
# Drawing a piece gets called with a board.
# Moving a piece involves deleting the piece then re-adding the piece at
# a different location.
# deleting a piece involves just deleting a piece.

# -- need to draw as kings!

class CheckersBoard(tk.Frame):
    def __init__(self, master=None, boardsize=400):
        tk.Frame.__init__(self, master)
        self.grid()
        self.boardsize = boardsize
        self.squaresize = self.boardsize / 8
        self.piecesize = self.boardsize / 9
        # Some colors:
        self._board_blk = '#808080'
        self._board_red = '#D04040'
        self._piece_blk = '#000000'
        self._piece_red = '#701010'
        self._piece_lin = '#C0C0C0'

        self.create_board()
        self.pieces = []
        self.master.title('Checkers!')
        
        self._piece_dict = {l+n:['empty', 'empty'] for l in 'ABCDEFGH' for n
                in '12345678'}

    def create_board(self):
        self.canvas = tk.Canvas(self, background=self._board_red, height=
                self.boardsize, width=self.boardsize)
        
        self._rectangles = []
        rs = self.boardsize / 8
        for i in xrange(8):
            for j in xrange(8):
                # make a rectangle
                if self._is_black(i, j):
                    x0 = i * rs
                    y0 = j * rs
                    self._rectangles.append(self.canvas.create_rectangle(
                            x0, y0, x0 + rs, y0 + rs, fill=self._board_blk))
        self.canvas.grid()

    def _charpos_to_xypos(self, charpos):
        """
        Translates a alphanumeric code to a position on the canvas.

        Parameters
        ----------
        charpos : String
            Length-2 string to evaluate the xy-position as, e.g. 'A1'

        Returns
        -------
        y, x : Int
            The (vertical, horizontal) position on the canvas. 
            Note that (y,x) = (0,0) is the upper left-most pixel on the canvas, while A1 is the center of the lower left corner's
            square.
        """
        p = charpos.upper()
        i = 'ABCDEFGH'.index(charpos[0])
        j = '12345678'.index(charpos[1])
        return j * self.squaresize, (8-i) * self.squaresize

    def _is_black(self, i, j):
        """Checks if square [i,j] is black"""
        ieven = (i % 2) == 0
        jeven = (j % 2) == 0
        return (ieven & (~jeven)) | (jeven & (~ieven))

    def draw_piece(self, position, color='black'):
        """
        Parameters
        ----------
            position : String
                Length-2 string of the coordinate of the piece, e.g. 'A1'
            color : 'black' or 'red', optional
                The color of the piece. Default is black.
        """
        y, x = self._charpos_to_xypos(position)
        col = self._piece_blk if color == 'black' else self._piece_red
        shift = (self.squaresize - self.piecesize) / 2
        id = self.canvas.create_oval(y + shift, x - shift, y + shift +
                self.piecesize, x - shift - self.piecesize, fill=col, 
                outline=self._piece_lin)
        self._piece_dict[position] = [id, color]

    def draw_pieces(self, positions, colors):
        for p, c in zip(positions, colors):
            self.draw_piece(p, color=c)

    def delete_piece(self, position):
        if self._piece_dict[position][0] == 'empty':
            raise ValueError('No piece at `position`.')
        self.canvas.delete(self._piece_dict[position][0])
        self._piece_dict[position] = ['empty', 'empty']

    def move_piece(self, old_position, new_position):
        if self._piece_dict[old_position][0] == 'empty':
            raise ValueError('No piece at `old_position`.')
        if self._piece_dict[new_position][0] != 'empty':
            raise ValueError('Cannot move piece to an occupied position.')
        color = self._piece_dict[old_position][1]
        self.delete_piece(old_position)
        self.draw_piece(new_position, color=color)



# positions = [k+n for k in 'ABCDEFGH' for n in '12345678']
# colors = [['red', 'black'][i % 2] for i in xrange(64)]
# [app.delete_piece(v) for v in ['D1','D2','D3','D4','D5','D6','D7','D8']]
# app.move_piece('C4', 'D4')
positions = ['A1', 'B2', 'C3']
colors = ['red', 'black', 'red']
app = CheckersBoard(boardsize=800)
# app.master.title('Sample Application')
app.draw_pieces(positions, colors)
for c in positions: print c, app._charpos_to_xypos(c)

# trying to save as a ps file...
app.canvas.update()
app.canvas.postscript(file=curdir+'/board.ps', colormode='color')
# ....
app.mainloop()