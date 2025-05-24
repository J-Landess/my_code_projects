import random
suits = "hearts", "diamonds","spades","clubs"
rank = "12345678910JQKA".split()
deck = [
    "A-SPADE","2-SPADE","3-SPADE","4-SPADE","5-SPADE","6-SPADE","7-SPADE","8-SPADE","9-SPADE","10-SPADE","J-SPADE","Q-SPADE","K-SPADE",
    "A-HEART","2-HEART","3-HEART","4-HEART","5-HEART","6-HEART","7-HEART","8-HEART","9-HEART","10-HEART","J-HEART","Q-HEART","K-HEART",
    "A-DIAMOND","2-DIAMOND","3-DIAMOND","4-DIAMOND","5-DIAMOND","6-DIAMOND","7-DIAMOND","8-DIAMOND","9-DIAMOND","10-DIAMOND","J-DIAMOND","Q-DIAMOND","K-DIAMOND",
    "A-CLUB","2-CLUB","3-CLUB","4-CLUB","5-CLUB","6-CLUB","7-CLUB","8-CLUB","9-CLUB","10-CLUB","J-CLUB","Q-CLUB","K-CLUB"]

def deal_cards():
    random.shuffle(deck)
    hand_dealt = [deck.pop() for _ in range(5)]
    return hand_dealt

def hold_cards(hand_dealt):
    for i, card in enumerate(hand_dealt,start=1):
        print(f"{i}:{card}") 
    while True:
        try:
            cards_held = [int(i) for i in input("What numbers would you like to hold?: ").split()]
            return cards_held
        except ValueError:
            print("Must be a list of index values seperated by a space\nExample:\nHold Cards\n1 4 5")


def new_cards(hand_dealt,cards_held):
    for i in range(5):
        if (i+1) not in cards_held:
            hand_dealt[i] = deck.pop()
    print(f"final hand: {hand_dealt}")


def run():
    hand_dealt = deal_cards()
    cards_held = hold_cards(hand_dealt)
    new_cards(hand_dealt,cards_held)
run()
