import os
import itertools
root1 = 'c:\\uri\\workspace'
root2 = 'c:\\uri\\workspace\\helloPydev'

#
# Walking without .svn and .git
#
def smart_walk():
    for root, dirs, files in os.walk(root1):
        size = sum( [os.path.getsize(os.path.join(root,fname)) for fname in files ] )
        print "{0:60}{1:10} bytes in {2:6} files".format( root, size, len(files) )
        for ex in ('.git','.svn', '.metadata'):
            if ex in dirs:
                dirs.remove( ex )

def nested_comp():
    allfiles = [os.path.join(root,f) for root,_,files in os.walk(root2) for f in files]
    #sort by size
    for fname in sorted( allfiles, key=os.path.getsize ):
        print fname, os.path.getsize(fname)
    
    
def lambada():
    ls = [10, -50, 30, 40, -20]
    
    print 'unsorted: ',
    for x in ls: print x,
    print
    
    print 'sorted: ',
    for x in sorted(ls): print x,
    print
    
    print 'abs sorted: ',
    for x in sorted(ls, key = lambda x: abs(x) ): print x,
    print
    
def grouping():
    ls = [('uri',20), ('uri',50), ('uri', 80), ('michal',15), 
          ('michal', 55), ('dana', 30), ('michal',5), ('dana',10)]
    di = dict();
    keyfn = lambda x: x[0]
    for k, g in itertools.groupby( sorted(ls,key=keyfn), keyfn ):
        di[ k ] = list(g)
    print di['uri']
    pass

def permute():
    def inserts(st,ch):
        return [ st[:i]+ch+st[i:] for i in xrange(len(st),-1,-1) ]
    def step(ls,ch):
        return [est for st in ls for est in inserts(st,ch)]
    print reduce( step, list('abcd'), [''] )
    
def main():
    smart_walk()
    nested_comp()
    lambada()
    grouping()
    permute()
    

if __name__ == '__main__':
    main()
    
