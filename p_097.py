# https://projecteuler.net/problem=97

# The first known prime found to exceed one million digits was discovered in
#   1999, and is a Mersenne prime of the form 26972593−1; it contains exactly
#   2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1,
#   have been found which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains
#   2,357,207 digits: 28433×27830457+1.

# Find the last ten digits of this prime number.


def main():
    # Binary exponentiation to get even faster result using
    #   square and multiply algorithm.
    # At each step we mod by 10^10 because we only care about the
    #   10 last digits (instead of moding a > 2m digits number)

    base = 2
    exp = 7830457
    mod = 10**10

    exp_bin = f"{exp:b}"
    num = base
    for bit in exp_bin[1:]:
        num *= num
        if bit == "1":
            num *= base
        num %= mod
    print(str(num * 28433 + 1)[-10:])


if __name__ == "__main__":
    main()
