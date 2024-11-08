import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, RED, DPI, BLACK, WHITE, doi_thu, GREEN_DAM_5E7B6F,GREEN_NHAT_DDE5D0,GREEN_CCDDA7,YELLOW_NHAT_F3EFCA, sound, soundBtn
from menuGame import screen, main_menu,load_and_transform_img, exit_red_btn, get_frame_and_blit_img, render_text

LINK_IMAGE_CELL = "image//board//cell.png" # Hình ảnh ô trống
LINK_IMAGE_CELL_X = "image//board//cell_x.png" 
LINK_IMAGE_CELL_O = "image//board//cell_o.png"
LINK_IMAGE_CELL_EFFECT = "image//board//cell_effect.png"
LINK_IMAGE_FINAL_MOVE_CELL = "image//board//final_move_cell.png"
LINK_IMAGE_BACKGROUND = "image//background.png"
LINK_IMAGE_BACKGROUND_RIGHT = "image//background_right.png"
LINK_IMAGE_BACKGROUND_RIGHT_UP = "image//background_right_up.png"
LINK_IMAGE_ICON_APP = "image//icon_game.png"

LINK_IMAGE_BUTTON_REPLAY = "image//buttonPlay//button_replay.png"
LINK_IMAGE_BUTTON_UNDO = "image//buttonPlay//button_undo.png"
LINK_IMAGE_BUTTON_MENU = "image//buttonPlay//button_menu.png"
LINK_IMAGE_BUTTON_HISTORY = "image//buttonPlay//button_his.png"
LINK_IMAGE_BUTTON_REPLAY_PRESSED = "image//buttonPlay//button_replay_pressed.png"
LINK_IMAGE_BUTTON_UNDO_PRS = "image//buttonPlay//button_undo_prs.png"
LINK_IMAGE_BUTTON_MENU_PRS = "image//buttonPlay//button_menu_prs.png"
LINK_IMAGE_BUTTON_HISTORY_PRS = "image//buttonPlay//button_his_prs.png"

LINK_MUSIC = "image//buttonPlay//music.png"
LINK_MUTE = "image//buttonPlay//mute.png"

# from numpy import array
pygame.init()

#Đặt title cho window
pygame.display.set_caption("Caro Game")

TABLE_SIZE = WINDOW_HEIGHT

img_cell = pygame.image.load(LINK_IMAGE_CELL)  
img_cell_x = pygame.image.load(LINK_IMAGE_CELL_X)
img_cell_o = pygame.image.load(LINK_IMAGE_CELL_O)
img_final_move_cell = pygame.image.load(LINK_IMAGE_FINAL_MOVE_CELL)
img_cell_effect = pygame.image.load(LINK_IMAGE_CELL_EFFECT)
img_icon = pygame.image.load(LINK_IMAGE_ICON_APP) 
pygame.display.set_icon(img_icon)

img_background = load_and_transform_img(LINK_IMAGE_BACKGROUND,DPI)

