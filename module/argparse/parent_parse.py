'''
create_time: 2024/2/29 14:19
author: yss
version: 1.0
'''
import argparse
parent_parser = argparse.ArgumentParser(add_help=False)  #创建一个解析器
parent_parser.add_argument('--parent', type=int)  #指定一个参数 --parent


foo_parser = argparse.ArgumentParser()  #创建一个解析器，指定父解析器,也就是会使用父解析器中的参数
sub_parser = foo_parser.add_subparsers(description='操作')

sub_parser.add_parser(name='sub test',help='sb test',parents=[parent_parser])
foo_parser.parse_args()