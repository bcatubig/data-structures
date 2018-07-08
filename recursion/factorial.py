def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def main():
    num = factorial(8)
    print(num)


if __name__ == "__main__":
    main()
