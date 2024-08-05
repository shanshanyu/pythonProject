# 2024/8/4  17:45
import functools

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

'''
test1 = functools.wrap(func)(test1) = decorator(test1) = test1
functools.update_wrapper(test1, func)
return test1  

'''
'''
my_decorator这个装饰器，用这个装饰器装饰其他函数，其他函数会变成 test1,但是其他属性被被复制过来
'''

def my_decorator(func):
    @functools.wraps(func)  #会把func 的一些元数据复制给test1
    def test1(*args, **kwargs):
        print("Calling decorated function")
        return func(*args, **kwargs)
    return test1


@my_decorator   # hello = my_decorator(say_hello) = test1
def say_hello():
    """This is a docstring."""
    print("Hello!")



say_hello()

print(say_hello.__name__)  # 输出: say_hello
print(say_hello.__doc__)   # 输出: This is a docstring.

