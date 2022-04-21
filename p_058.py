# https://projecteuler.net/problem=58

# Starting with 1 and spiralling anticlockwise in the following way, a square
#   spiral with side length 7 is formed.

# [37] 36  35  34  33  32 [31]
#  38 [17] 16  15  14 [13] 30
#  39  18  [5]  4  [3] 12  29
#  40  19   6   1   2  11  28
#  41  20  [7]  8   9  10  27
#  42  21  22  23  24  25  26
# [43] 44  45  46  47  48  49

# It is interesting to note that the odd squares lie along the bottom right
#   diagonal, but what is more interesting is that 8 out of the 13 numbers
#   lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square
#   spiral with side length 9 will be formed. If this process is continued,
#   what is the side length of the square spiral for which the ratio of primes
#   along both diagonals first falls below 10%?


def main():
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True

        up_to = int(n**0.5)

        for i in range(3, up_to + 1, 2):
            if not n % i:
                return False
        return True

    def diag_spiral():
        i, step = 1, 2
        while True:
            i += step
            yield i, i + step, i + 2 * step, i + 3 * step
            i += 3 * step
            step += 2

    diag = diag_spiral()
    cnt_prime, total = 0, 0

    while not total or cnt_prime / total > 0.1:
        cnt_prime += [is_prime(num) for num in next(diag)].count(True)
        total += 4

    print(total // 2 + 1)


if __name__ == "__main__":
    main()
