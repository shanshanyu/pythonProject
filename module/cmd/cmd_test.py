'''
create_time: 2024/1/19 11:12
author: yss
version: 1.0
'''

import cmd
import sys

class AdminShell(cmd.Cmd):
    def __init__(self):
        #子类重写父类的构造方法，需要调用父类的构造方法
        super().__init__()

    def do_exit(self):
        print('tomorrow is another day.Bye ~')
        return True

    def default(self,line):
        return self.do_exit()



def main():
    if len(sys.argv) == 1:
        shell = AdminShell()
        shell.cmdloop()
        print('over')


if __name__ == '__main__':
    pass
