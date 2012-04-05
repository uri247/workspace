'''
Created on Apr 5, 2012

@author: uri
'''

from board import Board
from moves import Move, possibleMove
from pieces import Shape, opositeColor

class Game(Board):
    def __init__(self):
        Board.__init__( self )
        pass

    def isend(self):
        mvs = possibleMove(self)
        for mv in mvs:
            if self[mv.dst] and self[mv.dst].shape == Shape.KING:
                return True
        return False
    
    def executeMove(self,move):
        assert isinstance(self, Board)
        assert isinstance(move, Move)
        assert self[move.src]
        assert self[move.src] == move.pc
        assert move.pc.color == self.nextmove
        assert move.dst
        assert not self[move.dst] or self[move.dst].color == opositeColor(self.nextmove)
        self[move.dst], self[move.src] = self[move.src], None
        

if __name__ == '__main__':
    gm = Game( )
    gm.readFen('r1nb1kbn/rPppPppp/p7/8/2Q2P2/6N1/R5PP/2N2K2 w')
    print gm.isend( )