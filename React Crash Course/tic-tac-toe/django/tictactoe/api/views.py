import threading
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data, DataSerializer 
from .timer_decorator import timer, print_return
import json
import random

with open("api/data.json", "r") as f:
    d = json.loads(''.join([i.strip() for i in f.readlines()]))
    d['turn'] = True
    d['player'] = 0
    d['bot'] = True
    d['moves'] = { "player1": [], "player2": [] }
    
    
# Create your views here.
def yield_func(request):
    
    def saveData(data):
        data['success'] = True
        gameData.data = data
        gameData.save()  
    
    def validateMove(data, bot_move, trial_n_err = 9):
            newBoxes = []
            for row in data['data']:
                newRow = []
                for box in row:
                    if box['box_id']==bot_move:
                        
                        if not box['state']:
                            box['state'] = True
                            box['player'] = "player2" if data['player']==0 else "player1"
                            # print(f"{'#'*100}\n\n{box}\n\n{'#'*100}")  
                            
                        else:
                            # print(f"{'#'*100}\n\n\nCOMMENCING TRIAL N ERR\n\n\n{'#'*100}")
                            
                            if trial_n_err > 0:  
                                validateMove(data, bot_move=trial_n_err-1, trial_n_err=trial_n_err-1)
                            else: 
                                break
                            
                    newRow.append(box)
                        
                        
                newBoxes.append(row)
            return newBoxes
    
    gameData = Data.objects.get(name='data')
    # gameData.data = d
    # gameData.save()
    # print(f"{'#'*100}\n\n\nSAVED { gameData.data }\n\n\n{'#'*100}")
    
    if request.method == 'PUT':
        data =  request.data 
        
        
        # 
                
        if data['bot']:
            if data['dataLoader']:
                botMove = botMoves(data, data['player'])
                data['moves']["player2" if data['player']==0 else "player1"].append(botMove)
                yield data
            else:
                botMove = data['moves']["player2" if data['player']==0 else "player1"][-1]
                if len(data['moves']['player1'])+len(data['moves']['player1'])<10 or data['player']:
                    data['data'] = validateMove(data, bot_move=botMove)
                    
                data['turn'] = not data['turn']
                winner = checkWin(data)
                if winner:
                    data["winner"] = winner  
                  
                t1 = threading.Thread(target=saveData, args=(data, ))
                t1.start()
                yield data
                t1.join()
    
        
    elif request.method == 'POST':
        # print(f"{'#'*100}\n\n\n{gameData.data}\n\n\n{'#'*100}")  
        
        if request.data == "restart":
            t1 = threading.Thread(target=saveData, args=(d, ))
            t1.start()
            yield d
            t1.join()
            
        elif float(request.data).is_integer():
            # print(f"{'#'*100}\n\n\n{request.data}\n\n\n{'#'*100}")  
            data = gameData.data
            data['player'] = int(request.data)
            
            if data['player']==1 and data['bot'] and len(data['moves']['player1'])+len(data['moves']['player2'])<9:
                botMove = random.randint(1, 9)
                data['moves']["player2" if data['player']==0 else "player1"].append(botMove)
                data['data'] = validateMove(data, botMove)
                data['turn'] = not data['turn']

            saveData(data)
            yield gameData.data
            
            
    return   

def checkWin(data: dict):
    win_patterns = ['123', '147', '159', '258', '357', '369', '456', '789']
    for player in data['moves']:
        player_moves = data['moves'][player]
        for wMove in win_patterns:
            points = 0
            for w in wMove:
                if player_moves.count(int(w))==1:
                    points+=1
            if points == 3:
                return player
    if len(data['moves']['player1'])+len(data['moves']['player1'])>9:
        return "Draw"
    return None

def botMoves(data:dict, player:int):
    moves = [data['moves'][player] for player in data['moves']]
    gameMoves = []
    player1 = data['moves']['player1']
    player2 = data['moves']['player2']
    gameMoves.extend(player1)
    gameMoves.extend(player2)
    win_patterns = ['123', '147', '159', '258', '357', '369', '456', '789']
    for move in moves:
        for i in range(len(win_patterns)):
            point = 0
            for w in win_patterns[i]:
                if move.count(int(w)) == 1:
                    point+=1
                if point == 2:
                    for x in win_patterns[i]:
                        if gameMoves.count(int(x))==0:
                            return int(x)
    even = [2, 4, 6, 8]
    try:
        botMove = int(moves[player][-1])-1
    except IndexError:
        return random.randint(1, 9)
    if gameMoves.count(5)==0:
        return 5
    elif even.count(botMove+1)>0:
        if gameMoves.count(botMove)==0:
            return botMove
    else:
        if moves[player].count(5) > 0:
            x = [1, 3, 7, 9]
            for i in x:
                if gameMoves.count(i)==0:
                    return i
        for i in even:
            if gameMoves.count(i)==0:
                return i
    m = [i for i in range(1, 10) if gameMoves.count(i)!=1]
    if m:
        return random.choice(m)
    else:
        return random.randint(1, 9)
        




@api_view(['GET', 'PUT', 'POST'])
# @timer
def index(request):
    gameData = Data.objects.filter(name='data').exists()  
    if gameData:
        try:
            f = next(yield_func(request))
            # print(f"{'#'*100}\n\n\n{f}\n\n\n{'#'*100}")
            return JsonResponse(f)
        except StopIteration as s:
            # print(f"{'#'*100}\n\n\nStopped\n\n\n{'#'*100}")
            gameData = Data.objects.get(name='data')
            serialized = DataSerializer(gameData, many=False) 
            return Response(serialized.data)
    else:        
        gameData = Data(name='data', data=d )
        gameData.save()
    
    serialized = DataSerializer(gameData, many=False) 
    return Response(serialized.data)