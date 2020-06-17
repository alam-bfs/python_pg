def divisors_of(num):
    divisor_list = []
    for i in range(num):
        if i == 0:
            continue
        if num % i == 0:
            divisor_list.append(i)
    print(divisor_list)


if __name__ == "__main__":
    divisors_of(12)
