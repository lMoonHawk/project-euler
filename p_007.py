# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
#   that the 6th prime is 13.

# What is the 10 001st prime number?


def main():
    primes = [2]
    k = 1
    while len(primes) != 10001:
        k += 2
        is_prime = True
        for prime in primes:
            if not k % prime:
                is_prime = False
                break

        if is_prime:
            primes.append(k)

    print(primes[-1])


if __name__ == "__main__":
    main()
