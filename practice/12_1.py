'''
create_time: 2023/5/30 21:08
author: yss
version: 1.0
'''

student_lst = []

class Student():

    __test = 'a'
    def __init__(self,name,age,sex,score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def add(self):
        tmp_lst = [self.name,self.age,self.sex,self.score]
        student_lst.append(tmp_lst)

    def show(self):
        for item in student_lst:
            for i in item:
                print(i,end='\t')
            print()


if __name__ == '__main__':
    print(Student._Student__test)  #python 的封装，通过 _classname[__propertyname]
    for i in range(5):
        stu_info = input(f'请输入第{i+1}位学生的信息：')
        tmp_lst = stu_info.split('#')
        s = Student(*tmp_lst)  #逆向参数收集
        s.add()
    s.show()


