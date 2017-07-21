"""
This is a blank file. 
It will test the implementation of checkers_tk.py step-by-step.
You (Brian) will do this hackishly by creating a daughter class that
inherits everything from the parent (which Michael wrote) except the
init. Then use try-except clauses to duplicate the init and print out
whether or not the user succeeded....? Can't check output.
"""

import os, sys
curdir = os.path.dirname(__file__)
sys.path.append(curdir)

from checkers_tk import CheckersGUI

class IncorrectAnswerError(Exception):
    pass


class CheckersTest(CheckersGUI):
    def _initialize(self):
        # Overloading _initialize to do nothing:
        pass

def truechar(pos, squaresize):
    i = 'ABCDEFGH'.index(pos[0])
    j = '12345678'.index(pos[1])
    return i * squaresize, (8-j) * squaresize

def checkchar(obj):
    allposes = [c+n for c in 'ABCDEFGH' for n in '12345678']
    for p in allposes:
        v0 = obj._charpos_to_xypos(p)
        v1 = truechar(p, obj.squaresize)
        if not all([a==b for a, b in zip(v0, v1)]):
            msg = 'Incorrect square!\t{}\nYours:\t\t{}\nCorrect:\t{}'.format(
                    p, v0, v1)
            raise IncorrectAnswerError(msg)

def drawpieces(obj):
    """Draws all the initial pieces except for the first one"""
    black_list = [c+n for c in 'ACEG' for n in '13']
    black_list.remove('A1')
    blb = [c + '2' for c in 'BDFH']
    black_list.extend(blb)

    red_list = [c+'7' for c in 'ACEG'] + [c+n for c in 'BDFH' for n in '68']
    obj.draw_pieces(black_list + red_list, ['black' for b in black_list] +
            ['red' for r in red_list])

def makekings(obj):
    for p in ['B2', 'D2', 'F2', 'H2']:
        obj.remove_piece(p)
        try:
            obj.draw_piece(p, 'black', king=True)
        except TypeError:
            raise NotImplementedError # meh. typeerror is if ``king`` is not implemented

def check_work(testclass=CheckersTest):
    test = testclass()
    funcs = [test.create_quit_button,
            test.create_canvas, 
            test.create_checkerboard,
            lambda : checkchar(test),
            lambda : test.draw_piece('A1', 'black'),
            lambda : drawpieces(test),
            lambda : test.delete_piece('B8'),
            lambda : [test.move_piece('A3', 'B4'), test.move_piece('H6', 'G5')],
            lambda : makekings(test)
            ]
    max_finished = 0
    for i, f in enumerate(funcs):
        try:
            f()
        # except Exception as e:
        except NotImplementedError as e:
            print 'Problem {} not finished yet!'.format(i+1)
            # raise e
            break
        else:
            max_finished += 1
    # now we have the var i which says how many of the functions we have
    # working. 
    # So we print to the user what they should see
    plist = [   '...a button which says `Quit` and quits when pressed',
                '...a red canvas',
                '...with black checkers squares on it. Lower-left square is black.',
                '',
                '...with one black piece in the lower left hand corner',
                '...and a complete initial checkers setup',
                '...with red missing one piece in its back row',
                '...where red and black have made a few moves',
                '...and all of black`s middle row is kings',
            ]
    print 'You should see:'
    if max_finished > 0:
        for a in xrange(max_finished):
            print plist[a]
    else:
        print '...a blank widget with an X in the upper right corner.'
    # And we mainloop() to show what is working:
    test.mainloop()


if __name__ == '__main__':
    check_work()

