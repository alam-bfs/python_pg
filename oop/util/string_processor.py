class StringProcessor:
    def __init__(self, string):
        self.string = string

    def rev_string(self):
        return self.string[::-1]


if __name__ == "__main__":
    StringProcessor = StringProcessor("car")
    print(StringProcessor.rev_string())