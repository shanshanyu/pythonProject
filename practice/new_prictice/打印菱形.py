'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

def print_diamond(n):
    if n < 4:
        print('请输入大于3的数字')
    for i in range(n):
        for  j in range(n-i-1):
            print(' ',end='')
        for k in range(2*i+1):
            print('*',end='')
        print()
    for i in range(n-1):
        for j in range(i+1):
            print(' ',end='')
        for k in range(2*(n-i-1-1)+1):
            print('*',end='')
        print()

def print_diamond_new(n):
    for i in range(1,n,2):
        spaces = ' ' * ((n-i)//2)
        stars = '*' * i
        print(spaces + stars)
    for i in range(n,0,-2):
        spaces = ' ' * ((n - i) // 2)
        stars = '*' * i
        print(spaces + stars)








if __name__ == '__main__':
    print_diamond_new(7)