# https://projecteuler.net/problem=30

# Surprisingly there are only three numbers that can be written as the sum of
#   fourth powers of their digits:

#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth
#   powers of their digits.


def main():
    nums = {num: num**5 for num in range(10)}
    answer = 0
    for i in range(2, 6 * 9**5):  # Can't got above 6 digits as 9^5*7 is 6 digits
        if sum(nums[int(digit)] for digit in str(i)) == i:
            answer += i

    print(answer)


if __name__ == "__main__":
    main()
