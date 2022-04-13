# https://projecteuler.net/problem=22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
#   containing over five-thousand first names, begin by sorting it into
#   alphabetical order. Then working out the alphabetical value for each name,
#   multiply this value by its alphabetical position in the list to obtain a
#   name score.

# For example, when the list is sorted into alphabetical order, COLIN, which
#   is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
#   COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

with open("inputs/p022_names.txt") as f:
    names = f.readline().replace('"', "").split(",")


def main():
    values = {chr(x + 64): x for x in range(1, 27)}
    for i, name in enumerate(sorted(names)):
        names[i] = sum([values[char] for char in name]) * (i + 1)
    print(sum(names))


if __name__ == "__main__":
    main()
