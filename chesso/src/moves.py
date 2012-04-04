'''
Created on Apr 2, 2012

@author: uri
'''

from board import *

class IllegalMove(Exception):
    pass

class Loc:
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def north(self):
        assert self.row != 0
        return Loc(self.row-1,self.col)
    def south(self):
        assert self.row != 7
        return Loc(self.row+1,self.col)
    def west(self):
        assert self.col != 0
        return Loc(self.row,self.col-1)
    def right(self):
        assert self.col != 7
        return Loc(self.row,self.col+1)
    def nw(self):
        assert self.row != 0 and self.col != 0
        return Loc(self.row-1,self.col-1)
    def ne(self):
        assert self.row != 0 and self.col != 7
        return Loc(self.row-1,self.col+1)
    def sw(self):
        assert self.row != 7 and self.col != 0
        return Loc(self.row+1, self.col-1)
    def se(self):
        assert self.row != 7 and self.col != 7
        return Loc(self.row+1,self.col+1)
    

class Move(object):
    def __init__(self,src,dst):
        self.src = src
        self.dst = dst
        
class PromotionMove(Move):
    def __init__(self):
        Move.__init__(self)
        Move.newPiece = Piece
    
    
def possibleMovePawn(board,sq):
    assert sq.piece.shape == Shapes.PAWN
    moves = []
    src = (sq.row,sq.col))
    if sq.piece.color == Colors.BLACK:
        assert sq.row != 0 and sq.row != 7
        if sq.row == 1:
            if board[row+2] == None:
                moves.append( Move(src,()
            
            if board[row+1,col]
    
    
class MyClass(object):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
        