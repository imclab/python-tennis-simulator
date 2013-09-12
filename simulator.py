import random
from model import TennisPlayer

def play_game(player1, player2):
    score = [0, 0]

    while True:
        if random.random() <= player1.first_serve:
            serving_player = player1.play_first_serve()
            returning_player = player2.play_first_serve_return()
    
        else:
            serving_player = player1.play_second_serve()
            returning_player = player2.play_second_serve_return()
    
        if serving_player == True and returning_player == False:
            score[0] += 1
    
        elif serving_player == False and returning_player == True:
            score[1] += 1
    
        elif serving_player == False and returning_player == False:
            if random.random() <= 0.275:
                score[0] += 1
        
            else:
                score[1] += 1
            
    
        elif serving_player == True and returning_player == True:
            if random.random() <= 0.5:
                score[0] += 1
        
            else:
                score[1] += 1
        
        if score[0] >= 4:
            break
        
        elif score[1] >= 4:
            break

    if score[0] >= 4:
        return player1

    elif score[1] >= 4:
        return player2
    
    elif score[0] == 3 and score[1] == 3:
        score[0] -= 1
        score[1] -= 1
        

def play_set(player1, player2):
    score = [0, 0]
    
    while True:
        if score[0] >= 6:
            break
    
        elif score[1] >= 6:
            break
            
        for n in range(2):
            if score[0] >= 6:
                break
    
            elif score[1] >= 6:
                break
                
            if n == 0:
                if play_game(player1, player2) == player1:
                    score[0] += 1
                else:
                    score[1] += 1
            
            else:
                if play_game(player2, player1) == player1:
                    score[0] += 1
                else:
                    score[1] += 1
                    
        if score[0] == 6 and score[0] - score[1] < 2:
            score[0] -= 1
            score[1] -= 1
        
        elif score[1] == 6 and score[1] - score[0] < 2:
            score[0] -= 1
            score[1] -= 1
        
        
    if score[0] == 6:
        return player1
    
    if score[1] == 6:
        return player2
                
    
def play_match(number_of_sets, player1, player2):
    score = [0, 0]
    for n in range(number_of_sets):
        if n % 2 == 0:
            if play_set(player1, player2) == player1:
                score[0] += 1
            
            else:
                score[1] += 1
        
        else:
            if play_set(player2, player1) == player2:
                score[1] += 1
            
            else:
                score[0] += 1
    if score[0] > score[1]:
        return 1
    
    else:
        return 2