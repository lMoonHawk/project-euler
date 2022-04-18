# https://projecteuler.net/problem=50

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below
#   one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a
#   prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most
#   consecutive primes?


from itertools import accumulate


def main():
    def is_prime(n):
        if n == 1:
            return False

        up_to = int(n**0.5)

        if n % 2:
            start, step = 3, 2
        else:
            start, step = 2, 1

        for i in range(start, up_to + 1, step):
            if not n % i:
                return False
        return True

    def gen_primes(i):
        while True:
            if is_prime(i):
                yield i
            i += 1

    answer = 0
    start, dist_max = 1, 1
    stop = False
    while not stop:
        # Assume stop, if dist_max is never reached
        #   starting from this prime number, loop ends
        stop = True
        for i, prime_test in enumerate(accumulate(gen_primes(start))):
            if prime_test > 1_000_000:
                break
            if i + 1 <= dist_max:
                continue

            stop = False

            if is_prime(prime_test):
                dist_max = i + 1
                answer = prime_test

        start += 1
    print(answer)


if __name__ == "__main__":
    main()
