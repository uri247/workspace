'''
Created on Apr 1, 2012

@author: uri
'''

from location import Loc
from pieces import Piece, pieceLetter, Colors, colorName, shapeByLetter


class Square:
    def __init__(self,loc,piece=None):
        assert isinstance(loc, Loc)
        self.loc = loc
        self.piece = piece
        
    
class Board:
    def __init__(self):
        self.squares = [ Square(Loc(i/8,i%8)) for i in range(64) ]
        self.nextmove = Colors.WHITE
        self.castling = '-'
        self.enpassant = '-'

    def __repr__(self):
        #join 8 rows; each row is a join of 8 letters.
        return "\n".join([
            "".join([
                pieceLetter(sq.piece)
                for sq in self.row(row)
                ])
            for row in range(8)
            ]) + \
            '\n - ' + colorName(self.nextmove) + ' move' + '\n'
            
                    
    def __setitem__(self,loc,value):
        assert isinstance(loc,Loc)
        self.squares[loc.index()].piece = value;
    
    def __getitem__(self,loc):       
        assert isinstance(loc, Loc)
        return self.squares[loc.index()].piece;

    def row(self,row):
        assert row>=0 and row<8
        return self.squares[row*8:row*8+8]

    def col(self,col):
        assert col>=0 and col<8
        return [self.squares[row+col] for row in range(8)]        

    def army(self,color):
        return [sq for sq in self.squares if (sq.piece and sq.piece.color == color)]
    
    def force(self,shape,color):
        return [sq for sq in self.squares if (sq.piece and sq.piece.color == color and sq.piece.shape == shape)]
    
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
        if( len(fields) > 1 ):
            self.nextmove = fields[1] == 'w' and Colors.WHITE or Colors.BLACK
        if( len(fields) > 2 ):
            self.castling = fields[2]
        if( len(fields) > 3 ):
            self.enpassant = fields[3]

    
    
if __name__ == '__main__':
    b = Board()
    b.readFen('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')
    print b
        
    w = b.army(Colors.WHITE)
    for sq in w:
        print "%s at %s" % (sq.piece, sq.loc)
