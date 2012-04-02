'''
Created on Mar 22, 2012

@author: uri
'''

def fibRec(n):
    """calculate Fibonaci recursively
    """
    f = n==0 and 1 or n==1 and 1 or fibRec(n-2) + fibRec(n-1)
    return f

def fibIt(n):
    """Calculate Fibonaci iteratively
    """
    a, b = 1, 1
    for x in range(1,n):
        x
        a, b = b, a+b
    return b


if __name__ == '__main__':
    for pair in [(fibRec, 'Recursive Algorithm'),(fibIt, 'IterativeAlgorithm')]:
        al = pair[0]
        print pair[1]
        for x in range(30):
            print '{0:3d} {1:12d}'.format( x, al (x) )
