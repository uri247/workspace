'''
Created on Apr 1, 2012

@author: uri
'''

class Shape:
    PION=1
    ROCK=2
    HORSE=3
    BISOPH=4
    QUINNE=5
    KING=6

class Color:
    WHITE=1
    BLACK=2

class Piece:
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color
        
class Square:
    def __init__(self,row,col,piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    def put(self, piece):
        self.piece = piece 
    

    
class Board:
    def __init__(self):
        self.squares = [None]*64
        for row in range(8):
            for col in range(8):
                self.squares[row*8+col] = Square(row,col)
            
    def put(self,row,col,piece):
        self.squares[row*8+col].piece = piece
        
    def get(self,row,col):
        return self.squares[row*8+col]
    
    def move(self, src_row, src_col, trg_row, trg_col):
        self.squares[trg_row*8+trg_col].piece = self.squares[src_row*8+src_col].piece
        self.squares[src_row*8+src_col].piece = None
        
