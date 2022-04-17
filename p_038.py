# https://projecteuler.net/problem=38

# Take the number 192 and multiply it by each of 1, 2, and 3:

#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576.
#   We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
#   and 5, giving the pandigital, 918273645, which is the concatenated
#   product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
#   the concatenated product of an integer with (1,2, ... , n) where n > 1?


def main():

    pendigital = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    answer = 0

    for num_0 in range(1, 10_000):
        digits = len(str(num_0))
        num, multiplier = num_0, 2

        while digits < 9:
            num = int(str(num) + str(num_0 * multiplier))
            multiplier += 1
            digits = len(str(num))
            if digits > len(set(str(num))):
                break

        if digits == 9 and set(str(num)) == pendigital and num > answer:
            answer = num

    print(answer)


if __name__ == "__main__":
    main()
