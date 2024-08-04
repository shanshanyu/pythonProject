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
def my_decorator(func):
    @functools.wraps(func)
    def test1(*args, **kwargs):
        print("Calling decorated function")
        return func(*args, **kwargs)
    return test1

@my_decorator
def say_hello():
    """This is a docstring."""
    print("Hello!")

say_hello()

print(say_hello.__name__)  # 输出: say_hello
print(say_hello.__doc__)   # 输出: This is a docstring.
