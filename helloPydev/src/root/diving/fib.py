'''
Created on Mar 22, 2012

@author: uri
'''

def fib(n):
    """calculate Fibonaci recursively
    """
    
    if n == 0:
        f = 1
    elif n == 1:
        f = 1
    else:
        f = fib(n-2) + fib(n-1)

    #print 'fib(',n,') = ',    
    #print f    
    return f

if __name__ == '__main__':
    for x in range(35):
        print '{0:3d} {1:12d}'.format(x,fib(x))
