# https://projecteuler.net/problem=79

# A common security method used for online banking is to ask the user for
#   three random characters from a passcode. For example, if the passcode was
#   531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
#   reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the
#   file so as to determine the shortest possible secret passcode of unknown
#   length.


def main():
    # Simple algorithm that only works with non-repeated digits
    pw = []
    with open("inputs/p079_keylog.txt") as f:
        for line in f:
            login = list(line.strip())
            for i, el in enumerate(login):
                if el not in pw:
                    pw.append(el)
                elif i > 0:
                    check_2 = pw.index(el)
                    check_1 = pw.index(login[i - 1])
                    if check_2 < check_1:
                        pw[check_1], pw[check_2] = (pw[check_2], pw[check_1])

    print(int("".join(pw)))


if __name__ == "__main__":
    main()
