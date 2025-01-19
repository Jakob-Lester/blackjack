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
        random_index = random.randint(0, len(Deck.cards) - 1)
        random_card = Deck.cards[random_index]
        hand.append(random_card)
        del Deck.cards[random_index]
        
    def get_score(cards):
        card_value = 0
        player_choice = ""
        for card in cards:
            if card[0] == "A":
                while player_choice != 1 and player_choice != 11:
                    player_choice = int(input("Would you like your 'Ace' to be 1 or 11?: "))
                    if player_choice == 1:
                        card_value += 1
                    elif player_choice == 11:
                        card_value += 11
            elif card[0] == "J" or card[0] == "Q" or card[0] == "K":
                card_value += 10
            elif card[0] == "1":
                if card[1] != 0:
                    card_value += 1
                else:
                    card_value += 10
            else:    
                card_value += int(card[0])
        return card_value      

def main():
    player_hand = []
    player_input = "" 
    while player_input != "fold":
        player_input = input("Draw or fold?: ")
        if player_input == "draw":
            Deck.deal_card(player_hand)
            hand_value = Deck.get_score(player_hand)
            print(f"Your hand: {player_hand} \nHand value: {hand_value}")
            
            if hand_value > 21:
                print("You bust")
                break
            elif hand_value == 21:
                print("Black Jack... You Win!")
                break
                      
        elif player_input == "fold":
            print("You fold...")
              
main()