
#this function allows players to view their cards  
import os
import time 
import pandas as pd 


#this function displays player1s cards 
def player1_card_display_function(player1, player1_deck,answer_yes,answer_no,player2):
   while True:
        move_on = input("Are you ready to see your cards? (yes/no): ").lower()
        #if player 1 says yes show them the cards 
        if move_on == answer_yes:
            print(f"{player1} deck: {player1_deck}")
            while True:
                finished_viewingdeck = input(f"{player1}, Are you finished viewing your deck? (yes/no): ").lower()
                time.sleep(1)
                #continue showing the deck and ask if they are finished in 5 seconds 
                if finished_viewingdeck == answer_no:
                    print("Ok, take your time!")
                    print(f"{player1} deck: {player1_deck}")
                    time.sleep(5)
                #make the cards disapear from terminal 
                elif finished_viewingdeck == answer_yes:
                    print("Ok! hiding your cards now")
                    time.sleep(1.7)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Now give the computer to {player2}!")
                    break 
                else:
                    print("Invalid response, please try again.")
            break
        #if player 1 says no ask them again 
        elif move_on == answer_no:
            print(f"Ok, make sure {player1} cannot see the screen")
        else:
            print("Invalid response, please try again.")

#this function displays player2s cards
def player2_card_display_function(player2, player2_deck, answer_yes,answer_no,player1):

    while True:
        move_on = input(f"{player2}, Are you ready to see your cards? (yes/no): ").lower()
        #if player 1 says yes show them the cards 
        if move_on == answer_yes:
            print(f"{player2} deck: {player2_deck}")
            while True:
                finished_viewingdeck = input(f"{player2}, Are you finished viewing your deck? (yes/no): ").lower()
                #continue showing the deck and ask if they are finished in 5 seconds 
                if finished_viewingdeck == answer_no:
                    print("Ok, take your time!")
                    print(f"{player2} deck: {player2_deck}")
                    time.sleep(5)
                #make the cards disapear from terminal 
                elif finished_viewingdeck == answer_yes:
                    print("Ok! hiding your cards now")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Now it is time to start the game!")
                    print("For rules and other information check out the Decktionary Battle README")
                    time.sleep(3)
                    break 
                else:
                    print("Invalid response, please try again.")
            break
        #if player 1 says no ask them again 
        elif move_on == answer_no:
            print(f"Ok, make sure {player1} cannot see the screen")
        else:
            print("Invalid response, please try again.")

#this function allowes player 1 to pick the card they want to play 
def player1_turn_function(the_muck, player1, player2, player1_deck, deck):
    the_muck.clear()
#player 1 chooses the card they want to be delt 
    print(f"{player1} it is your turn, make sure {player2} cannot see the screen")
    time.sleep(6)
    print(f"Here is your deck: {player1_deck}")
    print(f"The muck: {the_muck}")
# asks if they want to grab a card from the deck
    while True:
        grab_card = input("Do you want to pull a card from the deck? (yes/no): ").lower()
        if grab_card == "yes":
            player1_deck.append(deck.pop(0))
            print(f"Updated deck: {player1_deck}")
            print(f"The muck: {the_muck}")
            break
        elif grab_card == "no":
            print("Ok!")
            print(f"The muck: {the_muck}")
            break
        else:
            print("Invalid response")


    while True:
        player1_delt_card = input("Card you are placing in the muck: ").strip().lower()
        print(f"{player1} deck: {player1_deck}")
    # add the card to muck and delete the card from players deck 
        if player1_delt_card in map(str.lower,player1_deck):
            #find the card in the muck
            altered_player1_card = next(card for card in player1_deck if card.lower() == player1_delt_card)
            the_muck.append(altered_player1_card)
            player1_deck.remove(altered_player1_card)
            #clears the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{player1}, your card has been placed in the muck")
            print(f"Now give the computer to {player2}")
            time.sleep(7)
            #clears the terminal again so the instructions are less confusing
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("The card you entered is not in your deck")

#this function allowes player 2 to pick the card they want to play 
def player2_turn_function(the_muck, player1, player2, player2_deck, deck):
    #player 2 plays card 
        print(f"{player2}, it is your turn, make sure {player1} cannot see your screen")
        print("For rules and other information check out the Decktionary Battle README")
        time.sleep(6)
        print(f"Here is your deck: {player2_deck}")
        print(f"The muck: {the_muck}")

    # asks if they want to grab a card from the deck
        while True:
            grab_card = input("Do you want to pull a card from the deck? (yes/no): ").lower()
            if grab_card == "yes":
                print(f"Updated deck: {player2_deck}")
                print(f"TThe muck: {the_muck}")
                break
            elif grab_card == "no":
                print("Ok!")
                print(f"The muck: {the_muck}")
                break
            else:
                print("Invalid response")

        while True:
            player2_delt_card = input("Card you are placing in the muck: ").lower()
            print(f"{player2} deck: {player2_deck}")
        # add the card to muck and delete the card from players deck 
            if player2_delt_card in map(str.lower,player2_deck):
                #find the card in the muck
                altered_player2_card = next(card for card in player2_deck if card.lower() == player2_delt_card)
                
                the_muck.append(altered_player2_card)
                player2_deck.remove(altered_player2_card)
                #print(the_muck)
                #print(player2_deck)
                print(f"Your card has been placed in the muck")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("The card you entered is not in your deck")
            

