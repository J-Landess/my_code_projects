import random
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
    for i in enumerate(hand_dealt,start=1):
        print(i)   
    cards_held = input("What numbers would you like to hold?: ").split()
    return cards_held

def new_cards(hand_dealt,cards_held):
    if 1 not in cards_held:
        hand_dealt[0] = deck.pop()
        print(f"new hand: {hand_dealt}")


def run():
    hand1 = deal_cards()
    hold1 = hold_cards(hand_dealt=hand1)
    new_cards(hand_dealt=hand1,cards_held=hold_cards)
run()
