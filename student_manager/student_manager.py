# 2023/5/27  9:16
import json

def input_student():
    while True:
        stu_info = {}
        name = input('姓名：')
        chinese = input('语文：')
        math = input('数学：')
        english = input('英语：')
        stu_info['name']  = name if name else None
        stu_info['chinese']  = chinese if chinese else None
        stu_info['math'] = math  if math else None
        stu_info['english']  = english if english else None
        with open('stu_info.txt','a+',encoding='utf-8') as f:
            f.write(json.dumps(stu_info,ensure_ascii=False))
            f.write('\n')
        choice = input('是否继续添加学生信息(y/n)?： ')
        if(choice == 'y' or choice == 'Y'):
            pass
        else:
            break


def display_info():
    print('=' * 20 + '学生信息管理系统' + '=' * 20)
    print('-' * 22 + '功能菜单' + '-' * 22)
    print(' ' * 15 + '1.录入学生信息')
    print(' ' * 15 + '2.查找学生信息')
    print(' ' * 15 + '3.删除学生信息')
    print(' ' * 15 + '4.修改学生信息')
    print(' ' * 15 + '5.排序')
    print(' ' * 15 + '6.统计学生总人数')
    print(' ' * 15 + '7.显示所有学生信息')
    print(' ' * 15 + '0.退出系统')
    print('-' * 50)
    print()


def start_system():
    while True:
        #显示功能菜单
        display_info()

        #选择功能
        try:
            choice = int(input('请选择：'))
        except Exception as e:
            print(e.__str__(),'请重新选择！')
            continue

        if choice == 1:
            input_student()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 0:
            double_check = input('是否要退出系统(y/n)?: ')
            if double_check == 'y' or double_check == 'Y':
                return
            else:
                pass
        else:
            print('unrecognized input,input again.')



if __name__ == '__main__':
    start_system()