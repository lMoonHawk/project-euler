# https://projecteuler.net/problem=27

# Euler discovered the remarkable quadratic formula: n^2+n+41

# It turns out that the formula will produce 40 primes for the consecutive
#   integer values 0 <= n <= 39. However, when n=40,
#   40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
#   and certainly when n=41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n^2 - 79n + 1601 was discovered, which produces
#   80 primes for the consecutive values 0 <= n <= 79.
#   The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
#   n^2 + an + b, where |a| < 1000 and |b| < 1000
#   where |n| is the modulus/absolute value of n
#   e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients a and b for the quadratic expression
#   that produces the maximum number of primes for consecutive values of n,
#   starting with n=0.


def main():
    def primes(n):
        out = []
        sieve = [True] * (n + 1)
        for p in range(2, n + 1):
            if sieve[p] and sieve[p] % 2 == 1:
                out.append(p)
                for i in range(p, n + 1, p):
                    sieve[i] = False
        return out

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                return False
        return True

    max_primes = 0
    for a in range(-999, 1_000, 2):  # a must be odd of n=1
        for b in primes(1_000):
            n = 0
            while is_prime(n**2 + a * n + b):  # b must be prime for n=0
                n += 1
            if n > max_primes:
                answer = a * b
                max_primes = n
    print(answer)


if __name__ == "__main__":
    main()
