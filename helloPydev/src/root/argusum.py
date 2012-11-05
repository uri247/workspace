import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                     help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()

print args
print vars(args)
print 'integers: ',
for x in args.integers: print x,', ',
print
print args.accumulate
print 'accumulate: ', args.accumulate(args.integers)

