from random import randint


def PokerCards():
    pokercardlist = []
    for y in ['D', 'C', 'H', 'S']:
        for x in range(2, 10):

            pokercardlist.append("{}{}".format(x, y))
        pokercardlist.append('T{}'.format(y))
        pokercardlist.append('J{}'.format(y))
        pokercardlist.append('Q{}'.format(y))
        pokercardlist.append('K{}'.format(y))
        pokercardlist.append('A{}'.format(y))
    return pokercardlist


de = {
    "A": ":regional_indicator_a:",
    "2": ":two:",
    "3": ":three:",
    "4": ":four:",
    "5": ":five:",
    "6": ":six:",
    "7": ":seven:",
    "8": ":eight:",
    "9": ":nine:",
    "T": ":keycap_ten:",
    "J": ":regional_indicator_j:",
    "Q": ":regional_indicator_q:",
    "K": ":regional_indicator_k:",
    "D": ":diamonds:",
    "C": ":clubs:",
    "H": ":hearts:",
    "S": ":spades:"
}


def RemoveCardsEmoji(ListCards):
    RemovedCard = ListCards.pop(randint(0, len(ListCards)-1))
    EmojiText = de[RemovedCard[0]] + de[RemovedCard[1]]
    return EmojiText
