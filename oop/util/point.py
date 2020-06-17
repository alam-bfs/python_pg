class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __addition__(self):
        return self.x + self.y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


if __name__ == "__main__":
    p = Point(2, 3)
    p.__addition__()
    print(p)
