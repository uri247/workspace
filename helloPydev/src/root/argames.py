import argparse
br = '\n\n' + ''.join('-' for x in xrange(60)) 

def varg(cmdline):
    return cmdline.split()

def p(parser,cmdline):
    print
    print 'cmdline: ', cmdline
    ns = parser.parse_args( cmdline.split() )
    print 'result: ', ns
    return ns

def game1():
    print br
    parser = argparse.ArgumentParser( prog='game1' )
    parser.print_help();

def game2():
    print br
    parser = argparse.ArgumentParser( prog='game2' )
    parser.add_argument( '-f', '--foo' )
    parser.print_help()
    p( parser, '--foo 8' ) 

def game3():
    print br
    parser = argparse.ArgumentParser( prog='game3' )
    parser.add_argument( '--foo', action='store_const', const=42 )
    parser.add_argument( '--bar', action='store_true'  )
    parser.add_argument( '--beh', action='store_false' )
    parser.add_argument( '--biz' )
    parser.print_help()
    p(parser,'')
    p(parser,'--foo --bar --biz 8')
    p(parser,'--foo --beh')

def game4():
    print br
    parser = argparse.ArgumentParser( prog='game4' )
    parser.add_argument( '--ex', action='append', dest='exlist' )
    parser.print_help()
    p(parser,'--ex *.foo --ex *.bar')

def game5():
    print br
    parser = argparse.ArgumentParser( prog='game5' )
    parser.add_argument( '--str', action='append_const', const=str, dest='types' )
    parser.add_argument( '--int', action='append_const', const=int, dest='types' )
    parser.add_argument( '--version', '-v', action='version', version='%(prog)s 2.0')
    parser.print_help()
    p( parser, '--int --str' )
    #p( parser, '-v' )  #will exit
    
def game6():
    print br
    parser = argparse.ArgumentParser( prog='game6' )
    parser.add_argument( 'src', metavar='source file' )
    parser.add_argument( 'dst', metavar='destination file' )
    parser.print_help()
    p( parser, 'here there' )

def game7():
    print br
    parser = argparse.ArgumentParser( prog='game7' )
    parser.add_argument( '-s', nargs=2 )
    parser.print_help()
    p( parser, '-s 4 5' )

def game8():
    print br
    parser = argparse.ArgumentParser( prog='game8' )
    parser.add_argument( '-opt', nargs='?', default='no switch', const='switch with no arg' )
    parser.print_help()
    p( parser, '' )
    p( parser, '-opt')
    p( parser, '-opt switch-and-arg')

def game9():
    print br
    parser = argparse.ArgumentParser( prog='game9' )
    parser.add_argument( 'numbers', nargs='*', type=int )
    parser.print_help()
    ns = p( parser, '1 2 3 4 5')
    print 'sum: ', sum(ns.numbers)
    ns = p( parser, '')
    print 'sum: ', sum(ns.numbers)
    

if __name__ == '__main__':
    game1()
    game2()
    game3()
    game4()
    game5()
    game6()
    game7()
    game8()
    game9()

