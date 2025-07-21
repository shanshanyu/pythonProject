'''100~999内的水仙花数'''
import math

def narcissistic():
    for i in range(100,1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a**3 + b**3 + c**3 == i:
            print(i)

if __name__ == '__main__':
    narcissistic()