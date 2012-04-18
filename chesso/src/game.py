'''
Created on Apr 5, 2012

@author: uri
'''

from board import Board
from moves import Move, possibleMove, possibleMoveColor
from pieces import Shape, opositeColor

fenScholarMate = 'r1bqk1nr/pppp1Qpp/2n5/2b1p3/2B1P3/8/PPPP1PPP/RNB1K1NR b'
fenNotMate = 'r1bqk2r/pppp1Qpp/2n4n/2b1p3/2B1P3/8/PPPP1PPP/RNB1K1NR b'


class Game(Board):
    def __init__( self, other=None ):
        Board.__init__( self, other )
        pass

    def clone(self):
        copy = Game( self )
        return copy
        
    def executeMove(self,move):
        assert isinstance(self, Board)
        assert isinstance(move, Move)
        assert self[move.src]
        assert self[move.src].shape == move.pc.shape
        assert move.pc.color == self.nextmove
        assert move.dst
        assert not self[move.dst] or self[move.dst].color == opositeColor(self.nextmove)
        self[move.dst], self[move.src] = self[move.src], None
        self.nextmove = opositeColor(self.nextmove)

    def tryMove(self,move):
        newboard = self.clone( )
        newboard.executeMove( move )
        return newboard

    def canKillKing(self, color):
        mvs = possibleMoveColor( self, color )
        for mv in mvs:
            if self[mv.dst] and self[mv.dst].shape == Shape.KING:
                return True
        return False
                
    def isend(self):
        return self.canKillKing( self.nextmove )

    def isCheck(self):
        return self.canKillKing( opositeColor(self.nextmove) )
    
    def ismate(self):
        if not self.isCheck( ):
            return False
        mvs = possibleMove( self )
        for mv in mvs:
            b = self.tryMove( mv )
            if not b.isend( ):
                return False
        return True

    def childs(self):
        brds = []
        for mv in possibleMove( self ):
            b = self.tryMove(mv)
            if not b.isend():
                brds.append( (mv,b) )
        return brds


if __name__ == '__main__':
    gm = Game( )
    gm.readFen( fenScholarMate )
    print gm.ismate( )
    gm.readFen( fenNotMate )
    print gm.ismate( )
    
