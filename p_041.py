# https://projecteuler.net/problem=41

# We shall say that an n-digit number is pandigital if it makes use of all the
#   digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and
#   is also prime.

# What is the largest n-digit pandigital prime that exists?


from itertools import permutations


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

    def conc_int(iterable):
        """Concatenate iterable with single digits to a number using decimal
        expension"""
        return sum(
            digit * 10 ** (len(iterable) - 1 - i)
            for i, digit in enumerate(iterable)
        )

    found = False
    digits = 9
    while not found:
        for num in permutations(range(digits, 0, -1), digits):
            if is_prime(conc_int(num)):
                found = True
                break
        digits -= 1
    print(conc_int(num))


if __name__ == "__main__":
    main()
