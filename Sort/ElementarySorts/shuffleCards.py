import random

## Knuth Shuffle. Make sure to choose randomly between 0 and i;
## don't choose between 0, len(cards)
def shuffle(cards):
    for i in range(len(cards)):
        r = random.randint(0,i)
        cards[i], cards[r] = cards[r], cards[i]

    return cards

if __name__ == '__main__':
    cards = [i for i in range(1,53)]
    print(cards)
    print('*'*50)
    print(shuffle(cards))
    