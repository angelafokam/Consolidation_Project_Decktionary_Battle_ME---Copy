import random
import os 
import time 
from functions import player1_card_display_function
from functions import player2_card_display_function
from functions import player1_turn_function
from functions import player2_turn_function
from functions import card_values_function
from functions import scoring_system_function

# making the deck of cards

#give value to face cards and ace 
face_card_values = {"Queen":10,"Jack":10,"Ace":11}
ace_value = {"Ace":11}
#add the parts of the cards to lists 
deck = []
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
face_cards = ["Queens", "Jacks"]
ace_card = "Ace"
##combine numbers and suits to make 36 cards (9 each)
for suit in suits:
    for value in range(2,10):
        deck.append(f"{value} of {suit}")
##combine face cards and suits to make 8 cards (4 each)
for suit in suits:
    for face_card in ["Queen","Jack"]:
        deck.append(f"{face_card} of {suit}")
##combine ace and suits to make 4 cards 
for suit in suits:
        deck.append(f"{ace_card} of {suit}")

##shuffle the deck of cards 
random.shuffle(deck)
###print("shuffled deck", deck)

##deal the deck of cards 
player1_deck = []
player2_deck = []

for i in range(8):
    player1_deck.append(deck.pop(0))
    player2_deck.append(deck.pop(0))

print("The cards have been delt")
###print(player1_deck)
###print(player2_deck)
###len(deck)


#ask for players name 
player1 = input("Who will be the first player? ")
player2 = input("Who will be the second player? ")

## display players cards 
answer_yes = "yes"
answer_no = "no"

print(f"Ok, {player1} you will go first, make sure {player2} cannot see the screen")
player1_card_display_function(player1,player1_deck,answer_yes,answer_no,player2) #for player1
player2_card_display_function(player2, player2_deck,answer_yes,answer_no,player1) #for player2

#seperating the function seperatly 
#player 1 plays cards
the_muck= []
scores = {"player1":0, "player2":0}

#repeats the gaming process until the certain scoring criterias are met 
while True:
    #allows players to put cards in the deck and pick card from deck if wanted 
    player1_turn_function(the_muck, player1, player2, player1_deck, deck)
    player2_turn_function(the_muck, player1, player2, player2_deck, deck)
    
    #removes the card players played from the muck to determine their seperate values 
    player1_card = []
    player2_card = []
    player1_card.append(the_muck.pop(0))
    player2_card.append(the_muck.pop(0))

    #determines the value of the cards and displays the score
    card_values_function(player1, player2, player1_card,player2_card,face_card_values,scores)
    #ends the game and saves the results depending on scoring which determines how the game is won 
    end_loop = scoring_system_function(player1, player2, player1_deck, player2_deck, scores)

    if end_loop:
        break
    