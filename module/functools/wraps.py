# 2024/8/4  15:40
'''
functools.wraps(wrapped,assigned=WRAPPER_ASSIGNMENTS,updated=WRAPPER_UPDATES)
用于定义包装器函数时发起调用update_wrapper()作为函数装饰器，等价于
partial(update_wrapper,wrapped=wrapped,assigned=assigned,updated=updated) 就相当于调用
update_wrapper(wrapped,assigned,updated)


functools.partial(func,/,*args,**kwargs)
返回一个新的部分对象，当被调用时其行为类似于func附带位置参数args和关键字参数kwargs被调用。

partial函数固定普通参数收集*args

functools.update_wrapper(wrapper,wrapped,assigned=WRAPPER_ASSIGNMENTS,updated=WRAPPER_UPDATES)

functools.wraps(xx) == partial(update_wrapper,xx) == update_wrapper(xx)
'''


# 函数执行时间的装饰器

import functools
import time


def time_spend(func):
    '''
        这是一个装饰器函数
    '''

    '''
    def wraps(wrapped, assigned = functools.WRAPPER_ASSIGNMENTS, updated = functools.WRAPPER_UPDATES):
        def decorator(wrapper):
            functools.update_wrapper(wrapper, wrapped, assigned, updated)
            return wrapper
        return decorator

    '''
    '''
    import functools

    def update_wrapper(wrapper, wrapped, assigned=functools.WRAPPER_ASSIGNMENTS, updated=functools.WRAPPER_UPDATES):
        for attr in assigned:
            setattr(wrapper, attr, getattr(wrapped, attr))
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
        wrapper.__wrapped__ = wrapped
        return wrapper
    '''
    @functools.wraps(func)
    def test(*args,**kwargs):  # test = decorator   调用test就等价于调用funtools.update_wrapper(wrapper,func)
        # 开始时间
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'speed {end-start}s')

    return test

def get_primer():
    '''
        计算1~10000的质数
    '''
    for i in range(2,10001):
        # 计算质数
        if i == 2 or i == 3:
            print(i)
            continue
        flag = True
        for j in range(2,int(i/2)+1):
            if i%j == 0:
                continue
        if flag:
            print(i)


def main():
    time_spend(get_primer)()


if __name__ == '__main__':
    main()


