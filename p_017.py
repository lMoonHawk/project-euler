# https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#   then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written
#   out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342
#   (three hundred and forty-two) contains 23 letters and 115
#   (one hundred and fifteen) contains 20 letters. The use of "and" when
#   writing out numbers is in compliance with British usage.


def main():
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    exceptions = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    test = []
    for hundred in units:
        suffix = f"{hundred}hundred" if hundred != "" else ""
        for ten in tens:
            if ten == "ten":
                for exception in exceptions:
                    test.append(f"{suffix}{exception}")
            else:
                for unit in units:
                    if unit != "" and suffix[-3:] != "and" and suffix != "":
                        suffix = suffix + "and"
                    test.append(f"{suffix}{ten}{unit}")

    print(sum([len(el) for el in test]) + len("onethousand"))


if __name__ == "__main__":
    main()
