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
        return (self.row > 0) and Loc(self.row-1,self.col) or None
    def south(self):
        return (self.row < 7) and Loc(self.row+1,self.col) or None
    def west(self):
        return (self.col > 0) and Loc(self.row,self.col-1) or None
    def right(self):
        return (self.col < 7) and Loc(self.row,self.col+1) or None
    def nw(self):
        return (self.row > 0 and self.col > 0) and Loc(self.row-1,self.col-1) or None
    def ne(self):
        return (self.row > 0 and self.col < 7) and Loc(self.row-1,self.col+1) or None
    def sw(self):
        return (self.row < 7 and self.col > 0) and Loc(self.row+1, self.col-1) or None
    def se(self):
        return (self.row < 7 and self.col < 7) and Loc(self.row+1,self.col+1) or None
    def index(self):
        return self.row*8 + self.col

