# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def main():
    def get_factors(num):
        factors = []
        i = 2
        while num != 1:
            if num % i == 0:
                factors.append(i)
                num /= i
            i += 1
        return factors

    print(max(get_factors(600851475143)))


if __name__ == "__main__":
    main()
