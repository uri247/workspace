'''
Created on Apr 1, 2012

@author: uri
'''


class Shapes:
    PAWN=0
    KNIGHT=1
    BISHOP=2
    ROOK=3
    QUEEN=4
    KING=5

class Colors:
    WHITE=1
    BLACK=2

class ShapeTrait:
    def __init__( self, shape, name, letter ):
        self.shape = shape
        self.name = name
        self.letter = letter

ShapeTraits = [
    ShapeTrait( Shapes.PAWN, 'pawn', 'p' ),
    ShapeTrait( Shapes.KNIGHT, 'knight', 'n' ),
    ShapeTrait( Shapes.BISHOP, 'bishop', 'b' ),
    ShapeTrait( Shapes.ROOK, 'rook', 'r' ),
    ShapeTrait( Shapes.QUEEN, 'queen', 'q' ),
    ShapeTrait( Shapes.KING, 'king', 'k' ),               
    ]

def shapeName(shape):
    return ShapeTraits[shape].name

def shapeLetter(shape):
    return ShapeTraits[shape].letter

def shapeByLetter(ch):
    ch = ch.lower()
    li = [tr for tr in ShapeTraits if tr.letter == ch]
    assert len(li) <= 1
    if len(li):
        return li[0]
    else:
        raise KeyError

def colorName(color):
    return color==Colors.WHITE and "white" or "black"  

class Piece:
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color
    def __repr__(self):
        return '%s %s' % ( colorName(self.color), shapeName(self.shape) )

def pieceLetter(p):
    if p:        
        l = ShapeTraits[p.shape].letter
        if p.color == Colors.WHITE:
            l = l.upper()
        return l    
    else:
        return '.'
    
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

    def __repr__(self):
        #join 8 rows; each row is a join of 8 letters.
        return "\n".join([
            "".join([
                pieceLetter(sq.piece)
                for sq
                in self.squares[row*8:row*8+8]
                ])
            for row
            in range(8)
            ])
            
        for row in range(7,-1,-1):
            for col in range(8):
                p = self[row,col]
                if p:
                    print p.shapeLetter,
                else:
                    print '.',
            print
        print
                    
    def __setitem__(self,key,value):
        row,col = key
        self.squares[row*8+col].piece = value;
    
    def __getitem__(self,key):       
        row,col = key
        return self.squares[row*8+col].piece;

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
        row = 0
        col = 0
        for ch in placement:
            if ch == '/':
                assert col == 8
                row += 1
                col = 0
            elif ch.isdigit():
                col += int(ch)
            else:
                shape = shapeByLetter(ch).shape
                if ch.islower():
                    color = Colors.BLACK
                else:
                    color = Colors.WHITE
                piece = Piece( shape, color )
                self[row,col] = piece
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
