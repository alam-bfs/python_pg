import sys
from datetime import date, datetime


# Python version
def python_version():
    print(sys.version)


# display current date and time
def get_curr_datetime():
    print(date.today(), datetime.now().strftime("%H:%M:%S"))


# display file extension
def get_file_extension():
    print("abc.txt".split(".")[-1])


# display first and last color of string
def get_first_last_string():
    item_list = ["car", "house", "business", "family"]
    print(item_list[0], item_list[-1])


def reverse_string():
    print("car"[::-1])
    print(''.join(reversed("google")))


if __name__ == "__main__":
    python_version()
    get_curr_datetime()
    get_file_extension()
    get_first_last_string()
    reverse_string()
