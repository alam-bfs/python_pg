def prime_num(num):
    if num > 1:
        for x in range(2, num):
            if num % x == 0:
                print("{} is not a prime number".format(num))
                break
        else:
            print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number".format(num))


if __name__ == "__main__":
    prime_num(10)
