'''
create_time: 2024/2/28 17:20
author: yss
version: 1.0
'''

import argparse
parser = argparse.ArgumentParser()
# parser.add_argument('pos_arg',action='store',help='pos arg')  #位置参数
# parser.add_argument('--foo',action='store_true',help='foo help')  #可选参数

subparsers = parser.add_subparsers(dest='sub_action',required=True,description='操作')  #创建子解析器,dest用来保存子命令名称的属性名
#比如 python3 sub_parser.py a 1  那么 sub_action 的属性值就是 a，python3 sub_parser.py b 1， 那么 sub_action 的属性值就是 b
#print(type(subparsers))   <class 'argparse._SubParsersAction'>  #特殊动作对象
parser_a = subparsers.add_parser(name='a',help='a help')  #获得一个 ArgumentParser 对象
parser_a.add_argument('bar',type=int,help='bar help')

parser_b = subparsers.add_parser(name='b',help='b help')
parser_b.add_argument('barz',help='barz help')

parser_c = subparsers.add_parser(name='c',help='c help')

args = parser.parse_args()
print(dir(args))
print(args.sub_action)
