"""
What is checkers? Broadly checkers is a board, some pieces, and a set of
rules, and 2 players. 

 - The board is a 8x8 grid. 
 - It contains 4 types of pieces (red, black (x) king, soldier) on one
    of 32 squares, although there are 64 on the board. 
 - During each turn, each player moves 1 piece. This may or may not result
    in one of the opponents pieces being `killed`, or it may change a
    soldier to a king.
 - The players are `intelligences` that make a move according to some
    strategy. 

Things we need:

 - a player that makes moves.
Other comments:

We also need a TK interface. 

Perhaps it's best to write a complete checkers game yourself and abstract
away off of that.
"""