img_background_right = pygame.image.load(LINK_IMAGE_BACKGROUND_RIGHT) # nc đi trc mang màu này, đặt hình size nào cũng đc miễn có màu và to hơn cell size
rect_img_luotChoi = (260//DPI,260//DPI)
img_luot_x = pygame.transform.scale(img_cell_x, rect_img_luotChoi)
img_luot_o = pygame.transform.scale(img_cell_o, rect_img_luotChoi)



font_time = pygame.font.SysFont('Times New Roman', 80)
font_luot_dau = pygame.font.Font('font//Inter_Bold.ttf', 80 //DPI)
font_inter_bold = pygame.font.Font('font//Inter_Bold.ttf', 120 //DPI)

font_thanh_phan_ty_so = pygame.font.Font('font//Inter_Regular.ttf', 50//DPI)
#============================
text_denLuot = font_luot_dau.render("Đến lượt:",True, BLACK)
text_time = font_luot_dau.render("Time:", True, BLACK)

numOfAI = 0
def setNumOfAI(num):
    global numOfAI
    numOfAI = num


def display_text_TiSo(mode , string1,string2, number) :
    if mode == 0: # pvp play v play
        t1 = "Player 1: "
        t2 = "Player 2: "
    else:
        ta = "Player: "
        tb = "Máy: "
        if numOfAI == 1: # ai la quan 1 X
            t1 = tb
            t2 = ta
        else: 
            t2 = tb
            t1 = ta
    
    text1 = t1 + string1
    text2 = t2 + string2
    text_display_player = { 
        1: font_thanh_phan_ty_so.render(text1, True, BLACK),
        2: font_thanh_phan_ty_so.render(text2, True, BLACK)
    }
    return text_display_player[number]


# input là self.currentplayer 1,2
text_luot_xo = {
    1: font_luot_dau.render("Player 1", True, BLACK),
    2: font_luot_dau.render("Player 2",True,RED)
}

text_win = {
    1:font_inter_bold.render("X thắng",True,BLACK),
    2:font_inter_bold.render("O thắng",True,RED),
    3:font_inter_bold.render("Hòa",True,GREEN_DAM_5E7B6F)
}

img_luotChoi = {
    1: img_luot_x,
    2: img_luot_o
}

#button
replay_button = load_and_transform_img(LINK_IMAGE_BUTTON_REPLAY,DPI)
undo_button = load_and_transform_img(LINK_IMAGE_BUTTON_UNDO,DPI)
menu_button =load_and_transform_img(LINK_IMAGE_BUTTON_MENU,DPI)
his_button=load_and_transform_img(LINK_IMAGE_BUTTON_HISTORY,DPI)

replay_pressed_button = load_and_transform_img(LINK_IMAGE_BUTTON_REPLAY_PRESSED,DPI)
undo_prs_btn = load_and_transform_img(LINK_IMAGE_BUTTON_UNDO_PRS,DPI)
menu_prs_btn =load_and_transform_img(LINK_IMAGE_BUTTON_MENU_PRS,DPI)
his_prs_btn =load_and_transform_img(LINK_IMAGE_BUTTON_HISTORY_PRS,DPI)

music_button = load_and_transform_img(LINK_MUSIC,DPI*4)
mute_button = load_and_transform_img(LINK_MUTE,DPI*4)
#=======================
replay_btn = replay_button
undo_btn = undo_button
menu_btn = menu_button
his_btn = his_button

music_btn = music_button

list_his = []


def add_to_history(list_his, luotDau, win, time):
    # Tạo một dictionary cho lượt đấu hiện tại
    dict_current = {
        'Lượt đấu': luotDau,
        'Win' : win,
        'Time': time
    }
    # Thêm dictionary vào danh sách
    list_his.append(dict_current)

# def render_text(screen, font, text, color, viTrix, viTriy):
#     text_surface = font.render(text, True, color)
#     screen.blit(text_surface, (viTrix, viTriy))

def print_his(lisHis, screen, x,y):
    viTriy = y+ 46
    # In ra thông tin của từng lượt đấu
    for value in lisHis:
        
        output = f"Lượt đấu: {value['Lượt đấu']}               Win: {value['Win']}              Time: {value['Time']}"
        
        
        render_text(screen, font_thanh_phan_ty_so, output, BLACK, x,viTriy)
        viTriy += 30
        print(output)


#check xem vị trí (i,j) nằm trong giới hạn bàn cờ không
def check_position_valid(board, index_row, jndex_column):
    if 0 <= index_row < len(board) and 0 <= jndex_column < len(board):  #i,j thuộc giới hạn bàn cờ [0, len bàn cờ)
        return True # => là vị trí hợp lệ
    else:
        return False # => ko hợp lệ


class CaroGame: 
    List_direction = (
        (-1,-1), # huong len sang trai
        (-1,0), # huong len 
        (-1,1), # len sang phai
        (0,-1) # sang trai 
    )

    def __init__(self,board_row,board_column,show = True):
        self.board_row = board_row # so hang
        self.board_column = board_column  #so cot
        self.cell_size = min(int(TABLE_SIZE / self.board_row), int(TABLE_SIZE / self.board_column))  # Cập nhật kích thước ô
        self.show = show # hiển thị or ko 
        self.table_width = self.cell_size * self.board_column
        self.table_height = self.cell_size * self.board_row
        

        if show == True: #neu hien thi
            # tao dict tu dien cho hinh anh cua cell 
            self.Dict_image_cell = {
                # set lại size ảnh cell theo cell size
                0: pygame.transform.scale(img_cell, (self.cell_size, self.cell_size)),  # Ô trống
                1: pygame.transform.scale(img_cell_x, (self.cell_size, self.cell_size)),  # Ô X
                2: pygame.transform.scale(img_cell_o, (self.cell_size, self.cell_size))  # Ô O
            }
            
            self.img_previous_move = pygame.transform.scale(img_final_move_cell, (self.cell_size, self.cell_size))  # Hình ảnh cho nước đi trước
            self.img_effect_move = pygame.transform.scale(img_cell_effect, (self.cell_size, self.cell_size)) 
            
            # self.screen = pygame.display.set_mode((1000, 700))  # Thiết lập kích thước cửa sổ
            self.screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

        self.run = True # kiểm soát vòng lặp trò chơi
        self.play_with_computer = False # check chế độ: chơi với máy ko? mặc định False 
        self.check_show_affect = False  # Biến kiểm tra có hiển thị ô anh huong
        self.check_show_his = False 
        self.check_music = True
        self.load_time = pygame.time.get_ticks() #số mili giây đã trôi qua kể từ khi pygame được khởi tạo
        self.countLuotDau = 0
        self.countXWin = 0
        self.countOWin = 0
        self.reset_game(True)  # Khởi tạo lại trò chơi

    def reset_game(self, check):
        if check == True:
            global list_his, menu_btn
            self.countLuotDau = 1
            self.countXWin = 0
            self.countOWin = 0
            list_his = []
            menu_btn = menu_button
        else:
            self.countLuotDau += 1
        
       
        self.board_game = []  # Khởi tạo bảng trò chơi = 1 list rỗng

        for i in range(self.board_row):  # Lặp qua số dòng
            self.board_game.append([0] * self.board_column ) # Tạo hàng mới với giá trị 0 (trống) * số cột ( = so cot phan tu 0)

        self.current_player = 1 # 1x 2o
        self.play_time = pygame.time.get_ticks()  # Lưu thời gian hiện tại
        self.play_time_show = pygame.time.get_ticks() - 1000  # Thời gian hiển thị
        self.winner  = 0  # ban đầu là 0 (chưa ai thắng)
        self.time_end = None  # Thời gian kết thúc
        self.list_move_history = [] # List undo
        self.list_undo_effect = []  # Lịch sử ảnh hưởng để undo #
        self.list_undo_limit = []  # Lịch sử các tọa độ để undo # gh giới hạn à?
        self.list_affect = []  # Danh sách các ô có thể đánh , ô ả h mà ????

        self.left = None  # Biến xác định tọa độ trái
        self.right = None  #phải
        self.up = None  #trên
        self.down = None  #dưới

        
    def import_board(self, board ):
        self.reset_game(False)  # Khởi tạo lại trò chơi
        self.board_game = []  # Khởi tạo lại bảng

        for i in range(len(board)):  # Lặp qua chiều dài của bảng
            self.board_game.append(board[i].copy()) # Sao chép giá trị bảng input vào bảng game

        self.board_row =  len(board) # update số hàng
        self.board_column = len(board[0])  # update số cột, là số cột trong hàng đầu tiên.
        self.cell_size = min(int(TABLE_SIZE / self.board_row), int(TABLE_SIZE / self.board_column))  # Cập nhật kích thước ô

        if self.show == True:# Nếu hiển thị
            self.Dict_image_cell = {
                # set lại size ảnh cell theo cell size
                0: pygame.transform.scale(img_cell, (self.cell_size, self.cell_size)),  # Ô trống
                1: pygame.transform.scale(img_cell_x, (self.cell_size, self.cell_size)),  # Ô X
                2: pygame.transform.scale(img_cell_o, (self.cell_size, self.cell_size))  # Ô O
            }
            self.img_previous_move = pygame.transform.scale(img_final_move_cell, (self.cell_size, self.cell_size))
            self.img_effect_move = pygame.transform.scale(img_cell_effect, (self.cell_size, self.cell_size)) 
      
        self.import_list_affect()

    def import_list_affect(self):
        self.list_affect = []
        res = {1:0,2:0}
        for y in range(self.board_row):
            for x in range(self.board_column):
                for xm,ym in self.List_direction:
                    if self.board_game[y][x] != 0:
                        for i in range(-2,3):
                            if i != 0:
                                if check_position_valid(self.board_game, x+i*xm , y + i*ym):
                                    if (x+i*xm,y+i*ym) not in self.list_affect and self.board_game[y+i*ym][x+i*xm] == 0:
                                        self.list_affect.append((x+i*xm,y+i*ym))
                        if self.left == None:
                            self.left = x
                            self.right = x
                            self.up = y
                            self.down = y
                        else:
                            if x < self.left: self.left = x
                            elif x > self.right: self.right = x
                            if y < self.up: self.up = y
                            elif y > self.down: self.down = y

    def get_current_board(self):
        list_res = [] # Khởi tạo danh sách để lưu bản sao của board
        for i in range(len(self.board_game)):
            list_res.append(self.board_game[i].copy())  # Thêm bản sao của từng hàng vào danh sách
        return list_res # Trả về bản sao của bảng
    
    

    def set_player_vs_computer_mode(self):
        self.play_with_computer = True  # Đặt chế độ chơi với bot

    def set_player_vs_player_mode(self):
        self.play_with_computer = False  # Đặt chế độ chơi với người

    

    #lượt đấu
    def display_luot_dau(self):
        
        KC_W = ((WINDOW_WIDTH - (self.table_width+5)) - 857//DPI)//2 #vi tri dặt khung luot choi (vi tri thuc te 46 // 2)
        KC_H = 20 // DPI # 19 
        toa_do_x = self.table_width+5 + KC_W
        toa_do_y = 133//DPI + KC_H 
        width_frame = 857 // DPI 
        height_frame = 465 // DPI
        border_width = 4 // DPI

        render_text(self.screen, font_luot_dau,"Caro Game",WHITE,toa_do_x, 6)
        rect_hcn_luotDau = (toa_do_x,toa_do_y,width_frame,height_frame)

        text1 = "Lượt đấu: " +str(self.countLuotDau)
        text_luot_dau = font_luot_dau.render(text1 , True, BLACK)
        

        #ve nen cua khung luot dau - fill
        pygame.draw.rect(self.screen,GREEN_NHAT_DDE5D0,rect_hcn_luotDau,border_radius = 15 // DPI ) 
        #vẽ 1 khung hcn bo goc tron
        pygame.draw.rect(self.screen,BLACK,rect_hcn_luotDau,width = border_width,border_radius = 15 // DPI ) # thuc te // dpi
        
        self.screen.blit(text_luot_dau, (toa_do_x +70// DPI, toa_do_y+44// DPI))
        

        cell_mini_size = 75//DPI
        
        pygame.draw.rect(self.screen, WHITE,(toa_do_x +70//DPI,toa_do_y +270//DPI,cell_mini_size, cell_mini_size) )
        img_cell_x_mini = pygame.transform.scale(img_cell_x, (cell_mini_size,cell_mini_size)  )
        self.screen.blit(img_cell_x_mini, (toa_do_x +70//DPI,toa_do_y +270//DPI))
        pygame.draw.rect(self.screen,BLACK,(toa_do_x +70//DPI,toa_do_y +270//DPI,cell_mini_size, cell_mini_size),width = 1 )

        pygame.draw.rect(self.screen, WHITE,(toa_do_x +70//DPI,toa_do_y +368//DPI,cell_mini_size, cell_mini_size) )
        img_cell_o_mini = pygame.transform.scale(img_cell_o, (cell_mini_size,cell_mini_size)  )
        self.screen.blit(img_cell_o_mini, (toa_do_x +70//DPI,toa_do_y +368//DPI))
        pygame.draw.rect(self.screen,BLACK,(toa_do_x +70//DPI,toa_do_y +368//DPI,cell_mini_size, cell_mini_size),width = 1 )

        
        str1 = str(self.countXWin)
        str2 = str(self.countOWin)
        if self.play_with_computer == False: #pvp
            self.screen.blit(display_text_TiSo(0,str1,str2,1), (toa_do_x + 166//DPI, toa_do_y+274//DPI)) # may - player
            self.screen.blit(display_text_TiSo(0,str1,str2,2), (toa_do_x + 166//DPI, toa_do_y+372//DPI)) 
        else: 
            self.screen.blit(display_text_TiSo(1,str1,str2,1), (toa_do_x + 166//DPI, toa_do_y+274//DPI)) 
            self.screen.blit(display_text_TiSo(1,str1,str2,2), (toa_do_x + 166//DPI, toa_do_y+372//DPI))  # player1 - 2
        str3 = "Tỷ số: " + str(self.countXWin) + " - " + str(self.countOWin)
        text_ty_so = font_luot_dau.render(str3, True, BLACK)
        self.screen.blit(text_ty_so, (toa_do_x +70// DPI, toa_do_y+147// DPI))
        
            


    def display_luot_choi(self):
        KC_W = ((WINDOW_WIDTH - (self.table_width+5)) - 857//DPI)//2 #vi tri dặt khung luot choi (vi tri thuc te 46 // 2)
        KC_H = 20 // DPI # 19 
        #toa do frame luot choi
        toa_do_x = self.table_width+5 + KC_W # = luot dau
        toa_do_y = 133//DPI + KC_H*2 + (465 // DPI) #mau xanh fisrt + height khung luot dau 
        width_frame = 857 // DPI # = luot dau
        height_frame = 321 // DPI # khac
        border_width = 4 // DPI
        rect_hcn_luotChoi = (toa_do_x,toa_do_y,width_frame,height_frame)

        pygame.draw.rect(self.screen,GREEN_CCDDA7,rect_hcn_luotChoi,border_radius = 15 // DPI ) #hcn xanh
        pygame.draw.rect(self.screen,BLACK,rect_hcn_luotChoi,width = border_width,border_radius = 15 // DPI ) #khung den
        
        
        #text
        toa_do_x_text = toa_do_x + 45// DPI #thay doi
        toa_do_y_text = toa_do_y+ 44// DPI
        rect_text = (toa_do_x_text, toa_do_y_text )
        rect_text_2 = (toa_do_x_text, toa_do_y_text+98//2 )
        
        rect_img_xo = (toa_do_x+width_frame-44//DPI-260//DPI, toa_do_y+height_frame-29//DPI-260//DPI )
        xImgXO, yImgXO = rect_img_xo
        
        if self.winner == 0:  # Nếu trò chơi chưa kết thúc
            self.screen.blit(text_denLuot, rect_text)
            if self.play_with_computer:  # Nếu đang chơi với máy
                self.screen.blit(text_luot_xo[self.current_player], rect_text_2)  # Vẽ hình ảnh lượt đi máy
                pygame.draw.rect(self.screen,WHITE,(xImgXO,yImgXO,260//DPI,260//DPI) )
                self.screen.blit(img_luotChoi[self.current_player], rect_img_xo)
            else:
                self.screen.blit(text_luot_xo[self.current_player], rect_text_2)  # Vẽ hình ảnh lượt đi của người chơi
                pygame.draw.rect(self.screen,WHITE,(xImgXO,yImgXO,260//DPI,260//DPI) )
                self.screen.blit(img_luotChoi[self.current_player], rect_img_xo)
        else:
            rect_text_win = text_win[self.winner].get_rect(center = (toa_do_x + width_frame//2, toa_do_y + height_frame//2))
            self.screen.blit(text_win[self.winner], rect_text_win)  # Vẽ hình ảnh kết quả

    def display_time(self):
        '''
        screen
        color
        (x,y,w,h) (700 - int(0.06*self.cell_size),200,300 + int(0.06*self.cell_size),200)
        '''

        KC_W = ((WINDOW_WIDTH - (self.table_width+5)) - 857//DPI)//2 #vi tri dặt khung luot choi (vi tri thuc te 46 // 2)
        KC_H = 20 // DPI # 19 
        #toa do frame luot choi
        toa_do_x = self.table_width+5 + KC_W # =  luot dau
        toa_do_y = 133//DPI + KC_H*3 + (465 // DPI) + 321//DPI #  mau xanh fisrt + KC_h +height khung luot dau + KC + height khung luotChoi + KC + h khung time
        width_frame = 857 // DPI # = luot dau
        height_frame = 169 // DPI # khac
        border_width = 4 // DPI
        rect_frame_time = (toa_do_x,toa_do_y,width_frame, height_frame)
        rect_text_time = (toa_do_x +33//DPI, toa_do_y+ 36//DPI)# Time:
        rect_time = (toa_do_x +270//DPI, toa_do_y) #time hien thi
        pygame.draw.rect(self.screen,YELLOW_NHAT_F3EFCA,rect_frame_time,border_radius = 15 // DPI ) #hcn xanh
        pygame.draw.rect(self.screen,BLACK,rect_frame_time,width = border_width,border_radius = 15 // DPI ) #khung den
       
        if self.winner == 0: #game chua end
            if pygame.time.get_ticks() - self.play_time_show > 1000:
                self.play_time_show = pygame.time.get_ticks()
                time = (pygame.time.get_ticks() - self.play_time)//1000
                phut = time // 60
                giay = time % 60
                stringTime = ""
                if phut < 10:
                    stringTime += "0"
                stringTime += str(phut) + ":"
                if giay < 10:
                    stringTime += "0"
                stringTime += str(giay)
                
                
                self.img_time = font_time.render(stringTime,True, GREEN_DAM_5E7B6F)
                self.pos_img_time = self.img_time.get_rect() #vi tri img time
                self.pos_img_time.topleft = rect_time
                
        else:
            if self.time_end == None: 
                time = (pygame.time.get_ticks() - self.play_time)//1000
                phut = time // 60
                giay = time % 60
                stringTime = ""
                if phut < 10:
                    stringTime += "0"
                stringTime += str(phut) + ":"
                if giay < 10:
                    stringTime += "0"
                stringTime += str(giay)
                self.time_end = time
                if self.winner ==1: stringwin = 'X'
                elif self.winner ==2: stringwin ='O'
                elif self.winner ==3: stringwin = "HÒA"
                add_to_history(list_his, self.countLuotDau,stringwin ,stringTime)
                

        self.screen.blit(self.img_time,self.pos_img_time) 
        
        self.screen.blit(text_time, rect_text_time)
    
    
            
    def display_button(self):
        KC_H = 20 // DPI # 19 
        x_btn_replay = (self.table_width + (WINDOW_WIDTH-self.table_width)//2)
        y_btn_replay = 133//DPI + KC_H*4 + (465 // DPI) + 321//DPI + 169//DPI
        self.replay_button_frame = get_frame_and_blit_img(replay_btn,x_btn_replay, y_btn_replay+ (191//2)//DPI,2) #select 2 center

        x_btn_menu = x_btn_replay
        y_btn_menu = y_btn_replay + KC_H + 191//DPI
        self.menu_btn_frame =get_frame_and_blit_img(menu_btn,x_btn_menu,y_btn_menu + (191//2)//DPI,2)
        
        # center menu - 1/2 menu - kc - 1/2 undo = center undo
        x_btn_undo = x_btn_menu - (202//2) // DPI - KC_H - (278//2)//DPI
        y_btn_undo = y_btn_menu
        self.undo_btn_frame = get_frame_and_blit_img(undo_btn, x_btn_undo,y_btn_undo + (191//2)//DPI,2)

        x_his = x_btn_menu + (202//2) // DPI + KC_H + (278//2)//DPI
        y_his = y_btn_menu 
        self.his_btn_frame=get_frame_and_blit_img(his_btn,x_his,y_his + (191//2)//DPI,2)
    

    def show_history(self):
       
        #1/2 window - 1/2 hinh = vitri center his
        width = 4/5*WINDOW_WIDTH
        height = 4/5*WINDOW_HEIGHT
        xhis = WINDOW_WIDTH//2 - width //2
        yhis = WINDOW_HEIGHT//2 - height//2
        
        border_width = 4 // DPI
        rect_show_his = (xhis,yhis,width,height)
        pygame.draw.rect(self.screen,YELLOW_NHAT_F3EFCA,rect_show_his,border_radius = 15 // DPI ) #hcn 
        pygame.draw.rect(self.screen,BLACK,rect_show_his,width = border_width,border_radius = 15 // DPI ) #khung den
        
        rect_tieuDe = (xhis,yhis, width, 80)
        pygame.draw.rect(self.screen,GREEN_CCDDA7,rect_tieuDe,border_radius = 15 // DPI ) #hcn 
        pygame.draw.rect(self.screen,BLACK,rect_tieuDe,width = border_width,border_radius = 15 // DPI ) #khung den
        first_show = f"Lượt đấu       Win          Time"
        render_text(self.screen, font_luot_dau, first_show, GREEN_DAM_5E7B6F, xhis+33,yhis+25)
        print_his(list_his, self.screen,xhis+33,yhis+36)
        
        self.exit_red_btn_frame = get_frame_and_blit_img(exit_red_btn,xhis+width-7,yhis + 7,3)#3 topright

    
    def draw_game(self):
        global music_btn
        self.screen.blit(img_background, (0, 0))  # Vẽ hình nền, đặt tại vị trí (0,0) 
        # them nen ben phai 
        self.screen.blit(img_background_right, (self.table_width + 5, 0))  # Vẽ hình bên phải , toa do x = begin tu chieu rong bang
        # hcn goc tren phai
        pygame.draw.rect(self.screen, GREEN_DAM_5E7B6F, (self.table_width+5, 0, WINDOW_WIDTH - self.table_width+5,133// DPI))
        
        
        self.display_luot_dau()
        self.display_luot_choi()
        self.display_time() #vẽ time
        self.display_button()
    

        

        if len(self.list_move_history) != 0:  # Nếu có nước đi trước đó
            x, y = self.list_move_history[-1]  # Lấy nước đi cuối cùng
            self.screen.blit(self.img_previous_move, (x * self.cell_size +2, y * self.cell_size+3))  # Vẽ nền nước đi cuối cùng đó, +2,+3 sai so vi tri o trong bang
        
        if self.check_show_affect:  # Nếu hiển thị các ô bị ảnh hưởng
            for x, y in self.list_affect:
                self.screen.blit(self.img_effect_move, (x * self.cell_size +2, y * self.cell_size+3))  # Vẽ ô bị ảnh hưởng
        

        for i in range(self.board_row):  # Lặp qua hàng
            for j in range(self.board_column):  # Lặp qua cột
                self.screen.blit(self.Dict_image_cell[self.board_game[j][i]], (i * self.cell_size +2, j * self.cell_size+3))  # Vẽ hình ảnh của từng ô, self.board_game[j][i] là 0,1,2 ứng với hình ảnh empty, x,o
        
        # draw khung bảng
        '''
        self.screen nơi sẽ vẽ -cửa sổ hiển thị
        Màu
        (0, 0): Tọa độ (x, y)
        table_width
        table_height
        Độ dày của viền 6% chiều rộng ô (cell).
        Bán kính bo tròn cac góc 5 pixel
        '''
        toa_do_x_table = 0 #0
        toa_do_y_table = 0 #0
        
        boarder_width = int(0.09*self.cell_size)
        pygame.draw.rect(self.screen, GREEN_DAM_5E7B6F, (toa_do_x_table +2, toa_do_y_table+3, self.table_width, self.table_height), width=boarder_width, border_radius=0)  # Vẽ khung xung quanh bảng
        
        if self.check_music:
            music_btn = music_button
        else:
            music_btn = mute_button
            
        self.musicFrame = get_frame_and_blit_img(music_btn,WINDOW_WIDTH-5,  1, 3) # 3 topright

        if self.check_show_his: 
            self.show_history()
        
        pygame.display.update()  # Cập nhật màn hình


    def computer_move(self, x, y):
        # y la i, x la j
        # neu game chua end & vi tri hop le & cell đang empty
        if self.winner == 0 and check_position_valid(self.board_game, x,y) == True and self.board_game[y][x] == 0:
            if self.current_player == 1: #human
                self.board_game[y][x] =1 # đánh dấu player1 đánh ô tại hàng y cột x 
            else: 
                self.board_game[y][x] =2


            self.current_player = doi_thu[self.current_player] # Chuyển lượt 
            self.list_move_history.append([x,y]) # Lưu nước đi vào danh sách lsu move
            
            self.list_undo_effect.append(self.list_affect.copy())  # Lưu danh sách ô bị ảnh hưởng
            self.list_undo_limit.append((self.left,self.right,self.up,self.down))  # Lưu biên giới
            self.update_limit(x,y)
            
            self.winner = self.check_winner()  # Kiểm tra kết quả trò chơi, ai win chua
        

    def update_limit(self, x, y):
    # Cập nhật biên giới của vùng đã chơi dựa trên vị trí nước đi (x, y)
        if self.left == None:
            # Nếu chưa có biên trái, thiết lập biên cho vùng chơi
            self.left = x
            self.right = x
            self.up = y
            self.down = y
        else:
            # Cập nhật biên trái và phải nếu nước đi mới nằm ngoài các biên hiện tại
            if x <  self.left:   self.left = x  # Cập nhật biên trái
            elif x > self.right: self.right = x  # Cập nhật biên phải
            # Cập nhật biên trên và dưới
            if y < self.up:      self.up = y  #  trên
            elif y > self.down:  self.down = y  #  dưới

        # Nếu nước đi mới nằm trong danh sách ô bị ảnh hưởng, xóa nó khỏi danh sách
        if (x, y) in self.list_affect:
            self.list_affect.remove((x, y))

        # Kiểm tra các ô ảnh hưởng xung quanh vị trí nước đi
        for xm, ym in self.List_direction: # list 4 huong
            if self.board_game[y][x] != 0:  # Nếu ô hiện tại không rỗng
                for i in range(-2, 3):  # Kiểm tra trong khoảng từ -2 đến 2 ô
                    if i != 0:  # Bỏ qua ô hiện tại
                        # Kiểm tra xem vị trí mới có nằm trong giới hạn không
                        x_new = x + i * xm
                        y_new = y + i * ym
                        if check_position_valid(self.board_game, x_new, y_new) == True:
                            # Nếu ô mới chưa bị ảnh hưởng và ô đó là rỗng
                            if (x_new, y_new) not in self.list_affect and self.board_game[y_new][x_new] == 0:
                                self.list_affect.append((x_new, y_new))  # Thêm ô vào danh sách ảnh hưởng

    # def lay_L_nuoc_di(self):
    def get_list_move_affected(self):
    # Trả về bản sao của danh sách ô bị ảnh hưởng
        return self.list_affect.copy()
    
    def get_limit(self):
        return self.left,self.right,self.up,self.down
    
    # lệnh undo hoàn tác nc di
    def undo(self, num = 1): 
        for i in range(num):
            if len(self.list_move_history) != 0:  # Nếu còn nước đi để hoàn tác, tuc la lsu move con nc di
                # Khôi phục danh sách ô bị ảnh hưởng từ danh sách undo
                self.list_affect = self.list_undo_effect[-1]

                # Khôi phục biên giới từ danh sách undo
                self.left,self.right,self.up,self.down = self.list_undo_limit[-1]

                 # Lấy nước đi cuối cùng
                x, y = self.list_move_history[-1]
                self.board_game[y][x] = 0  # Đặt ô đó về trạng thái rỗng
        
                # Xóa nước đi cuối cùng và các thông tin liên quan
                self.list_move_history.pop(-1)
                self.list_undo_effect.pop(-1)
                self.list_undo_limit.pop(-1)

                self.current_player = doi_thu[self.current_player]  # Chuyển lượt
                self.winner = 0  # Đặt lại kết quả trò chơi
    
    def click_button(self, check_press, select):
        if select == 1: 
            global replay_btn  # Khai báo biến toàn cục
            button = replay_btn
            button_nhan = replay_pressed_button #nhấn nhả
            button_nha = replay_button
        elif select == 2:
            global undo_btn 
            button = undo_btn
            button_nhan = undo_prs_btn 
            button_nha = undo_button
        elif select == 3:
            global menu_btn 
            button = menu_btn
            button_nhan = menu_prs_btn
            button_nha =  menu_button
        elif select == 4: 
            global his_btn 
            button = his_btn
            button_nhan = his_prs_btn
            button_nha =  his_button
    
        if (check_press == 1): # nhấn
            soundBtn.play()
            button = button_nhan
        else: 
            button = button_nha
        
        if select == 1: replay_btn = button
        elif select ==2: undo_btn = button
        elif select == 3: menu_btn = button
        else: his_btn = button
        
    
    def event(self): 
        # Xử lý các sự kiện trong trò chơi
        for e in pygame.event.get():  # Lặp qua các sự kiện
            if e.type == pygame.QUIT:  # Nếu người dùng đóng cửa sổ
                self.run = False  # Đặt cờ dừng trò chơi
                pygame.mixer.quit()
                pygame.quit()  # Thoát Pygame
                return
            if e.type == pygame.MOUSEBUTTONDOWN:  # Nếu có nhấp chuột
                if self.winner == 0 and (self.play_with_computer == False or self.current_player == 1 or self.current_player == 2):  # Nếu trò chơi chưa kết thúc và lượt hợp lệ (1,2) (x,o)
                    x, y = pygame.mouse.get_pos()  # Lấy tọa độ chuột
                    x, y = x // self.cell_size, y // self.cell_size  # Chuyển đổi tọa độ chuột thành ô
                    
                    # Kiểm tra xem ô có hợp lệ không
                    if check_position_valid(self.board_game, x,y) == True and self.board_game[y][x] == 0 and self.check_show_his == False:
                        # Đánh dấu ô cho người chơi hiện tại
                        if self.current_player == 1:
                            self.board_game[y][x] = 1  # Nước đi của người chơi 1
                            sound.play(maxtime=2000)
                        else:
                            self.board_game[y][x] = 2  # Nước đi của người chơi 2
                            sound.play(maxtime=2000)
                        self.current_player = doi_thu[self.current_player] # Chuyển lượt
                     
                        # Lưu nước đi và trạng thái vào danh sách undo
                        self.list_move_history.append([x, y])
                        self.list_undo_effect.append(self.list_affect.copy())
                        self.list_undo_limit.append((self.left,self.right,self.up,self.down))
                        self.update_limit(x, y)  # Cập nhật biên giới
                        self.winner = self.check_winner()  # Kiểm tra kết quả
               
                if self.replay_button_frame.collidepoint(e.pos): # frame la 1 khung cua 
                    #replay select 1 
                    self.click_button(1,1)
                    self.reset_game(False)
                elif self.winner == 0 and self.undo_btn_frame.collidepoint(e.pos):
                    self.click_button(1,2)
                    if self.play_with_computer: self.undo(2)
                    else: self.undo()
                elif self.menu_btn_frame.collidepoint(e.pos):
                    self.click_button(1,3)
                    self.run = False
                    self.screen = screen
                    main_menu()
                elif self.his_btn_frame.collidepoint(e.pos):
                    self.click_button(1,4)
                    self.check_show_his = True
                elif self.check_show_his == True and self.exit_red_btn_frame.collidepoint(e.pos):
                    self.check_show_his = False
                elif self.musicFrame.collidepoint(e.pos):
                    self.check_music = not self.check_music
                    checkPauseMusic(self.check_music)
                    
            if e.type == pygame.MOUSEBUTTONUP:
                    # nhả = 0
                if self.replay_button_frame.collidepoint(e.pos): # frame la 1 khung cua 
                    self.click_button(0,1)
                elif self.undo_btn_frame.collidepoint(e.pos):
                    self.click_button(0,2)
                elif self.menu_btn_frame.collidepoint(e.pos):
                    self.click_button(0,3)
                elif self.his_btn_frame.collidepoint(e.pos):
                    self.click_button(0,4)   
                
            if e.type == pygame.KEYDOWN:  # Nếu có phím được nhấn
                if e.key == pygame.K_TAB:  # TAB
                    self.check_show_affect = not self.check_show_affect  #  hiển thị ô bị ảnh hưởng or ko 

    def check_winner_by_direction(self, x, y, xm, ym):
        # Kiểm tra kết quả theo hướng cụ thể
        x0, y0 = x, y  # Lưu vị trí ban đầu
        x -= xm  # Di chuyển một bước về hướng đã cho
        y -= ym
        count = 0  # Đếm số ô liên tiếp
        symbol = self.board_game[y0][x0]  # Lưu giá trị của ô ban đầu (0,1,2)
        while True:
            # Kiểm tra xem có vượt ra ngoài giới hạn hoặc ô này có gt != symbol cua o (x0,y0)
            if (not check_position_valid(self.board_game,x,y)) or symbol != self.board_game[y][x]:
                break  # Dừng 
            count += 1  # Tăng số ô liên tiếp
            x -= xm  # Tiếp tục di chuyển
            y -= ym
        
        # Khôi phục về vị trí ban đầu
        x, y = x0, y0
        x += xm  # Di chuyển một bước về hướng ngược lại
        y += ym
        while True:
            if (not check_position_valid(self.board_game,x,y)) or symbol != self.board_game[y][x]:
                break  # Dừng nếu không hợp lệ
            count += 1  # Tăng số ô liên tiếp
            x += xm  # Tiếp tục di chuyển
            y += ym
        if count < 4: # Nếu < 4 ô liên tiếp
            return 0   #trả về 0
        return symbol  # Trả về giá trị của ô thắng
         
    def check_winner(self):
        # Kiểm tra kết quả của trò chơi
        x, y = self.list_move_history[-1]  # Lấy nước đi cuối cùng
        # Kiểm tra theo các hướng khác nhau
        res = self.check_winner_by_direction(x, y, 1, 0)  # Kiểm tra theo hướng ngang
        if res != 0: 
            if res == 1: self.countXWin +=1
            elif res == 2: self.countOWin+=1
            return res # Nếu có người thắng, trả về kết quả
                        
        res = self.check_winner_by_direction(x, y, 0, 1)  # theo hướng dọc
        if res != 0: 
            if res == 1: self.countXWin +=1
            elif res == 2: self.countOWin+=1
            return res # Nếu có người thắng, trả về kết quả
              
        res = self.check_winner_by_direction(x, y, 1, 1)  #  hướng chéo từ trái lên phải
        if res != 0: 
            if res == 1: self.countXWin +=1
            elif res == 2: self.countOWin+=1
            return res
         
        res = self.check_winner_by_direction(x, y, 1, -1)  #  chéo từ phải lên trái
        if res != 0: 
            if res == 1: self.countXWin +=1
            elif res == 2: self.countOWin+=1
            return res
               
        if len(self.list_affect) == 0: 
            return 3  # Nếu không còn ô bị ảnh hưởng, trả về 3 (hòa)
        
        return 0  # Nếu chưa có ai thắng, hòa, trả về 0

    
    def wait(self):
        # Kiểm tra và vẽ lại màn hình nếu đã qua 1 giây
        if pygame.time.get_ticks() - self.load_time > 1000:
            self.load_time = pygame.time.get_ticks()  # Cập nhật thời gian tải
            self.draw_game()  # Vẽ lại màn hình
        pygame.event.get()  # Xử lý các sự kiện

    def run_game(self):
        # Xử lý sự kiện và vẽ lại màn hình nếu trò chơi vẫn đang chạy
        self.draw_game()
        self.event()  # Gọi hàm xử lý sự kiện
        if self.run == True:  # Nếu trò chơi vẫn đang chạy
            self.draw_game()  # Vẽ lại màn hình
        return self.run  # Trả về trạng thái trò chơi

    

def checkPauseMusic(check):
    if check:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    


















