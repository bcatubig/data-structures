# Input  : n = 2
# Output : 1

# Input  : n = 9
# Output : 34


def n_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a = 0
    b = 1

    for i in range(1, n):
        a, b = b, a + b
    return b

    # Recusive
    # return n_fib(n - 1) + n_fib(n - 2)


def main():
    print(n_fib(9))


if __name__ == "__main__":
    main()
