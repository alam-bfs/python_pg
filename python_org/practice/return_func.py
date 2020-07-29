from datetime import date


def maturity() -> date:
    return date(2020, 12, 31)


if __name__ == "__main__":
    print(maturity())
