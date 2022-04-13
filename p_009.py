# https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main():
    for a in range(1, 1000):
        # c = sqrt(a^2+b^2)
        # c = 1000 - a - b
        # sqrt(a^2+b^2) = 1000 - a - b
        # Real solutions for b = (1000 * (a - 500)) / (a - 1000)
        b = (1000 * (a - 500)) / (a - 1000)
        # Check for natural number
        if int(b) == b:
            break

    print(int(a * b * (1000 - a - b)))


if __name__ == "__main__":
    main()
