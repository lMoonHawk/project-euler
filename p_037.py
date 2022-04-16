# https://projecteuler.net/problem=37

# The number 3797 has an interesting property. Being prime itself, it is
#   possible to continuously remove digits from left to right, and remain prime
#   at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
#   left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to
#   right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


from itertools import product


def main():
    def is_prime(n):
        if n == 1:
            return False

        up_to = int(n**0.5)

        if n % 2:
            start, step = 3, 2
        else:
            start, step = 2, 1

        for i in range(start, up_to + 1, step):
            if not n % i:
                return False
        return True

    def truncate(num):
        num = str(num)
        times = len(num) - 1

        yield int(num)
        for i in range(times):
            yield int(num[0 : i + 1])
            yield int(num[times - i : times + 1])

    count, answer = 0, 0
    digit_count = 2

    while count < 11:
        # All primes with digits > 1 end with:
        for digits_in in product({1, 3, 7, 9}, repeat=digit_count - 2):
            # 1st digit has to be prime
            for digits_first in {2, 3, 5, 7}:
                # Last digit has to be prime not div by 2 and 5
                for digit_last in {3, 7}:
                    digits = (digits_first, *digits_in, digit_last)
                    # Concatenate number with decimal expension
                    num = sum(
                        digit * 10 ** (len(digits) - 1 - i)
                        for i, digit in enumerate(digits)
                    )
                    if all(is_prime(small_num) for small_num in truncate(num)):
                        count += 1
                        answer += num
        digit_count += 1

    print(answer)


if __name__ == "__main__":
    main()
