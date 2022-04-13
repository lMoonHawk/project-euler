# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, and only being able to move to
#   the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?
import math


def main():
    # Choose one of three method...
    GRID_SIZE = 20

    def memoization(m, n, memo={}):
        if (m, n) in memo:
            return memo[m, n]
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        memo[m, n] = memoization(m - 1, n) + memoization(m, n - 1)
        return memo[m, n]

    def tabulation(m, n):
        tab = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        tab[1][1] = 1
        for i in range(m + 1):
            for j in range(n + 1):
                if j + 1 < n + 1:
                    tab[i][j + 1] += tab[i][j]
                if i + 1 < m + 1:
                    tab[i + 1][j] += tab[i][j]
        return tab[m][n]

    def combinatorics(m, n):
        answer = math.comb((m - 1) + (n - 1), m - 1)
        return answer

    print(memoization(GRID_SIZE + 1, GRID_SIZE + 1))
    # print(tabulation(GRID_SIZE + 1, GRID_SIZE + 1))
    # print(combinatorics(GRID_SIZE + 1, GRID_SIZE + 1))


if __name__ == "__main__":
    main()
