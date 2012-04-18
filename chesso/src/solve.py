from game import Game
from pieces import Colors

fenLoyd = '8/8/8/6Q1/4R3/2K2p2/5k2/5b2 w'
fenBermudez = '8/8/4N1K1/8/8/3k1B2/1Q1b4/8 w'
fenMacleod = '1N3R2/4p3/rRq1k3/2P4B/2P5/5r2/6Qp/Bb4nK w'

fenFokin = 'K7/8/8/2Q5/8/3k4/6N1/3B4 w'


def cloneChainPlusOne(chain,tr):
    newchain = [ g.clone() for g in chain ]
    newchain.append(tr)
    return newchain

def mateIn1(gm):
    assert gm.nextmove == Colors.WHITE
    #print 'trying to do mate in 1 for:'
    #print gm
    tries = gm.childs( )
    for tr in tries:
        
        if tr.ismate( ):
            return tr
        else:
            pass        
    else:
        return None


def escapeIn1(gm):
    assert gm.nextmove == Colors.BLACK
    #print 'trying to find escape for:'
    #print gm
    tries = gm.childs( )
    if len(tries) == 0:
        return None
    chainlist = []
    for tr in tries:
        mt = mateIn1(tr)
        if mt:
            ch = [tr, mt]
            chainlist.append( ch )
        else:
            return None
    else:
        return chainlist

def mateIn2(gm):
    assert gm.nextmove == Colors.WHITE
    #print 'trying to find mate in two for:'
    #print gm
    tries = gm.childs( )
    for tr in tries:
        chainlist = escapeIn1( tr )
        if chainlist:
            return [ [tr] + ch for ch in chainlist ]
        else:
            pass
    else:
        return None


def mateInN(gm, n):
    assert gm.nextmove == Colors.WHITE
    if( n == 1 ):
        b = mateIn1( gm )
        if b:
            return [ [b] ]
        else:
            return None
    else:
        tries = gm.childs( )
        for tr in tries:
            chainlist = escapeInN( tr, n )
            if chainlist:
                return [ [tr] + ch for ch in chainlist ]
        return None
    

def escapeInN( gm, n ):
    assert gm.nextmove == Colors.BLACK
    tries = gm.childs( )
    chainlist = []
    for tr in tries:
        subchlist = mateInN( tr, n-1 )
        if subchlist:
            subchlist =[ [tr] + ch for ch in subchlist ]
            chainlist += subchlist
        else:
            return None
    else:
        return chainlist


def printChain( ch ):
    for g in ch:
        print g                        

def printChainList( chainlist ):
    for ch in chainlist:
        print '-------------'
        printChain( ch )

if __name__ == '__main__':
    gm = Game( )
    gm.readFen( fenLoyd )
    gm.readFen( fenMacleod )
    chainlist = mateInN(gm,2)
    
    #gm.readFen( fenFokin )
    #chainlist = mateInN( gm, 3 )
    
    printChainList( chainlist )
    
