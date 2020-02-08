import card
import deck
import hand
import bankroll

def separator(bord = 1):
    for _ in range(0, bord):
        print("------------------------------------------")

def make_bet():
    separator()
    while True:
        while True:
            try:
                bet = int(input("!!!Time to bet!!!\nHow much would you like to bet?: "))
            except:
                print("A number required. Try again!")
            else:
                break

        print(f"Your bankroll is :{playerMoney}")
        if playerMoney.withdrawal(bet):
            print("Bet accepted!")
            print(f"You have left :{playerMoney}")
            separator()
            break
        else:
            print("Insufficient funds. Try again!")
    return bet



def won():
    pass
playerMoney = bankroll.Bankroll(100)
casinoMoney = bankroll.Bankroll()
mainDeck = deck.Deck()


while True:
    print("!!!Welcome to Naebumba Casino!!!")
    print("!!!!!You are about to play some BlackJack!!!!!")
    #input("Hit anykey+enter to begin....")


    mainDeck.reshuffle()
    playerHand = hand.Hand(mainDeck.pull_card(), mainDeck.pull_card())
    casinoHand = hand.Hand(mainDeck.pull_card(), mainDeck.pull_card())
    gameStatus = "Running"
    bet = make_bet()

    while True:
        separator(3)
        print(f"Your cards: {playerHand.show_hand()}")
        print(f"You have:{playerHand.value}")
        separator()
        print(f"Dealer first card is:{casinoHand.cards[0].rank}{casinoHand.cards[0].suit}")


        while True:
            while True:
                decision = input("H for Hit\nS for Stay\n").upper()
                if decision == "H" or decision == "S":
                    break
                print("H or S, please. Try again")

            if decision == "H":
                playerHand.add_card(mainDeck.pull_card())
                print(f"You HIT and you get: {playerHand.cards[-1].rank}{playerHand.cards[-1].suit}")
                print(playerHand.value)
                if playerHand.value > 21:
                    print(f"You lose! You now have{playerHand.value}! BUSTED!!! Your bet was {bet}.")
                    playerMoney.withdrawal(bet)
                    print(f"Your bankroll: {playerMoney}")
                    separator()
                break
            else:
                print(f"You stay, and the dealer gets to play!")
                separator()
                print(f"Your cards: {playerHand.show_hand()}")
                print(f"You have:{playerHand.value}")
                separator()
                print(f"Dealer cards: {casinoHand.show_hand()}")
                print(f"Dealer has:{casinoHand.value}")
                separator()

                if casinoHand.value < playerHand.value:
                    print(f"You win! Your bet was {bet}!")
                    playerMoney.income(bet*2)
                    gameStatus = "Won"

                if casinoHand.value == playerHand.value:
                    print("Whoa, a draw! DEALER WINS ANYWAY.")

                if casinoHand.value >= playerHand.value:
                    print(f"You lose! Your bet was {bet}.")
                    playerMoney.withdrawal(bet)
                    gameStatus = "Lost"

                print(f"Your bankroll: {playerMoney}")
                break

        if gameStatus != "Running" and "Y" != input("Hit Y if you want to play again. Goodbye otherwise!").upper():
            break




