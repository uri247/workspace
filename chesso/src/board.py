'''
Created on Apr 1, 2012

@author: uri
'''

from location import Loc
from pieces import Colors, colorName, Piece, pieceLetter, shapeByLetter


class Square:
    def __init__(self,loc,piece=None):
        self.loc = loc
        self.piece = piece
        
    def put(self, piece):
        self.piece = piece 
    

    
class Board:
    def __init__(self):
        self.squares = [ Square(Loc(i/8,i%8)) for i in range(64) ]
        self.move = Colors.WHITE
        self.castling = '-'
        self.enpassant = '-'

    def __repr__(self):
        #join 8 rows; each row is a join of 8 letters.
        return "\n".join([
            "".join([
                pieceLetter(sq.piece)
                for sq in self.squares[row*8:row*8+8]
                ])
            for row in range(8)
            ])  + '\n - ' + colorName(self.move) + ' move' + '\n'
            
                    
    def __setitem__(self,loc,value):
        assert isinstance(loc,Loc)
        self.squares[loc.index()].piece = value;
    
    def __getitem__(self,loc):       
        assert isinstance(loc, Loc)
        return self.squares[loc.index()].piece;

    def move(self, src, dst):
        self.squares[dst], self.squares[src] = self.squares[src], None

    def whites(self):
        return [ sq for sq in self.squares if (sq.piece and sq.piece.color == Colors.WHITE) ]

    def clear(self):
        for sq in self.squares:
            sq.piece = None
            
    def readFen(self,fen):
        self.clear()
        fields = fen.split( ' ' )
        placement = fields[0]
        row, col = 0, 0
        for ch in placement:
            if ch == '/':
                assert col == 8
                row, col = row+1, 0
            elif ch.isdigit():
                col += int(ch)
            else:
                shape = shapeByLetter(ch).shape
                if ch.islower():
                    color = Colors.BLACK
                else:
                    color = Colors.WHITE
                piece = Piece( shape, color )
                self[Loc(row,col)] = piece
                col += 1
        row += 1
        assert row == 8 and col == 8

    
    
if __name__ == '__main__':
    b = Board()
    b.readFen('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')
    print b
        
    w = b.whites();
    for sq in w:
        print "%s at (%d,%d)" % (sq.piece, sq.row, sq.col)
