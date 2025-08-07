
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} eat')

    def run(self):
        print(f'{self.name} run')


class Teacher(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary

    def teach(self):
        print(f'{self.name} teach')


def main():
    t = Teacher('tom',32,1500)
    t.teach()

if __name__ == '__main__':
    main()
