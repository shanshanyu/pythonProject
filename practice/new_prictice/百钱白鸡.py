'''
公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
'''

def money_chicken():
    for x in range(0,21):
        for y in range(0,34):
            for z in range(0,101,3):
                if 5*x+3*y+1/3*z == 100 and x+y+z == 100:
                    print(x,y,z)


if __name__ == '__main__':
    money_chicken()