# https://projecteuler.net/problem=40

# An irrational decimal fraction is created by concatenating the positive
#   integers:
# 0.12345678910[1]112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the
#   following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


def main():

    find = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]

    num, index = 1, 1
    answer = 1

    while find:
        span = len(str(num))
        offset = find[0] - index
        if span > offset:
            answer *= int((str(num)[offset]))
            del find[0]

        index += span
        num += 1

    print(answer)


if __name__ == "__main__":
    main()
