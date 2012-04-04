'''
Created on Apr 3, 2012

@author: uri
'''

class Shape:
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
    ShapeTrait( Shape.PAWN, 'pawn', 'p' ),
    ShapeTrait( Shape.KNIGHT, 'knight', 'n' ),
    ShapeTrait( Shape.BISHOP, 'bishop', 'b' ),
    ShapeTrait( Shape.ROOK, 'rook', 'r' ),
    ShapeTrait( Shape.QUEEN, 'queen', 'q' ),
    ShapeTrait( Shape.KING, 'king', 'k' ),               
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
    def letter(self):
        l = ShapeTraits[self.shape].letter
        if self.color == Colors.WHITE:
            l = l.upper()
            return l

def pieceLetter(p):
    if p:
        return p.letter()
    else:
        return '.'
