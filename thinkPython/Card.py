class Card:
    '''표준 카드 플레이어를 표현'''
    ''' 스페이드 -> 3
        하트 -> 2
        다이아몬드 -> 1
        클럽 -> 0

        잭 -> 11
        퀸 -> 12
        킹 -> 13
    '''
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                            Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    # def __lt__(self, other):
    #     #문양을 확인한다
    #     if self.suit < other.suit: return True
    #     if self.suit > other.suit: return False
    #     #문양이 같으면 순위를 확인한다
    #     return self.rank < other.rank
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

card1 = Card(2, 11)
card2 = Card(3, 4)
print(card1)
print(card2)
print(card1 < card2)