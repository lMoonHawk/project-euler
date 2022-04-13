# https://projecteuler.net/problem=28

# Starting with the number 1 and moving to the right in a clockwise direction
#   a 5 by 5 spiral is formed as follows:

# [21] 22  23 2 4 [25]
#  20  [7]  8  [9] 10
#  19   6  [1]  2  11
#  18  [5]  4  [3] 12
# [17] 16  15 1 4 [13]

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
#   formed in the same way?
SPIRAL_SIZE = 1001


def main():
    diag = 1
    current = 1
    # Numbers in the diagonal are always counted as:
    #  3,  5,  7,  9 (step = 2)
    # 13, 17, 21, 25 (step = 4)
    # 31, 37, 43, 49 (step = 6)
    # ...            (step = 2*n)
    # Number of elements = diameter * 4 corners = (size / 2) * 4
    for i in range(1, (4 * SPIRAL_SIZE // 2) + 1):
        # Converting 1, ..., n to 2, 2, 2, 2, 4, 4, 4, 4, ...
        step = 2 * ((i + 3) // 4)

        next_num = current + step
        diag += next_num
        current = next_num
    print(diag)


if __name__ == "__main__":
    main()
