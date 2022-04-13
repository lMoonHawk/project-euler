# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made
#   from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


from itertools import combinations


def main():
    answer = 0
    for m, n in combinations(range(100, 999), 2):
        num = str(m * n)
        if num == num[::-1]:
            num = int(num)
            answer = num if num > answer else answer
    print(answer)


if __name__ == "__main__":
    main()
