import logging


def my_logger(original_function):
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper


@my_logger
def display():
    print('display only')


@my_logger
def display_info(name, age):
    print('display with info, Name: {}, Age: {}'.format(name, age))


if __name__ == '__main__':
    display_info('kaiser', 48)


