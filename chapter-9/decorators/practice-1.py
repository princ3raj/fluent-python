
def decorate(func):
    return func

@decorate
def target():
    return "Hello World"

"""This code has the same effect writing like this"""

def target():
    return "Hello World"

target = decorate(target)


def deco(func):
    def inner():
        print("Running Innner")
    return inner

@deco
def target():
    print("Running target")

'''

deco returns its inner function object.
target is decorated by deco.
Invoking the decorated target actually runs inner. 
Inspection reveals that target is a now a reference to inner.

'''

'''

1. A decorator is a function or another callable.
2. A decorator may replace the decorated function with a different one.
3. Decorators are executed immediately when a module is loaded

'''

'''
A key feature of decorators is that they run right
after the decorated function is defined. 
That is usually at import time (i.e., when a module is loaded by Python).
'''


