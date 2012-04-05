'''
Created on Apr 2, 2012

@author: uri
'''

from board import Board, Square
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


def possibleMoveRank(board,sq):
    assert isinstance(board, Board)
    assert isinstance(sq, Square)
    assert sq.piece.shape in [Shape.ROOK, Shape.BISHOP, Shape.QUEEN]

    moves = []
    src = sq.loc
    piece = sq.piece

    directionsDict = {
        Shape.ROOK: [ Loc.north, Loc.south, Loc.east, Loc.west ],
        Shape.BISHOP: [ Loc.nw, Loc.ne, Loc.sw, Loc.se ],
        Shape.QUEEN: [ Loc.nw, Loc.north, Loc.ne, Loc.west, Loc.east, Loc.sw, Loc.south, Loc.se ]
        }
    
    directions = directionsDict[ piece.shape ]

    for direction in directions:
        dst = src
        while True:
            dst = direction(dst)
            if not dst:
                break                
            elif not board[dst] or board[dst].color == opositeColor(piece.color):
                moves.append( Move(src, dst) )
                if board[dst]:
                    break
            else:
                break
            pass
        pass
    return moves

def nop(board,sq):
    return [] 

def possibleMove(board, sq):
    assert isinstance(board,Board)
    assert isinstance(sq, Square)
    src = sq.loc
    piece = board[src]
    movedict = {
        Shape.PAWN: possibleMovePawn,
        Shape.ROOK: possibleMoveRank,
        Shape.BISHOP: possibleMoveRank,
        Shape.QUEEN: possibleMoveRank,
        Shape.KING: nop,
        Shape.KNIGHT: nop
        }
    movefn = movedict[piece.shape]
    return movefn(board,sq)
    

def executeMove( board, move ):
    assert isinstance(board,Board)
    assert isinstance(move, Move)
    
    


if __name__ == '__main__':
    b = Board()
    ''''b.readFen('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2')'''
    b.readFen('r1nb1kbn/rPppPppp/p7/8/2Q2P2/6N1/R5PP/2N2K2')
    print b
    
    pmvs = []
    whites = b.army(Colors.WHITE)
    for sq in whites:
        pmvs += possibleMove(b,sq)
        
    for mv in pmvs:
        print mv
