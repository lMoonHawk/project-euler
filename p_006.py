# https://projecteuler.net/problem=6

# The sum of the squares of the first ten natural numbers is,
#   1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
#   numbers and the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred
#   natural numbers and the square of the sum.


def main():
    def brute_force():
        c = sum(m * n for m in range(1, 101) for n in range(1, 101) if m != n)
        print(c)

    def formula():
        sum_sq = (100 * (100 + 1) * (2 * 100 + 1)) // 6
        sq_sum = (100 * (100 + 1) // 2) ** 2
        print(sq_sum - sum_sq)

    # brute_force()
    formula()


if __name__ == "__main__":
    main()
