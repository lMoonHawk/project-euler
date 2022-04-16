# https://projecteuler.net/problem=52

# It can be seen that the number, 125874, and its double, 251748, contain
#   exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
#   contain the same digits.


def main():
    num, multiples = 1, None
    while num == 1 or any(x != multiples[0] for x in multiples):
        num += 1
        multiples = [set(str(num * k)) for k in range(1, 7)]

    print(num)


if __name__ == "__main__":
    main()
