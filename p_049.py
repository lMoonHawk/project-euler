# https://projecteuler.net/problem=49


# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
#   increases by 3330, is unusual in two ways: (i) each of the three terms are
#   prime, and, (ii) each of the 4-digit numbers are permutations of one
#   another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
#   exhibiting this property, but there is one other 4-digit increasing
#   sequence.

# What 12-digit number do you form by concatenating the three terms in this
#   sequence?


from itertools import combinations_with_replacement, permutations


def main():
    def is_prime(n):
        if n == 1 or n % 2 == 0:
            return False
        if n == 2:
            return True

        up_to = int(n**0.5)

        for i in range(3, up_to + 1, 2):
            if not n % i:
                return False
        return True

    def conc_int(iterable):
        """Concatenate iterable with single digits to a number using decimal
        expension"""
        return sum(
            digit * 10 ** (len(iterable) - 1 - i)
            for i, digit in enumerate(iterable)
        )

    for digits in combinations_with_replacement(range(0, 10), 4):
        perms = [
            conc_int(perm) for perm in permutations(digits) if perm[0] != 0
        ]
        for i in range(len(perms)):
            if not is_prime(perms[i]):
                continue
            for j in range(i + 1, len(perms)):
                if not is_prime(perms[j]):
                    continue
                for k in range(j + 1, len(perms)):
                    if not is_prime(perms[k]):
                        continue
                    if (
                        perms[i] != perms[j] != perms[k]
                        and perms[j] - perms[i] == perms[k] - perms[j]
                        and perms[i] != 1487
                    ):
                        answer = (
                            perms[i] * 10**8 + perms[j] * 10**4 + perms[k]
                        )
                        break

    print(answer)


if __name__ == "__main__":
    main()