#this function determines the card values in the muck and displays the score 
def card_values_function(player1, player2, player1_card,player2_card,face_card_values,scores):
    #program checks value of cards and gives point 
    # Determine the card value for Player 1
    global player1_value
    global player2_value 

    player1_card_str = player1_card[0]  
    parts = player1_card_str.split(" of ")
    rank = parts[0]
    suit = parts[1]
    if rank.isdigit():  
        rank_value = int(rank)
        player1_value = rank_value + 1  
    else:  
        rank_value = face_card_values.get(rank, 0)
        player1_value = rank_value + 1  
    # Determine the card value for Player 2
    player2_card_str = player2_card[0] 
    parts = player2_card_str.split(" of ")
    rank = parts[0]
    suit = parts[1]
    if rank.isdigit(): 
        rank_value = int(rank)
        player2_value = rank_value + 1  
    else:  
        rank_value = face_card_values.get(rank, 0)
        player2_value = rank_value + 1 

    # Display the scores and update based on card comparison
    if player1_value > player2_value:
        print(f"{player1} wins the round +1")
        scores["player1"] += 1
    elif player1_value < player2_value:
        print(f"{player2} wins the round +1")
        scores["player2"] += 1
    else:
        print("It's a tie!")
    
    print(f"{player1} score: {scores["player1"]}             {player2} score: {scores["player2"]}")
    
#this function determines how the game is won 
def scoring_system_function(player1, player2, player1_deck, player2_deck, scores):
    #if one of them scores a 9 and 1
        if scores["player1"] == 1 and scores["player2"] <=1:
            print("Gameover, Early game end")
            results = print(f"{player1} wins, with a score of 9 to {scores["player2"]}")
            results_printed = {"Player": [player1,player2], "Score":[9, scores["player2"]]}
            #turning the code into panda dataframe 
            results_df = pd.DataFrame(results_printed)
            #saving the results into a csv using the panda dataframe styling 
            results_df.to_csv("Decktionary_game_results.csv", index = False)
            print("Results have been sasved to 'Decktionary_game_results.csv'!")
            print("It was fun playing with you!")
            return True
        
        elif scores["player2"]  == 1 and scores["player1"]  <=1:
            print("Gameover, Early game end")
            results = print(f"{player2} wins, with a score of {scores["player1"]} to 9")
            print(results)
            results_printed = {f"Player": [player1,player2], "Score":[scores["player2"], 9]}
            #turning the code into panda dataframe 
            results_df = pd.DataFrame(results_printed)
            #saving the results into a csv using the panda dataframe styling 
            results_df.to_csv("Decktionary_game_results.csv", index = False)
            print("Results have been sasved to 'Decktionary_game_results.csv'!")
            print("It was fun playing with you!")
            return True
        
        #if one of them scores a 16 to 0
        elif scores["player1"]  ==16 and scores["player2"]  ==0:
            print("Gameover, Shot to the Moon")
            print(f"{player2} earns +17 points")
            results = print(f"{player2} wins, with a score of 16 to 17")
            results_printed = {"Player": [player1,player2], "Score": [16,17]}
            #turning the code into panda dataframe 
            results_df = pd.DataFrame(results_printed)
            #saving the results into a csv using the panda dataframe styling 
            results_df.to_csv("Decktionary_game_results.csv", index = False)
            print("Results have been sasved to 'Decktionary_game_results.csv'!")
            print("It was fun playing with you!")
            return True
        
        elif scores["player2"] == 16 and scores["player1"]  == 0:
            print("Gameover, Shot to the Moon")
            print(f"{player1} earns +17 points")
            results = print(f"{player1} wins, with a score of 17 to 16")
            results_printed = {"Player": [player1,player2], "Score":[17,16]}
            #turning the code into panda dataframe 
            results_df = pd.DataFrame(results_printed)
            #saving the results into a csv using the panda dataframe styling 
            results_df.to_csv("Decktionary_game_results.csv", index = False)
            print("Results have been sasved to 'Decktionary_game_results.csv'!")
            print("It was fun playing with you!")
            return True
        
    #if one of their decks is empty 
        if not player1_deck or not player2_deck:
            print(f"Gameover, {player1} has no more cards")
            if scores["player1"] > scores["player2"]:
                results = print(f"{player1} wins, with a score of {scores["player1"]} to {scores["player2"]}")
                results_printed = {"Player": [player1,player2], "Score":[scores["player1"], scores["player2"]]}
                #turning the code into panda dataframe 
                results_df = pd.DataFrame(results_printed)
                #saving the results into a csv using the panda dataframe styling 
                results_df.to_csv("Decktionary_game_results.csv", index = False)
                print("Results have been sasved to 'Decktionary_game_results.csv'!")
                print("It was fun playing with you!")
                return True
            
            elif scores["player1"] < scores["player2"]:
                results = print(f"{player2} wins, with a score of {scores["player1"]} to {scores["player2"]}")
                results_printed = {"Player": [player1,player2], "Score":[scores["player1"], scores["player2"]]}
                #turning the code into panda dataframe 
                results_df = pd.DataFrame(results_printed)
                #saving the results into a csv using the panda dataframe styling 
                results_df.to_csv("Decktionary_game_results.csv", index = False)
                print("Results have been sasved to 'Decktionary_game_results.csv'!")
                print("It was fun playing with you!")
                return True

            elif scores["player1"] == scores["player2"] :
                results = print(f"Its a tie!  {scores["player1"]} to {scores["player2"]}")
                results_printed = {"Player": [player1,player2], "Score":[scores["player1"], scores["player2"]]}
                #turning the code into panda dataframe 
                results_df = pd.DataFrame(results_printed)
                #saving the results into a csv using the panda dataframe styling 
                results_df.to_csv("Decktionary_game_results.csv", index = False)
                print("Results have been sasved to 'Decktionary_game_results.csv'!")
                print("It was fun playing with you!")
                return True
        return False    



