# https://projecteuler.net/problem=39

# If p is the perimeter of a right angle triangle with integral length sides
#   {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


def main():
    squares = {x * x: x for x in range(1, 1_001)}

    max_p, max_sol = 0, 0
    for perimeter in range(3, 1_001):
        sol = 0
        for a in range(1, perimeter - 1):
            for b in range(a, (perimeter - a) // 2):
                c_squared = a * a + b * b
                if c_squared not in squares:
                    continue
                c = squares[c_squared]
                if a + b + c == perimeter:
                    sol += 1
        if sol > max_sol:
            max_sol, max_p = sol, perimeter
    print(max_p)


if __name__ == "__main__":
    main()
