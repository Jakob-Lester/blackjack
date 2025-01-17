import random

class Deck:
    cards = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    for suit in suits:
        for rank in ranks:
            cards.append(f"{rank} of {suit}")

    def shuffle_deck():
        random.shuffle(Deck.cards)

    def deal_card(hand):
        random_card = Deck.cards[random.randint(0, len(Deck.cards))]
        hand.append(random_card)
        del Deck.cards[random_card]

        
def main():
    player_hand = []
    player_input = ""
    while player_input != "fold":
        player_input = input("Draw or fold?: ")
        if player_input == "draw":
            Deck.deal_card(player_hand)
            print(player_hand)
        elif player_input == "fold":
            break
            
          
main()