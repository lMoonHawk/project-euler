# https://projecteuler.net/problem=12


# The sequence of triangle numbers is generated by adding the natural numbers.
#   So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#   The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?


def main():
    def triangular():
        t, n = 0, 1
        while True:
            t += n
            n += 1
            yield t

    def count_div(n):
        count = 2
        for i in range(2, int(n**0.5)):
            if not n % i:
                count += 2
        if (n**0.5).is_integer():
            count += 1
        return count

    for t in triangular():
        if count_div(t) > 500:
            print(t)
            break


if __name__ == "__main__":
    main()
