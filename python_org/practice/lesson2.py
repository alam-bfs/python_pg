import argparse


def num_check(num):
    return "{} is even number".format(num) if num % 2 == 0 else "{} is odd number".format(num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process integer for Even or Odd')
    parser.add_argument('integers', metavar='N', type=int, help='an integer for the even odd number')
    args = parser.parse_args()
    print(num_check(args.integers))
