'''
create_time: 2024/4/9 17:13
author: yss
version: 1.0
desc: optoolkit 命令行入口
'''
from tools.menu import Menu


def main():
    m = Menu()
    steps = [
        "Allinone Check",
        "Calculate Kudu Tserver Metadata Size",
        "Process Notify",
        "Start Sensors Product",
        "Stop Sensors Product",
        "Auto Event Delete",
        "Migration Evaluation",
        "Zookeeper_maxClientCnxns Change",
        "Change IP",
        "Fix docker0",
        "test1",
        "test2"
    ]
    m.draw(steps,title=['optoolkit','abc'],guide="【Select】↑ ↓ 【choose】Enter 【Search】s/S 【Quit】q/Q/b/B\
【Page】g/l")


if __name__ == '__main__':
    main()