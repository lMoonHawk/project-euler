# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following
#   sequence:  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#   Although it has not been proved yet (Collatz Problem), it is thought that all starting
#   numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def main():
    chains_count = [0, 0]
    for k in range(2, 1_000_000):
        n = k
        count = 1
        while n != 1:
            n = 3 * n + 1 if n % 2 else n // 2
            count += 1
            if n < k:
                count += chains_count[n]
                break
        chains_count.append(count)

    print(chains_count.index(max(chains_count)))


if __name__ == "__main__":
    main()
