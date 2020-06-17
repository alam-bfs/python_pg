import random


def get_number(first, last):
    return random.randint(first, last)


if __name__ == "__main__":
    guess = int(input("Guess a number: "))
    comp_pick = get_number(1, 9)
    if comp_pick == guess:
        print("you win. You pick {} and computer pick {}".format(guess, comp_pick))
    else:
        print("you lose. You pick {} and computer pick {}".format(guess, comp_pick))
