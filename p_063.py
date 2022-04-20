# https://projecteuler.net/problem=63

# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
#   number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?


def main():
    count = 0

    # num > 9 is impossible (nb of digits is always > power)
    # For num = 9, k can be at his max at 21 (else nb of digits < power)
    for power in range(1, 22):
        for num in range(1, 10):
            result = len(str(num**power))
            if result == power:
                count += 1
            elif result > power:
                break

    print(count)


if __name__ == "__main__":
    main()
