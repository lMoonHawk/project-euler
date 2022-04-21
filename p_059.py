# https://projecteuler.net/problem=59

# Each character on a computer is assigned a unique code and the preferred
#   standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to
#   ASCII, then XOR each byte with a given value, taken from a secret key.
#   The advantage with the XOR function is that using the same encryption key
#   on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
#   then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text
#   message, and the key is made up of random bytes. The user would keep the
#   encrypted message and the encryption key in different locations, and
#   without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified
#   method is to use a password as a key. If the password is shorter than the
#   message, which is likely, the key is repeated cyclically throughout the
#   message. The balance for this method is using a sufficiently long password
#   key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower
#   case characters.
# Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file
#   containing the encrypted ASCII codes, and the knowledge that the plain
#   text must contain common English words, decrypt the message and find the
#   sum of the ASCII values in the original text.


from itertools import cycle, product

RANK = {
    " the ": 10,
    " be ": 9,
    " to ": 8,
    " of ": 7,
    " and ": 6,
    " a ": 5,
    " in ": 4,
    " that ": 3,
    " have ": 2,
    " it ": 1,
}


def main():
    with open("inputs/p059_cipher.txt") as f:
        cipher = [int(el) for el in f.readline().split(",")]

    def decrypt(message: list[int], key: tuple[int], to_string=True) -> str:
        key = cycle(key)
        if to_string:
            return "".join([chr(el ^ next(key)) for el in message])
        else:
            return [el ^ next(key) for el in message]

    rank_result = {}
    for key in product(range(97, 123), repeat=3):
        decrypted = decrypt(cipher, key)
        rank_result[key] = sum(
            decrypted.count(word) * value for word, value in RANK.items()
        )

    password = max(rank_result, key=rank_result.get)
    print(sum(decrypt(cipher, password, False)))


if __name__ == "__main__":
    main()
