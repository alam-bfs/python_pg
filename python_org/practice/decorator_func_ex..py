def decorator_function(orig_function):
    def wrapper_function(*args, **kwargs):
        print("add functionality without changing original function's functionality")
        return orig_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("i just display things")


@decorator_function
def display_info_with_args(name, age):
    print("i display details info. Name: {} and Age: {}".format(name, age))


if __name__ == "__main__":
    display()
    print("==================================================")
    display_info_with_args("Kaiser", 48)
