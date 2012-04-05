'''
Created on Apr 2, 2012

@author: uri
'''

from board import Board, Square
from location import Loc
from pieces import Shape, Colors, Piece, opositeColor, ShapeTraits, PromotableShapes

class Move(object):
    def __init__(self, pc, src, dst):
        self.pc = pc
        self.src = src
        self.dst = dst
    def __repr__(self):
        return "{0}: {1}=>{2}".format(self.pc,self.src,self.dst)
        
class PromotionMove(Move):
    def __init__( self, pc, src, dst, newPiece ):
        Move.__init__( self, pc, src, dst )
        self.newPiece = newPiece
    def __repr__(self):
        return "{0}: {1}=>{2} promoted to {3}".format( self.pc, self.src, self.dst, self.newPiece )

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
                        moves.append( PromotionMove(piece, src, dst, Piece(shape, piece.color)) )
            else:
                moves.append( Move(piece, src, dst) )
    if pawnOnStart(sq):
        f = forward(src, piece.color)
        if (board[f] == None):
            df = forward( f, piece.color )
            if board[df] == None:
                m = Move( piece, src, df )
                moves.append(m)
    return moves


directionsDict = {
    Shape.ROOK: [ Loc.north, Loc.south, Loc.east, Loc.west ],
    Shape.BISHOP: [ Loc.nw, Loc.ne, Loc.sw, Loc.se ],
    Shape.QUEEN: [ Loc.nw, Loc.north, Loc.ne, Loc.west, Loc.east, Loc.sw, Loc.south, Loc.se ],
    Shape.KNIGHT: [ Loc.nnw, Loc.nne, Loc.nee, Loc.see, Loc.sse, Loc.ssw, Loc.sww, Loc.nww ],
    Shape.KING: [  Loc.nw, Loc.north, Loc.ne, Loc.west, Loc.east, Loc.sw, Loc.south, Loc.se ],
    }


def possibleMoveRank(board,sq):
    assert isinstance(board, Board)
    assert isinstance(sq, Square)
    assert sq.piece.shape in [Shape.ROOK, Shape.BISHOP, Shape.QUEEN]
    moves = []
    src = sq.loc
    piece = sq.piece
    directions = directionsDict[ piece.shape ]

    for direction in directions:
        dst = src
        while True:
            dst = direction(dst)
            if not dst:
                break                
            elif not board[dst] or board[dst].color == opositeColor(piece.color):
                moves.append( Move(piece, src, dst) )
                if board[dst]:
                    break
            else:
                break
            pass
        pass
    return moves



def possibleMoveShort(board,sq):
    assert isinstance(board, Board)
    assert isinstance(sq,Square)
    assert sq.piece.shape in [ Shape.KNIGHT, Shape.KING ]
    moves = []    
    for fn in directionsDict[ sq.piece.shape ]:
        dst = fn(sq.loc)
        if dst and (not board[dst] or board[dst].color == opositeColor(sq.piece.color)):
            moves.append( Move(sq.piece, sq.loc,dst) )
    return moves
    
    
def nop(board,sq):
    return []

movedict = {
    Shape.PAWN: possibleMovePawn,
    Shape.ROOK: possibleMoveRank,
    Shape.BISHOP: possibleMoveRank,
    Shape.QUEEN: possibleMoveRank,
    Shape.KING: possibleMoveShort,
    Shape.KNIGHT: possibleMoveShort,
    }
    
def possibleMoveSq(board, sq):
    assert isinstance(board,Board)
    assert isinstance(sq, Square)
    src = sq.loc
    piece = board[src]
    movefn = movedict[piece.shape]
    return movefn(board,sq)

def possibleMove(board, sq=None):
    if sq:
        return possibleMoveSq(board, sq)
    else:
        mvs = []
        for sq in board.army( board.nextmove ):
            mvs += possibleMoveSq(board,sq)
        return mvs
    pass


def executeMove( board, move ):
    assert isinstance(board,Board)
    assert isinstance(move, Move)


if __name__ == '__main__':
    b = Board()
    b.readFen('r1nb1kbn/rPppPppp/p7/8/2Q2P2/6N1/R5PP/2N2K2 w')
    print b
    
    mvs = []
    army = b.army( b.nextmove )
    for sq in army:
        mvs += possibleMove( b, sq )
        
    for mv in mvs:
        print mv
