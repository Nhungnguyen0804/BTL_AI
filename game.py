from CaroGame import CaroGame, setNumOfAI
import random
from caroScore import calculate_score
def sort_move(caro):
    list_move = caro.get_list_move_affected()
    list_optimal_move = []
    for x,y in list_move:
        caro.computer_move(x,y)
        if caro.winner == 0:
            list_optimal_move.append([calculate_score(caro,1),(x,y)])      
        elif caro.winner == 1:
            caro.undo() #return board, trc return de di lai nc di != 
            return [["x",(x,y)]]
        elif caro.winner == 2:
            caro.undo()
            return [["o",(x,y)]]
        else: 
            list_optimal_move.append([0,(x,y)])
        caro.undo()
    # sort nc di toi uu 
    if caro.current_player == 1: # sort giam dan
        list_optimal_move.sort(reverse=True)
    else: list_optimal_move.sort()
    return list_optimal_move

global caroMain
def minimax(caro, depth, max, root, alpha ):
    caroMain.wait()
    list_move_sorted = sort_move(caro) # list 2 thanh phan ( score va pos (x,y))
    
    # print(list_move_sorted)


    if root == True: # dang o root
        score = list_move_sorted[0][0] # p.tu first co chi so 0 la score
        x,y = list_move_sorted[0][1]
        if score =='x' or score =='o': 
            return [(x,y)] # tra luon pos (x y) ko can xet j nua       
        res = None
        list_res =[]
        for score, pos in list_move_sorted: # pos : tọa độ
            if depth !=1: 
                x,y = pos
                caro.computer_move(x,y)
                #nhánh, alpha root ko dc = -1 vi phu thuoc max,min
                # max => -1, min => -1
                branch = minimax(caro , depth-1, not max, False, None if res == None else res-1 if max else res+1)
                
                caro.undo()
            else:  
                # print('***nhanh root', score)
                branch = score #depth = 1 r
            
            if branch!=None:
                # root k bt den luot X hay O, k bt max hay min => can dk max = true thi ...
                if max == True and (res == None or branch > res):
                    print('xo', caro.current_player, 'depth',depth,'diem',score,'max',max,'toado',pos, 'nhanh',branch,'res kq',res)
                    list_res = [pos] # lay toa do cua từng score
                    res = branch
                elif max == False and (res == None or branch < res): # min
                    print('xo', caro.current_player, 'depth',depth,'diem',score,'max',max,'toado',pos, 'nhanh',branch,'res kq',res)
                    list_res = [pos] # lay toa do cua từng score
                    res = branch
                elif res == branch:
                    print('xo', caro.current_player, 'depth',depth,'diem',score,'toado append',pos, 'nhanh',branch,'res kq',res)
                    list_res.append(pos) # lay toa do cua từng score       
        return list_res
    else: #ko la root
        score = list_move_sorted[0][0]
        x,y = list_move_sorted[0][1]




        if score =='x': return 100000
        elif score == 'o': return -100000
        
        res = None
        for score, pos in list_move_sorted: #pos: toa do
            if depth !=1:
                x,y = pos
                caro.computer_move(x,y)
                branch = minimax( caro, depth-1,not max, False, res)
                caro.undo()
            else: 
                return score # ko la root & depth = 1 => tra luon ve diem 



            if branch != None:
                if max == True:
                    if res == None or branch > res: 
                        res = branch
                    if alpha != None and res >= alpha: 
                        return None
                else: #min
                    if res == None or branch < res: 
                        res = branch
                    if alpha != None and res <= alpha: 
                        return None
        return res

#X thi bmax= max, O thi min
# root luon true o lan goi first
# def ai_move(depth): #depth : do thminh
#     if caro_main.get_limit()[0] == None: 
#         x,y = caro_main.board_row //2, caro_main.board_column//2
#     else:
#         caro_phu.import_board(caro_main.board_game)
#         caro_phu.current_player = caro_main.current_player
#         L = minimax(caro_phu, depth, True if caro_main.current_player == 1 else False, True, None)
#         # L = list(set(L))
#         print('nhung nc di toi uu:', L)
#         x,y = random.choice(L)
#         print('x',x)
#         print('y',y)
#     caro_main.computer_move(x,y)
def ai_move(caro_main,caro_phu, depth): #depth : do thminh
    if caro_main.get_limit()[0] == None: 
        x,y = caro_main.board_row //2, caro_main.board_column//2
    else:
        caro_phu.import_board(caro_main.board_game)
        caro_phu.current_player = caro_main.current_player
        L = minimax(caro_phu, depth, True if caro_main.current_player == 1 else False, True, None)
        # L = list(set(L))
        print('nhung nc di toi uu:', L)
        x,y = random.choice(L)
        print('x',x)
        print('y',y)
    caro_main.computer_move(x,y)



def runPlayGame(checkPVC, checkmoveFirst):
    global caroMain
    from menuGame import sizeBoard
    size = sizeBoard

    caro_main = CaroGame(size,size)
    caroMain = caro_main
    #caro phụ
    caro_phu = CaroGame(caro_main.board_row, caro_main.board_column)

    caro_main.reset_game(True)
    while caro_main.run_game():
        if checkPVC == True:
            caro_main.set_player_vs_computer_mode()
            setNumOfAI(checkmoveFirst)
            if caro_main.current_player == checkmoveFirst: #checkmoveFirst = 1,2                
                ai_move(caro_main, caro_phu,3)
        else:
            caro_main.set_player_vs_player_mode()

# runPlayGame()