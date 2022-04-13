# https://projecteuler.net/problem=23

# A perfect number is a number for which the sum of its proper divisors is
#   exactly equal to the number. For example, the sum of the proper divisors
#   of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
#   number.

# A number n is called deficient if the sum of its proper divisors is less
#   than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
#   number that can be written as the sum of two abundant numbers is 24.
#   By mathematical analysis, it can be shown that all integers greater than
#   28123 can be written as the sum of two abundant numbers. However, this
#   upper limit cannot be reduced any further by analysis even though it is
#   known that the greatest number that cannot be expressed as the sum of two
#   abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
#    of two abundant numbers.


def main():
    def is_abundant(n):
        result = 1
        up_to = int(n**0.5)

        if up_to**2 == n:
            result += up_to
            up_to -= 1

        if n % 2:
            step = 2
            start = 3
        else:
            step = 1
            start = 2

        for i in range(start, up_to + 1, step):
            result += i + n // i if not n % i else 0
            if result > n:
                return True
        return False

    abundants = []
    for i in range(28_124):
        if is_abundant(i):
            abundants.append(i)

    tab = [True] * 28_123
    for a in abundants:
        for b in abundants:
            if a + b < 28_123:
                tab[a + b] = False

    print(sum(i for i, x in enumerate(tab) if x))


if __name__ == "__main__":
    main()
