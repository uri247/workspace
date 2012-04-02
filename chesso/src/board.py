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

def shapeName(shape):
    names = { Shape.PION: 'pion', Shape.ROCK : 'rock', Shape.HORSE: 'horse',
             Shape.BISOPH: 'bishop', Shape.QUINNE: 'queen', Shape.KING: 'king' }
    return names[shape]

class Color:
    WHITE=1
    BLACK=2

def colorName(color):
    return color==Color.WHITE and "WHITE" or "BLACK"
    

class Piece:
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color
    def __repr__(self):
        return '%s %s' % ( shapeName(self.shape), colorName(self.color) )

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

    def __setitem__(self,key,value):
        row,col = key
        self.squares[row*8+col].piece = value;
    
    def __getitem__(self,key):       
        row,col = key
        return self.squares[row*8+col].piece;

    def move(self, src, dst):
        self.squares[dst], self.squares[src] = self.squares[src], None

    def whites(self):
        return [ sq for sq in self.squares if (sq.piece and sq.piece.color == Color.WHITE) ]
            



if __name__ == '__main__':
    b = Board()
    b[0,0] = Piece(Shape.ROCK, Color.WHITE)
    b[0,1] = Piece(Shape.HORSE, Color.WHITE)
    b[0,2] = Piece(Shape.BISOPH, Color.WHITE)
    b[7,0] = Piece(Shape.ROCK, Color.BLACK)
    b[7,4] = Piece(Shape.KING, Color.BLACK)
    for i in range(8):
        b[1,i] = Piece(Shape.PION, Color.WHITE)
        b[6,i] = Piece(Shape.PION, Color.BLACK)
    
    w = b.whites();
    for sq in w:
        print sq.piece
