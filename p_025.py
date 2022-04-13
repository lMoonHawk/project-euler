# https://projecteuler.net/problem=25

# The Fibonacci sequence is defined by the recurrence relation:

#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain
#   1000 digits?


def main():
    def fib(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

    digit_count = 0
    i = 12
    while digit_count < 1_000:
        i += 1
        current = fib(i)
        digit_count = len(str(current))

    print(i)


if __name__ == "__main__":
    main()
