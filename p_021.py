# https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n
#   (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
#   each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are
#   1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#   The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


from itertools import combinations


def main():
    def d(n):
        result = 1
        up_to = int(n**0.5)
        result += up_to if up_to**2 == n else 0

        step = 2 if n % 2 else 1
        for i in range(2, up_to, step):
            result += i + n // i if not n % i else 0
        return result

    memo = {}
    count = 0
    for a, b in combinations(range(2, 10_000), 2):
        if a in memo:
            d_a = memo[a]
        else:
            d_a = d(a)
            memo[a] = d_a

        if b in memo:
            d_b = memo[b]
        else:
            d_b = d(b)
            memo[b] = d_b

        count += d_a + d_b if d_a == b and d_b == a else 0

    print(count)


if __name__ == "__main__":
    main()
