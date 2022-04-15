# https://projecteuler.net/problem=42

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
#   so the first ten triangle numbers are:
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its
#   alphabetical position and adding these values we form a word value.
#   For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
#   If the word value is a triangle number then we shall call the word a
#   triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
#   containing nearly two-thousand common English words, how many are triangle
#   words?


def main():

    with open("inputs/p042_words.txt") as f:
        words = f.readline().replace('"', "").split(",")

    value = {chr(x + 64): x for x in range(1, 27)}

    def add_triangle_num():
        index = len(triangle_nums)
        triangle_nums.append(index + 1 + triangle_nums[index - 1])

    triangle_nums = [1]

    count = 0
    for word in words:
        word_val = sum([value[letter] for letter in word])

        if word_val > triangle_nums[-1]:
            while word_val > triangle_nums[-1]:
                add_triangle_num()

        count += 1 if word_val in triangle_nums else 0

    print(count)


if __name__ == "__main__":
    main()
