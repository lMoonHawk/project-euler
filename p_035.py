# https://projecteuler.net/problem=35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


def main():
    def rotations(x: int):
        x = str(x)
        for i in range(len(x)):
            yield int(x[i:] + x[:i])

    def is_prime(n):
        up_to = int(n**0.5)

        if n % 2:
            step = 2
            start = 3
        else:
            step = 1
            start = 2

        for i in range(start, up_to + 1, step):
            if not n % i:
                return False
        return True

    count = 1  # accounts for 2
    for i in range(3, 1_000_000, 2):
        if all(is_prime(perm) for perm in rotations(i)):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
