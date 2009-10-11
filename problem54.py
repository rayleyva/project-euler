"""
POKER!

hands:
0: high card
1: pair
2: two pair
3: three of a kind
4: straight
5: flush
6: full house
7: four-of-a-kind
8: straight-flush

example row:
8C TS KC 9H 4S 7D 2S 5D 3S AC
"""
CARDS = ['!', '!', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def flush(hand):
    """
    flushes are easy!
    """
    suits = { 'C': 0, 'S': 0, 'D': 0, 'H': 0 }
    for card in hand:
        suits[card[1]] += 1
    return 5 in suits.values()

def straight(hand):
    """
    straights are a little more complex, because in 7 card hands the straight
    can start at sorted index 0, 1, or 2.  aces can be 1 or 14
    """
    vals = values_from_hand(hand)
    for x in range(len(vals), 5, -1):
        if vals[x - 1] == 14: # does the hand contain an ace?
            vals.insert(0, 1) # simulate an ace at the beginning
    for i in range(0, len(vals) - 4):
        consecutive = 0
        for j in range(i, i + 5):
            if vals[j] - j == vals[i]:
                consecutive += 1
                if consecutive == 5:
                    return True
    return False

def poker_sort(hand):
    """
    a somewhat crufty sorting method for poker
    hands of my own invention, based on the principle
    that, given 4 suits, there can never be more than
    4-of-a-kind.  Multiple decks / Wildcards are not
    taken into account
    """
    data = { 1: [], 2: [], 3: [], 4: [] }
    vals = values_from_hand(hand)
    for card in vals:
        added = False
        for i in range(3, 0, -1):
            if card in data[i]:
                card_list = data[i]
                idx = card_list.index(card)
                del(data[i][idx])
                data[i+1].append(card)
                added = True
        if not added:
            data[1].append(card)
    for k, v in data.items():
        v.sort()
        v.reverse()
    # correct for 5-card hands (i.e., 2x3-of-a-kind or 3x2-of-a-kind)
    if len(data[3]) > 1:
        data[2].append(data[3][-1])
        del(data[3][-1])
    if len(data[2]) > 2:
        data[1].append(data[2][-1])
        del(data[2][-1])
    return data

def score_hand(hand):
    """
    Score a hand
    in 5 & 7 card hands, using the best 5 cards,
    it is not possible to have a straight or flush
    and a better hand (i.e. a full house / four of a kind)
    """
    score = 0
    if flush(hand) and straight(hand):
        score = 8
    elif flush(hand):
        score = 5
    elif straight(hand):
        score = 4
    else:
        data = poker_sort(hand)
        if len(data[4]) > 0:
            score = 7
        elif len(data[3]) > 0 and len(data[2]) > 0:
            score = 6
        elif len(data[3]) > 0:
            score = 3
        elif len(data[2]) >= 2:
            score = 2
        elif len(data[2]) == 1:
            score = 1
    return score

def winner(*hands):
    """
    Calculate the winning hand in a list of hands
    """
    best = []
    best_score = 0
    for hand in hands:
        score = score_hand(hand)
        if score == best_score:
            best.append(hand)
        elif score > best_score:
            best = [hand]
            best_score = score
    if len(best) == 1:
        return best[0]
    else:
        best_data = []
        for i in range(len(best)):
            best_data.append(poker_sort(best[i]))

        tmp = []
        cards_available = 5
        winner = ''
        for i in range(4, 0, -1):
            high = []
            for j in range(len(best)):
                best_data[j][i] = best_data[j][i][:cards_available]
                if best_data[j][i] == high:
                    tmp.append(best[j])
                elif best_data[j][i] > high:
                    tmp = [best[j]]
                    high = best_data[j][i]
            cards_available -= (len(high) * i)
            winner += ''.join([CARDS[x]*i for x in high])
            if len(tmp) == 1:
                return tmp[0]
            elif len(tmp) > 1:
                tmp = []
                pass
    
    return 'Tie: %s' % (winner)
    
def values_from_hand(hand):
    """
    Return sorted numeric values of cards in a hand
    """
    values = []
    for card in hand:
        val = CARDS.index(card[0])
        values.append(val)
    values.sort()
    return values
    

f = open('poker.txt', 'r')
data = f.read()
hands = data.split('\n')

player1, player2 = 0, 0
all_hands = []

for hand in hands:
    tokens = hand.split()
    if len(tokens) == 10:
        if winner(tokens[:5], tokens[5:]) == tokens[:5]:
            player1 += 1
        else:
            player2 += 1
    all_hands.append(tokens[:5])
    all_hands.append(tokens[5:])
print '%d - %d' % (player1, player2)
