# https://projecteuler.net/problem=36

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in
#   base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include
#   leading zeros.)


def main():
    def is_pal(string):
        return string == string[::-1]

    answer = 0
    for i in range(1, 1_000_000):
        if is_pal(str(i)) and is_pal(f"{i:b}"):
            answer += i

    print(answer)


if __name__ == "__main__":
    main()
