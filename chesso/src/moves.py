'''
Created on Apr 2, 2012

@author: uri
'''

from board import Board
from location import Loc
from pieces import Shape, Colors, Piece, opositeColor, ShapeTraits, PromotableShapes

class Move(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    def __repr__(self):
        return "{0}=>{1}".format(self.src,self.dst)
        
class PromotionMove(Move):
    def __init__(self, src, dst, newPiece):
        Move.__init__(self,src, dst)
        self.newPiece = newPiece
    def __repr__(self):
        return "{0}=>{1} promoted to {2}".format(self.src,self.dst,self.newPiece)

def pawnBeforePromotion(sq):
    piece = sq.piece
    loc = sq.loc
    if (loc.row == 1 and piece.color == Colors.WHITE) or (loc.row == 6 and piece.color == Colors.BLACK):
        return True
    else:
        return False

def pawnOnStart(sq):
    piece = sq.piece
    loc = sq.loc
    if (loc.row == 6 and piece.color == Colors.WHITE) or (loc.row == 1 and piece.color == Colors.BLACK):
        return True
    else:
        return False

def forward(loc, color):
    if color == Colors.WHITE:
        return Loc(loc.row-1, loc.col)
    else:
        return Loc(loc.row+1, loc.col)
    

def possibleMovePawn(board,sq):
    assert isinstance(board, Board)
    assert sq.piece.shape == Shape.PAWN
    moves = []
    src = sq.loc
    piece = sq.piece
    if piece.color == Colors.WHITE:
        posdests = [(src.nw(),True), (src.north(),False), (src.ne(),True)]
    else:
        posdests = [(src.sw(),True), (src.south(),False), (src.se(),True)]
    posdests = [dst for dst in posdests if dst[0]]
         
    for posdest in posdests:
        dst = posdest[0]
        mustHit = posdest[1]
        dstpiece = board[ dst ]        
        sameOnDst = dstpiece and dstpiece.color == piece.color
        oponentOnDst = dstpiece and dstpiece.color == opositeColor(piece.color)
        freeOnDst = not sameOnDst and not oponentOnDst
        if (mustHit and oponentOnDst) or (not mustHit and freeOnDst):
            if pawnBeforePromotion(sq):
                for shape in PromotableShapes:
                    shtrt = ShapeTraits[shape]
                    have = len( board.force(shape,piece.color) )
                    maximum = shtrt.maximum
                    if have < maximum:
                        moves.append( PromotionMove(src, dst, Piece(shape, piece.color)) )
            else:
                moves.append( Move(src, dst) )
    if pawnOnStart(sq):
        f = forward(src, piece.color)
        if (board[f] == None):
            df = forward( f, piece.color )
            if board[df] == None:
                m = Move( src, df )
                moves.append(m)
    return moves



def executeMove( board, move ):
    assert isinstance(board,Board)
    assert isinstance(move, Move)
    
    


if __name__ == '__main__':
    b = Board()
    ''''b.readFen('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')'''
    b.readFen('rnb1kbnr/PppPpppp/8/8/4P3/5N1R/5PP1/1N2K3')
    print b
    
    wpsqrs = [sq for sq in b.army(Colors.WHITE) if sq.piece.shape == Shape.PAWN ]
    pmvs = []
    for psq in wpsqrs:
        pmvs += possibleMovePawn(b, psq)
        
    for mv in pmvs:
        print mv
