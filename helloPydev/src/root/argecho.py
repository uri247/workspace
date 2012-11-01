import sys
import getopt

#
# list style print of argv
#
print sys.argv,'\n\n'

#
# print each argument in a line
#
for i,arg in enumerate(sys.argv):
    print "%2i.%s" % (i, arg)  


#
# the Unix getopt style parsing
try:
    opts, args = getopt.getopt( sys.argv[1:], 
                                "hfgt:p:",
                                [ 'help', 'float', 'grammer', 'time=', 'print='] )
except getopt.GetoptError:
    print "Usage:"
    sys.exit(-2)
for opt, arg in opts:
    if opt in ('-h', '--help'):
        print "Usage:"
        sys.exit()
    elif opt in ('-f', '--float'):
        print "Debug!"
    elif opt in ('-g', '--grammer'):
        print "Grammer"
    elif opt in ('-t' '--time'):
        print "time", arg
    elif opt in ('-p', '--print'):
        print "print", arg
        
    
            



