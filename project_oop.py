# War game

from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards

    def still_has_cards(self):
        """
        Return true if the player still has cards left
        """
        return len(self.hand.cards) != 0


# GAME LOGIC

print("WELCOME TO WAR!!")
print("Let's Begin")
print("Take a chance and try to beat the computer!!!")

# create deck and split in half
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# create both players
comp = Player("computer", Hand(half1))

name = input("What is your name?")
user = Player(name, Hand(half2))

total_rounds = 0
war_counts = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings:")
    print(user.name + " has the count : " + str(len(user.hand.cards)))
    print(comp.name + " has the count : " + str(len(comp.hand.cards)))
    print("Play a card!")
    print("\n")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if (
        c_card[1] == p_card[1]
    ):  # at the top, in the tuple (s,r) we need to compare only rank. not the suite.
        war_counts += 1

        print("WAR!!!")

        print("Each player removes 3 cards 'face down' and then one card face up")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        table_cards.append(c_card)
        table_cards.append(p_card)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("GAME OVER. Number of Rounds : " + str(total_rounds))

print("Wars happened " + str(war_counts) + " times!! Can you believe that!!!")

print("Does the computer still have cards?")
print(str(comp.still_has_cards()))
print(type(comp.still_has_cards()))

print("Does the human player still have cards?")
print(str(user.still_has_cards()))

if comp.still_has_cards():
    print("THE COMPUTER HAVE WON!!!!!")
else:
    print("CONGRATS!!!! YOU HAVE WON!!!!!!!!!!!")
