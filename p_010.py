# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def main():
    k = 3
    count = 2
    while k < 2_000_000 - 2:
        is_prime = True
        for i in range(2, int(k**0.5) + 1):
            if not k % i:
                is_prime = False
                break

        if is_prime:
            count += k

        k += 2

    print(count)


if __name__ == "__main__":
    main()
