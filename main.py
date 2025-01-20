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
        
    def get_score(cards, player, hand_value):
        card_value = 0
        player_choice = ""
        last_card = cards[-1]
        
        if player == "player":
            if last_card[0] == "A":
                while player_choice != 1 and player_choice != 11:
                    player_choice = int(input("Would you like your 'Ace' to be 1 or 11?: "))
            if player_choice == 1:
                card_value += 1
            elif player_choice == 11:
                card_value += 11
            elif last_card[0] == "J" or last_card[0] == "Q" or last_card[0] == "K":
                card_value += 10
            elif last_card[0] == "1":
                if last_card[1] == "0":
                    card_value += 10
                else:
                    card_value += 1
            else:    
                card_value += int(last_card[0])
            
        elif player == "dealer":
            if last_card[0] == "A":
                if hand_value + 11 <= 21:
                    card_value += 11
                else:
                    card_value += 11
            elif last_card[0] == "J" or last_card[0] == "Q" or last_card[0] == "K":
                card_value += 10
                
            elif last_card[0] == "1":
                if last_card[1] == "0":
                    card_value += 10
                else:
                    card_value += 1
            else:    
                card_value += int(last_card[0])
            
        return card_value

    def who_wins(player_hand_value, dealer_hand_value):
        player_diff = 21 - player_hand_value
        dealer_diff = 21 - dealer_hand_value

        if player_diff < dealer_diff:
            return "You win!"
        elif player_diff == dealer_diff:
            return "Tie!"
        else:
            return "You lose!"


def main():
    game_over = False
    player_standing = False
    dealer_hand = []
    player_hand = []
    player_input = ""
    player_hand_value = 0
    dealer_hand_value = 0 
    while game_over == False:
        if player_standing == False:    
            player_input = input("Draw, Stand, or Fold?: ")
            if player_input == "draw":
                Deck.deal_card(player_hand)
                player_hand_value += Deck.get_score(player_hand, "player", player_hand_value)
                print(f"Your hand: {player_hand} \nHand value: {player_hand_value}")    
            
            if player_input == "stand":
                player_standing = True

            elif player_input == "fold":
                print("You fold...")
                game_over = True
              
            if dealer_hand_value < 17:
                Deck.deal_card(dealer_hand)
                dealer_hand_value += Deck.get_score(dealer_hand, "dealer", dealer_hand_value)
                print(f"Dealer hand: {dealer_hand} \nDealer hand value: {dealer_hand_value}")
            if dealer_hand_value == 21 and player_hand_value == 21:
                print("Tie")
                game_over = True
            elif player_hand_value == 21:
                print("Blackjack! You win!")
            if player_hand_value > 21:
                print("You bust... Dealer wins!")
                game_over = True
            if dealer_hand_value > 21:
                print("Dealer busts... You win!")
                game_over = True

        elif player_standing == True:
            while dealer_hand_value < 17:
                Deck.deal_card(dealer_hand)
                dealer_hand_value += Deck.get_score(dealer_hand, "dealer", dealer_hand_value)
                print(f"Dealer hand: {dealer_hand} \nDealer hand value: {dealer_hand_value}")
            if dealer_hand_value == 21 and player_hand_value == 21:
                print("Tie")
                game_over = True
            elif dealer_hand_value > 21:
                print("Dealer busts!... You win!")
                game_over = True
            else:
                print(Deck.who_wins(player_hand_value, dealer_hand_value))
                game_over = True
                      
main()