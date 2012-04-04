'''
Created on Apr 3, 2012

@author: uri
'''


class IllegalMove(Exception):
    pass

class Loc(object):
    """Loc represents a location on the chess board. It has row and col
    properties, and a reach set of helper methods
    """
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def __repr__(self):
        return "({0},{1})".format(self.row, self.col)
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
    def index(self):
        return self.row*8 + self.col

        