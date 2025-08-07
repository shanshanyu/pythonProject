'''员工工资结算：
某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
其中，部门经理的月薪是固定 15000 元；
（以小时为单位）支付月薪，每小时 200 元；
销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。
'''

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    '''抽象基类'''
    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):
    def salary(self):
        return 15000

class Programmer(Employee):
    def __init__(self, name,work_hour=0):
        super().__init__(name)
        self.work_hour = work_hour

    def salary(self):
        return 200 * self.work_hour

class Salesman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales = sales

    def salary(self):
        return 1500 + self.sales * 0.05


def main():
    employees = [Manager('曹操'),Programmer('张辽'),Programmer('吕布'),Salesman('荀彧')]
    for emp in employees:
        if isinstance(emp, Programmer):
            emp.work_hour =int(input(f'请输入{emp.name}工作时间：'))
        if isinstance(emp, Salesman):
            emp.sales = int(input(f'请输入{emp.name}销售额：'))
        print(emp.name,emp.salary())


if __name__ == '__main__':
    main()




