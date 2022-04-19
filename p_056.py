# https://projecteuler.net/problem=56

# A googol (10100) is a massive number: one followed by one-hundred zeros;
#   100100 is almost unimaginably large: one followed by two-hundred zeros.
#   Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the
#   maximum digital sum?


def main():
    answer = max(
        [
            sum(int(digit) for digit in str(a**b))
            for a in range(1, 100)
            for b in range(1, 100)
        ]
    )
    print(answer)


if __name__ == "__main__":
    main()
