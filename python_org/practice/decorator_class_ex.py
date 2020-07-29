class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('add new functionality without changing existing functionality')
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print('display only')


@DecoratorClass
def display_with_info(name, age):
    print('display with info: Name: {}, Age: {}'.format(name, age))


if __name__ == '__main__':
    display()
    display_with_info('kaiser', 42)
