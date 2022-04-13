# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some
#   research for yourself.
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a
#   century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


from itertools import cycle


def main():
    d, m, y = 1, 1, 1900
    dd = cycle(range(7))  # Monday to Sunday
    week_day = next(dd)
    count = 0

    while (d, m, y) != (1, 1, 2001):
        count += 1 if week_day == 6 and y >= 1901 and d == 1 else 0

        leap_year = False
        if not y % 4:
            leap_year = True
            if not y % 100:
                leap_year = False
                if not y % 400:
                    leap_year = True

        if (
            d == 31
            or (d == 30 and m in {4, 6, 9, 11})
            or (d == 28 and m == 2 and not leap_year)
            or (d == 29 and m == 2 and leap_year)
        ):
            d = 1
            if m == 12:
                m = 1
                y += 1
            else:
                m += 1
        else:
            d += 1

        week_day = next(dd)

    print(count)


if __name__ == "__main__":
    main()
