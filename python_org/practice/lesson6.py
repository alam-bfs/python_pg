import argparse

parser = argparse.ArgumentParser("description=Find Palindrome word")
parser.add_argument('-s', '--string', metavar='', help='string is palindrome or not')
args = parser.parse_args()


def palindrome_word(string):
    if string[::-1] == string:
        print("{} is a palindrome word".format(string))
    else:
        print("{} is not a palindrome word".format(string))


if __name__ == "__main__":
    palindrome_word(str(args.string))
