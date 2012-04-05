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
    def index(self):
        return self.row*8 + self.col
    def north(self):
        return (self.row > 0) and Loc(self.row-1,self.col) or None
    def south(self):
        return (self.row < 7) and Loc(self.row+1,self.col) or None
    def west(self):
        return (self.col > 0) and Loc(self.row,self.col-1) or None
    def east(self):
        return (self.col < 7) and Loc(self.row,self.col+1) or None
    def nw(self):
        return (self.row > 0 and self.col > 0) and Loc(self.row-1,self.col-1) or None
    def ne(self):
        return (self.row > 0 and self.col < 7) and Loc(self.row-1,self.col+1) or None
    def sw(self):
        return (self.row < 7 and self.col > 0) and Loc(self.row+1, self.col-1) or None
    def se(self):
        return (self.row < 7 and self.col < 7) and Loc(self.row+1,self.col+1) or None
    def nnw(self):
        return self.north() and self.north().nw() or None
    def nne(self):
        return self.north() and self.north().ne() or None
    def nee(self):
        return self.east() and self.east().ne() or None
    def see(self):
        return self.east() and self.east().se() or None
    def sse(self):
        return self.south() and self.south().se() or None
    def ssw(self):
        return self.south() and self.south().sw() or None
    def sww(self):
        return self.west() and self.west().sw() or None
    def nww(self):
        return self.west() and self.west().nw() or None
