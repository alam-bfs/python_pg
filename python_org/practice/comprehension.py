
# args = positional arguments
# *args = all arguments in tuple
# **kwargs = all keyword arguments
# when invoke foo(), first and second argument is positional arguments
# all the arguments up to key=value will be tuple and key=value will dictionary


def foo(args1, args2, *args, **kwargs):
    print(args1)
    print(args2)
    print(args)
    print(kwargs)


if __name__ == "__main__":
    foo(1, 2, "emp_id", "0001", a="apple", b="ball")
    foo(1, 2, "emp_id", "0002", a="apple", b="ball")
    foo(1, 2, 10001, 1010101, a="apple", b="ball")
