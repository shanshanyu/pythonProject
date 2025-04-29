import random
def create_phone_number(n):
    dest_str = ''
    dest_str += '({}{}{}) {}{}{}-{}{}{}{}'.format(random.choice(n),random.choice(n),random.choice(n),random.choice(n),random.choice(n),random.choice(n),random.choice(n),random.choice(n),random.choice(n),random.choice(n))
    print(dest_str)


#  "(123) 456-7890"


if __name__ == '__main__':
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])