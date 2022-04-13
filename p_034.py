# https://projecteuler.net/problem=34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of
#   their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.


from math import factorial


def main():
    nums = {num: factorial(num) for num in range(10)}
    answer = 0
    for i in range(3, 7 * factorial(9)):  # Can't got above 7 digits as 9!*8 is 7 digits
        if sum(nums[int(digit)] for digit in str(i)) == i:
            answer += i

    print(answer)


if __name__ == "__main__":
    main()
