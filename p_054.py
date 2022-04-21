# https://projecteuler.net/problem=54

# In the card game poker, a hand consists of five cards and are ranked, from
#   lowest to highest, in the following way:

#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the
#   highest value wins; for example, a pair of eights beats a pair of fives
#   (see example 1 below). But if two ranks tie, for example, both players
#   have a pair of queens, then highest cards in each hand are compared (see
#   example 4 below); if the highest cards tie then the next highest cards are
#   compared, and so on.

# Consider the following five hands dealt to two players:
# Hand	 	Player 1	 	    Player 2	 	     Winner
# 1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD          Player 2
#       Pair of Fives       Pair of Eights
#
# 2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH          Player 1
#       Highest card Ace    Highest card Queen
#
# 3	 	2D 9C AS AH AC      3D 6D 7D TD QD          Player 2
#       Three Aces          Flush with Diamonds
#
# 4	 	4D 6S 9H QH QC      3D 6D 7H QD QS          Player 1
#       Pair of Queens      Pair of Queens
#       Highest card Nine   Highest card Seven
#
# 5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D          Player 1
#       Full House          Full House
#       With Three Fours    With Three Threes

# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
#   first five are Player 1's cards and the last five are Player 2's cards.
#   You can assume that all hands are valid (no invalid characters or repeated
#   cards), each player's hand is in no specific order, and in each hand there
#   is a clear winner.

# How many hands does Player 1 win?

RANK = ["HC", "OP", "TP", "TK", "S", "F", "FH", "FK", "SF", "RF"]
CARDS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def main():
    def hand_value(h):
        values = [CARDS[card[0]] for card in h]
        val_cnt = {c: values.count(c) for c in values}
        suits = [card[1] for card in h]

        # Straight
        consecutive = set([x for x in values if x + 1 in values])
        if len(consecutive) == 4:
            main = "S"
            # Straight Flush
            if len(set(suits)) == 1:
                main = "SF"
            by = max(consecutive) + 1
            high = None

        # Four of a Kind
        elif len(val_cnt) == 2:
            main = "FK"
            by = max(val_cnt, key=val_cnt.get)
            high = min(val_cnt, key=val_cnt.get)

        # Full House
        elif set(val_cnt.values()) == {2, 3}:
            main = "FH"
            by = [k for k, cnt in val_cnt.items() if cnt == 3][0]
            high = [k for k, cnt in val_cnt.items() if cnt == 2][0]

        # Flush
        elif len(set(suits)) == 1:
            main = "F"
            by = max(values)
            high = sorted(values)[-2::-1]

        # Three of a Kind
        elif 3 in val_cnt.values():
            main = "TK"
            by = max(val_cnt, key=val_cnt.get)
            high = [card for card in sorted(values)[::-1] if card != by]

        # Two Pairs
        elif list(val_cnt.values()).count(2) == 2:
            main = "TP"
            by = max([k for k, cnt in val_cnt.items() if cnt == 2])
            high = [k for k, cnt in val_cnt.items() if cnt == 2 and k != by]
            high.append(min(val_cnt, key=val_cnt.get))

        # One Pair
        elif list(val_cnt.values()).count(2) == 1:
            main = "OP"
            by = [k for k, cnt in val_cnt.items() if cnt == 2][0]
            high = [v for v in sorted(values)[::-1] if v != by]

        # High Card
        else:
            main = "HC"
            by = max(values)
            high = sorted(values)[-2::-1]

        return main, by, high

    def play(h1, h2):
        main1, by1, high1 = hand_value(h1)
        main2, by2, high2 = hand_value(h2)

        if RANK.index(main1) == RANK.index(main2):
            if by1 == by2:
                for c1, c2 in zip(high1, high2):
                    if c1 != c2:
                        return "1" if c1 > c2 else "2"
                return "0"
            else:
                return "1" if by1 > by2 else "2"
        else:
            return "1" if RANK.index(main1) > RANK.index(main2) else "2"

    answer = 0
    with open("inputs/p054_poker.txt") as f:
        for line in f:
            hands = line.strip().split(" ")
            p1, p2 = hands[:5], hands[5:]
            if play(p1, p2) == "1":
                answer += 1
    print(answer)


if __name__ == "__main__":
    main()
