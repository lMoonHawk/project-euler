# https://projecteuler.net/problem=43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
#   of each of the digits 0 to 9 in some order, but it also has a rather
#   interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
#   we note the following:

#     d2d3d4=406 is divisible by 2
#     d3d4d5=063 is divisible by 3
#     d4d5d6=635 is divisible by 5
#     d5d6d7=357 is divisible by 7
#     d6d7d8=572 is divisible by 11
#     d7d8d9=728 is divisible by 13
#     d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.


from itertools import permutations


def main():
    def conc_int(iterable):
        """Concatenate iterable with single digits to a number using decimal
        expension"""
        return sum(
            digit * 10 ** (len(iterable) - 1 - i)
            for i, digit in enumerate(iterable)
        )

    count_num = 0
    for num in permutations(range(10), 10):
        if (
            num[3] % 2 == 0
            and conc_int(num[2:5]) % 3 == 0
            and conc_int(num[3:6]) % 5 == 0
            and conc_int(num[4:7]) % 7 == 0
            and conc_int(num[5:8]) % 11 == 0
            and conc_int(num[6:9]) % 13 == 0
            and conc_int(num[7:10]) % 17 == 0
        ):
            count_num += conc_int(num)

    print(count_num)


if __name__ == "__main__":
    main()
