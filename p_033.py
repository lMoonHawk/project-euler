# https://projecteuler.net/problem=33


# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
#   in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
#   which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less
#   than one in value, and containing two digits in the numerator and
#   denominator.

# If the product of these four fractions is given in its lowest common terms,
#   find the value of the denominator.


def main():
    def simplify_denom(n, d):
        i = 2
        while i < min(n, d) + 1:
            if n % i == 0 and d % i == 0:
                n = n // i
                d = d // i
            else:
                i += 1
        return d

    prod_num, prod_deno = 1, 1

    for numerator in range(10, 99):
        for denominator in range(numerator + 1, 100):
            common = set(str(numerator)).intersection(str(denominator))
            div = numerator / denominator
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue
            for digit in common:
                str_num, str_deno = str(numerator), str(denominator)

                ind_num = str_num.index(digit)
                ind_deno = str_deno.index(digit)

                simp_num = int(str_num[:ind_num] + str_num[ind_num + 1 :])
                simp_deno = int(str_deno[:ind_deno] + str_deno[ind_deno + 1 :])
                if simp_deno > 0 and simp_num / simp_deno == div:
                    prod_num *= simp_num
                    prod_deno *= simp_deno

    print(simplify_denom(prod_num, prod_deno))


if __name__ == "__main__":
    main()
