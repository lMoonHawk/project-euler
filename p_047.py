# https://projecteuler.net/problem=47

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors
#   each. What is the first of these numbers?


def main():
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True

        up_to = int(n**0.5)

        for i in range(3, up_to + 1, 2):
            if not n % i:
                return False
        return True

    def prime_fact(n):
        out = []
        i = 2
        while n > 1:
            if n % i == 0:
                n //= i
                out.append(i)
            else:
                i += 1
        return out

    found = False
    i, count = 3, 0
    while not found:
        i += 1

        if not is_prime(i) and len(set(prime_fact(i))) == 4:
            count += 1
            if count == 4:
                found = True
        else:
            count = 0

    print(i - 3)


if __name__ == "__main__":
    main()
