# 2023/5/27  9:16

import os.path

filename = 'stu_info.txt'

def find_student():
    pass

def delete_student():
    while True:
        stu_lst = []
        if os.path.exists(filename):
            stu_name = input('请输入需要删除的学生姓名：')
            if stu_name == '':  #判断字符串是否为空
            #if not stu_name:
                print('输入的学生姓名为空，请重新输入！')
                continue

            #读取信息放到列表中
            with open(filename,'r',encoding='utf-8') as file:
                stu_list = file.readlines()

            flag = False
            #在列表中修改信息
            for item in stu_list:
                #item = eval(item.strip())  #eval把字符串转换成字典
                if stu_name == eval(item)['name']:   #每个 item 是一个包裹字典的字符串
                    stu_list.remove(item)
                    flag = True
                    with open(filename, 'w', encoding='utf-8') as file :
                        for d in stu_list :
                            file.write(d)
                            break

            if flag:
                print(f'学生{stu_name}信息删除完成')
            else:
                print(f'未找到学生{stu_name}')
        else:
            print('学生信息为空！')

        answer = input('是否继续删除学生信息(y/n)?: ')
        if answer == 'y' or answer == 'Y':
            pass
        else:
            break

def update_student():
    while True:
        stu_list = []
        if os.path.exists(filename) :
            stu_name = input('请输入需要修改的学生姓名：')
            #if stu_name == '' :  # 判断字符串是否为空
            if not stu_name:
                print('输入的学生姓名为空，请重新输入！')
                continue

            # 读取信息放到列表中
            with open(filename, 'r', encoding='utf-8') as file :
                stu_list = file.readlines()

            file = open(filename,'w',encoding='utf-8')


            flag = False
            for item in stu_list:
                if stu_name == eval(item)['name']:
                    flag = True
                    print(f'找到学生{stu_name},请修改！')
                    student = {}
                    student['name']  = stu_name
                    try:
                        student['chinese']  = int(input('语文：'))
                        student['math'] = int(input('数学：'))
                        student['english'] = int(input('英语：'))
                    except:
                        print('输入的学生成绩不是数字，请重新输入！')

                    file.write(str(student)+'\n')
                else:
                    file.write(item)

                if flag:
                    print(f'学生{stu_name}信息修改完成！')
                else:
                    print(f'学生{stu_name}未找到')

            answer = input('是否继续修改学生信息(y/n)?: ')
            if answer == 'y' or answer == 'Y':
                pass
            else:
                break
        else:
            print('学生信息为空！')
            break



def sort_student():
    pass

def count_student():
    pass

def display_all_student():
    pass

def insert_student():
    while True:
        student = {}
        name = input('姓名：')
        if name == '':
            continue
        student['name'] = name
        #需要判断的分数是不是整数
        try:
            chinese = int(input('语文：'))
            math = int(input('数学：'))
            english = int(input('英语：'))
        except:
            print("输入的分数不是一个整数,请重新输入！")
            continue
        student['chinese'] = chinese
        student['math'] = math
        student['english'] = english

        with open(filename,'a',encoding='utf-8') as file:
            file.write(str(student)+'\n')

        print(f'学生{name}插入完成！')
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
            insert_student()
        elif choice == 2:
            find_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            update_student()
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