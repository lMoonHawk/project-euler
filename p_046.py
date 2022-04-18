# https://projecteuler.net/problem=46

# It was proposed by Christian Goldbach that every odd composite number can be
#   written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a
#   prime and twice a square?


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

    i = 7
    stop = False
    while not stop:
        i += 2
        if is_prime(i):
            continue
        square = 1
        while True:
            if is_prime(i - 2 * square * square):
                break
            square += 1
            if i - 2 * square * square < 0:
                stop = True
                break
    print(i)


if __name__ == "__main__":
    main()
