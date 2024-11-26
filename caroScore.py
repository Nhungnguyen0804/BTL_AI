from CaroGame import CaroGame, check_position_valid
from constants import doi_thu

# move len sang trai, len, len sang phai, sang trai
List_4_huong = [(-1,-1), (-1,0),(-1,1), (0,-1)]

def countEmptyCell(caro, x,y,xm,ym, numOfPlayerSymbol):
    countEmpty=0
    while (caro.board_game[y][x] == 0): # o rong
        countEmpty+=1
        if numOfPlayerSymbol + countEmpty > 3:  return countEmpty
        
        x += xm
        y += ym
        if check_position_valid(caro.board_game, x,y) == False: break
    
    return countEmpty

# điểm từng hướng 1 của quân cờ (quân o)
def score_tung_huong(caro, x,y, xm,ym):
    x0,y0 = x,y
    currentPlayer = caro.board_game[y][x]
    huong1 = 1
    count = 0 
    nhay_cach = False #chua nhay
    while True:
        x+=xm
        y+=ym
        if (check_position_valid(caro.board_game,x,y) == False 
            or caro.board_game[y][x] == doi_thu[currentPlayer]):
            huong1=0
            break

        if caro.board_game[y][x] == 0: #empty
            if nhay_cach == True:
                break
            else:
                x_nhay_cach =x+xm #tang 1 o
                y_nhay_cach=y+ym
                if check_position_valid(caro.board_game,x_nhay_cach, y_nhay_cach) and caro.board_game[y_nhay_cach][x_nhay_cach]== currentPlayer:
                    nhay_cach= True
                    continue
                break
            
        count+=1

    x1,y1 =x,y #x ,y of huong1 luu gt o khi end xet huong1
    #reset x,y ve ban dau
    x,y=x0,y0

    #xet huong ngc lai
    huong2=1
    while True:
        x-=xm
        y-=ym
        if check_position_valid(caro.board_game,x,y)==False or caro.board_game[y][x] == doi_thu[currentPlayer]:
            huong2=0
            break

        if caro.board_game[y][x] == 0:
            if nhay_cach == True:
                break
            else:
                x_nhay_cach =x-xm #tang 1 o
                y_nhay_cach=y-ym
                if check_position_valid(caro.board_game,x_nhay_cach, y_nhay_cach) and caro.board_game[y_nhay_cach][x_nhay_cach]== currentPlayer:
                    nhay_cach= True
                    continue
                break

        count += 1
    x2,y2 =x,y
    if huong1 == 1: 
        numOfEmptyCell = countEmptyCell(caro, x1,y1,xm,ym,count)
        if count + numOfEmptyCell <=3: huong1 = 0 # k du o di 5 quan co
    
    if huong2 == 1:
        numOfEmptyCell = countEmptyCell(caro,x2,y2,-xm,-ym,count)
        if count + numOfEmptyCell <=3: huong2 = 0
    
    if count > 3: count=3

    if nhay_cach == True: res_nhay_cach=0.75
    else: res_nhay_cach = 1
    score = 3**count* (huong1+huong2) * res_nhay_cach
    # print(score)
    return score

#ham tinh diem O
def score_o(caro,x,y):
    res = 0
    for xm,ym in List_4_huong:
        res += score_tung_huong(caro,x,y,xm,ym)

    return res

def calculate_score(caro, maxPlayer):
    Dict_res = {1: 0, 2: 0 }
    left,right,up,down = caro.get_limit()
    # print("left,right,up,down: ", left,right,up,down)
    
    if left != None: #3 cai kia giong left
        for y in range(up, down+1):
            for x in range(left,right+1):
                if caro.board_game[y][x] != 0:
                    Dict_res[caro.board_game[y][x]] += score_o(caro,x,y) # j ung truc x, i ung truc y

    # print(Dict_res)
    Dict_res[caro.current_player] *= 2
    # print(Dict_res)
    return Dict_res[maxPlayer] - Dict_res[doi_thu[maxPlayer]]





