# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from
#   1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
#   numbers from 1 to 20?


def main():
    def div_up_to(k, n):
        for i in range(1, n + 1):
            if k % i:
                return False
        return True

    def small_div_up_to(n):
        k = n
        while not div_up_to(k, n):
            k += n
        return k

    print(small_div_up_to(20))


if __name__ == "__main__":
    main()
