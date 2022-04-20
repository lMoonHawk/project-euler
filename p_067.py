# https://projecteuler.net/problem=67

# By starting at the top of the triangle below and moving to adjacent numbers
#   on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and
#   'Save Link/Target As...'), a 15K text file containing a triangle with
#   one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible
#   to try every route to solve this problem, as there are 299 altogether!
#   If you could check one trillion (1012) routes every second it would take
#   over twenty billion years to check them all. There is an efficient
#   algorithm to solve it. ;o)

triangle = []
with open("inputs/p067_triangle.txt") as f:
    for line in f:
        triangle.append([int(num) for num in line.strip().split(" ")])

# NOTE: As there are only 16384 routes, it is possible to solve this problem by
#   trying every route. However, Problem 67, is the same challenge with a
#   triangle containing one-hundred rows; it cannot be solved by brute force,
#   and requires a clever method! ;o)


def main():
    while len(triangle) > 1:
        for k, _ in enumerate(triangle[1]):
            triangle[1][k] += max(
                triangle[0][k - 1] if k > 0 else 0,
                triangle[0][k] if k < len(triangle[1]) - 1 else 0,
            )
        triangle.pop(0)

    print(max(triangle[0]))


if __name__ == "__main__":
    main()
