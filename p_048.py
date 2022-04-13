# https://projecteuler.net/problem=48

# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


def main():
    print(str(sum([k**k for k in range(1, 1001)]))[-10:])


if __name__ == "__main__":
    main()
