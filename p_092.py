# https://projecteuler.net/problem=92

# A number chain is created by continuously adding the square of the digits in
#   a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless
#   loop. What is most amazing is that EVERY starting number will eventually
#   arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?


def main():
    def sqr_chain_end(n, memo={}):
        if n in memo:
            return memo[n]
        if n in [1, 89]:
            return n

        memo[n] = sqr_chain_end(sum(int(digit) ** 2 for digit in str(n)))
        return memo[n]

    answer = 0
    for num in range(1, 10_000_000):
        if sqr_chain_end(num) == 89:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
