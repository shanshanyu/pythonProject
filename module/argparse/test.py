'''
create_time: 2023/5/5 10:25
author: yss
version: 1.0
'''
import sys
import argparse
parser = argparse.ArgumentParser(description="hello")   #创建一个 ArgumentParser对象,是一个解析器

#print(type(parser))

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
#print(args)

#print("{} {}".format(args.a,args.b))

print(args.accumulate)
print(args.integers)
