def primes(n):
    out = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p] and sieve[p] % 2 == 1:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


def primes2(n):
    out = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


from timeit import timeit

# print(timeit(lambda: primes(1_000_000), number=10))
# print(timeit(lambda: primes2(1_000_000), number=10))

print(len(primes(1_000)))
