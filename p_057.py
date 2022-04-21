# https://projecteuler.net/problem=57

# It is possible to show that the square root of two can be expressed as an
#   infinite continued fraction.
# sqrt(2) = 1 + (1 / (2 + (1 / (2 + (1 / 2 +...))))
# By expanding this for the first four iterations, we get:
# 1 + 1/2                   = 3/2   = 1.5
# 1 + 1/(2+1/2)             = 7/5   = 1.4
# 1 + 1/(2+1/(2+1/2))       = 17/12 = 1.41666...
# 1 + 1/(2+1/(2+1/(2+1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
#   expansion, 1393/985, is the first example where the number of digits in
#   the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator
#   with more digits than the denominator?


def main():
    # Compute iteratively 2 + 1 / x starting from x = 2 + 1 / 2 = 5 / 2
    num, denom = 5, 2
    answer = 0
    for i in range(2, 1_001):
        num, denom = num * 2 + denom, num
        if len(str(num - denom)) > len(str(denom)):
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
