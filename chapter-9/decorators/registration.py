'''

registry will hold references to functions decorated by @register.
register takes a function as argument.
Display what function is being decorated, for demonstration. Include func in registry.
Return func: we must return a function; here we return the same received as argument.
f1 and f2 are decorated by @register.
f3 is not decorated.
main displays the registry, then calls f1(), f2(), and f3(). main() is only invoked if registration.py runs as a script.


'''

registry = []
def register(func):
    print(f"running register ({func})")
    registry.append(func)
    return func

@register
def f1():
    print(f"running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()
