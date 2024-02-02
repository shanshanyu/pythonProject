# 2023/5/13  9:12

def div(a,b):
    return a/b

def get_float():
    num = float(input(': '))
    return num

if __name__ == '__main__':
    try:
        num = get_float()
    except ZeroDivisionError:  #except 可以捕获到异常
        print("error")
    except:
        print('error occur')
        raise
