'''
create_time: 2023/5/5 10:25
author: yss
version: 1.0
'''

import argparse
parser = argparse.ArgumentParser(description="hello")

#print(type(parser))

parser.add_argument('-a',action="store_true",default=False)
parser.add_argument('-b',action="store",dest='b')

args = parser.parse_args(['-a','-bhaha'])
print(args)

print("{} {}".format(args.a,args.b))