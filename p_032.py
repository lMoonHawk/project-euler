# https://projecteuler.net/problem=32

# We shall say that an n-digit number is pandigital if it makes use of all the
#   digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
#   through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
#   multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
#   can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
#   include it once in your sum.

from itertools import permutations


def main():
    def conc_int(iterable):
        """Concatenate iterable with single digits to a number using decimal
        expension"""
        return sum(
            digit * 10 ** (len(iterable) - 1 - i)
            for i, digit in enumerate(iterable)
        )

    valid_products = set()
    pand_prod = []

    for num in permutations(range(1, 10), 9):
        # Product has to be 4 digits long
        product = conc_int(num[-4:])
        if product in valid_products:
            continue
        # 4 possible "x" placement
        # We can check only 2 by symmetry with permutations above
        # m x mmmm = pppp
        # mm x mmm = pppp
        if (
            num[0] * conc_int(num[1:-4]) == product
            or conc_int(num[:2]) * conc_int(num[2:-4]) == product
        ):
            pand_prod.append(product)
            valid_products.add(product)

    print(sum(pand_prod))


if __name__ == "__main__":
    main()
