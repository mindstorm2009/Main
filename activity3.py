from dataclasses import dataclass


@dataclass
class Coin:
    __slots__ = 'name', 'value'
    name: str
    value: int


nickel = Coin('nickel', 5)
dollar = Coin('dollar', 100)
quarter = Coin('quarter', 25)
dime = Coin('dime', 10)
penny = Coin('penny', 1)

def make_change(price, payment):
    change = payment - price
    coins = []
    while change > 0:
        if change >= 100:
            coin = dollar
        elif change >= 25:
            coin = quarter
        elif change >= 10:
            coin = dime
        elif change >= 5:
            coin = nickel
        elif change >= 1:
            coin = penny

        coins += [coin]
        change -= coin.value
    print(coins)

def create_dict():
    file = open("words_alpha.txt")
    d = {}
    for line in file:
        word = line.strip()
        first = word[0]
        if first not in d:
            d[first] = [word]
        else:
            d[first] += [word]
    file.close()
    return d


def main():
    """letter = input("What letter: ")
    dict = create_dict()
    while letter != "":
        print(dict[letter])
        letter = input("What letter: ")"""
    make_change(173, 500)

main()
