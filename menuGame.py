import pygame
import sys
from constants import WINDOW_WIDTH, WINDOW_HEIGHT,BLACK,DPI,YELLOW_NHAT_F3EFCA, soundBtn
#link image
LINK_IMAGE_MENU_BACKGROUND = "image\\Menu\\caro_menu_background.png"
LINK_IMAGE_START_BUTTON =  "image\\Menu\\button\\start.png"
LINK_IMAGE_START_PRESSED_BUTTON = "image\\Menu\\button\\start_pressed.png"
LINK_LV = "image\\Menu\\button\\lv.png"
LINK_LV_PRS = "image\\Menu\\button\\lv_prs.png"
LINK_HD = "image\\Menu\\button\\hd.png"
LINK_HD_PRS = "image\\Menu\\button\\hd_prs.png"
LINK_EXIT = "image\\Menu\\button\\ex.png"
LINK_EXIT_PRS = "image\\Menu\\button\\ex_prs.png"
#===============================
LINK_IMG_EXIT = "image\\Menu\\exit.png"
LINK_TANG = "image\\Menu\\tang1.png"
LINK_TANG_PRS = "image\\Menu\\tang2.png"
LINK_GIAM = "image\\Menu\\giam1.png"
LINK_GIAM_PRS = "image\\Menu\\giam2.png"
LINK_IMG_PVP = "image\\Menu\\button\\LVbutton\\pvp.png"
LINK_IMG_PVP1 = "image\\Menu\\button\\LVbutton\\pvp1.png" 
LINK_IMG_PVC = "image\\Menu\\button\\LVbutton\\pvc.png"
LINK_IMG_PVC1 = "image\\Menu\\button\\LVbutton\\pvc1.png"
LINK_IMG_MAY_X = "image\\Menu\\button\\LVbutton\\mayX.png"
LINK_IMG_MAY_X1 = "image\\Menu\\button\\LVbutton\\mayX1.png"
LINK_IMG_PLAYER_X = "image\\Menu\\button\\LVbutton\\playerX.png"
LINK_IMG_PLAYER_X1 = "image\\Menu\\button\\LVbutton\\playerX1.png"

LINK_CONTENT_HD = "image\\Menu\\nd_hd.png"

checkShowLV = False
checkShowHD = False
# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Menu")

#=======================
def load_and_transform_img(linkImg, sizeImg):
    img = pygame.image.load(linkImg).convert_alpha()
    img = pygame.transform.scale(img , (img.get_width()// sizeImg, img.get_height()//sizeImg))
    return img
def get_frame_and_blit_img(img, x,y, select):
    if select == 1:
        frame = img.get_rect(topleft =(x,y))
    elif select == 2:
        frame = img.get_rect(center =(x,y))
    elif select ==3:
        frame = img.get_rect(topright =(x,y))
    screen.blit(img,frame)
    return frame
#========================

menu_background = load_and_transform_img(LINK_IMAGE_MENU_BACKGROUND,DPI)
start_button = load_and_transform_img(LINK_IMAGE_START_BUTTON,DPI)
lv_button = load_and_transform_img(LINK_LV,DPI)
hd_button = load_and_transform_img(LINK_HD,DPI)
exit_button = load_and_transform_img(LINK_EXIT,DPI)

#nhấn
start_pressed_button=load_and_transform_img(LINK_IMAGE_START_PRESSED_BUTTON,DPI)
lv_prs_button=load_and_transform_img(LINK_LV_PRS,DPI)
hd_prs_button=load_and_transform_img(LINK_HD_PRS,DPI)
exit_prs_button=load_and_transform_img(LINK_EXIT_PRS,DPI)

#show lv
exit_red_btn = load_and_transform_img(LINK_IMG_EXIT,8)
pvc_button = load_and_transform_img( LINK_IMG_PVC, DPI)
pvp_button = load_and_transform_img(LINK_IMG_PVP,DPI)
mayDanhTrc_button = load_and_transform_img(LINK_IMG_MAY_X, DPI)
nguoiDanhTrc_button = load_and_transform_img(LINK_IMG_PLAYER_X,DPI)

pvc1_button = load_and_transform_img(LINK_IMG_PVC1, DPI)
pvp1_button = load_and_transform_img(LINK_IMG_PVP1,DPI)
mayDanhTrc1_button = load_and_transform_img(LINK_IMG_MAY_X1, DPI)
nguoiDanhTrc1_button = load_and_transform_img(LINK_IMG_PLAYER_X1, DPI)

tang1_button = load_and_transform_img(LINK_TANG,4)
tang2_button = load_and_transform_img(LINK_TANG_PRS,4)
giam1_button = load_and_transform_img(LINK_GIAM,4)
giam2_button = load_and_transform_img(LINK_GIAM_PRS,4)

content_hd = load_and_transform_img(LINK_CONTENT_HD,DPI)
#==============================================
start_btn = start_button
lv_btn = lv_button
hd_btn = hd_button
exit_btn = exit_button

tang_btn = tang1_button
giam_btn = giam1_button

#==============================================
start_button_frame = start_button.get_rect(topleft = (665,230))
lv_btn_frame = lv_button.get_rect(topleft = (665, 340))
hd_btn_frame = hd_button.get_rect(topleft = (665, 340 + 110))
exit_btn_frame = exit_button.get_rect(topleft = (665, 340 + 110 +110))
#==============================================
global exit_show_lv_frame 
global pvcFrame
global pvpFrame
global mayTrcFrame
global nguoiTrcFrame
global tangFrame
global giamFrame

global exitHDFrame

check_pvc = True
sizeBoard = 15 

def tangSize():
    global sizeBoard
    if sizeBoard <= 30: sizeBoard+=1

def giamSize():
    global sizeBoard
    if sizeBoard>5: sizeBoard -=1

def checkPVC(check):
    global pvc_btn,pvp_btn
    if check == True: #mode play vs computer
        pvc_btn = pvc_button
        pvp_btn = pvp1_button
    else:
        pvc_btn = pvc1_button
        pvp_btn = pvp_button

check_move_first = 1
def checkAI_move_first(check):
    global mayDanhTrc_btn,nguoiDanhTrc_btn
    if check == 1:
        mayDanhTrc_btn = mayDanhTrc_button
        nguoiDanhTrc_btn = nguoiDanhTrc1_button
    else:
        mayDanhTrc_btn = mayDanhTrc1_button
        nguoiDanhTrc_btn = nguoiDanhTrc_button




fontSelectSizeBoard = pygame.font.Font('font//Inter_Bold.ttf', 80 //DPI)
fontThuong = pygame.font.Font('font//Inter_Regular.ttf', 300//DPI)
def render_text(screen, font, text, color, viTrix, viTriy):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (viTrix, viTriy))

def render_text_center(screen, font, text, color, viTrix, viTriy):
    text_surface = font.render(text, True, color)
    text_rect  = text_surface.get_rect(center = (viTrix,viTriy))
    screen.blit(text_surface, text_rect)

def click_btn(checkPress,select):
    
    if select == 1:
        global start_btn
        button = start_btn
        buttonNhan = start_pressed_button
        buttonNha = start_button
    elif select == 2:
        global lv_btn
        button = lv_btn
        buttonNhan = lv_prs_button
        buttonNha = lv_button
    elif select ==3:
        global hd_btn
        button = hd_btn
        buttonNhan = hd_prs_button
        buttonNha = hd_button
    elif select ==4:
        global exit_btn
        button = exit_btn
        buttonNhan = exit_prs_button
        buttonNha = exit_button
        #=========================================
    elif select ==5:
        global tang_btn
        button = tang_btn
        buttonNhan = tang2_button
        buttonNha = tang1_button
    elif select == 6: 
        global giam_btn
        button = giam_btn
        buttonNhan = giam2_button
        buttonNha = giam1_button    

    if (checkPress == 1): # nhấn
                # print("start")
        soundBtn.play()
        button = buttonNhan
    else: 
                # print("nhả")
        button = buttonNha
    
    if select == 1: start_btn = button
    elif select ==2: lv_btn = button
    elif select == 3: hd_btn = button
    elif select == 4: exit_btn = button
    elif select == 5: tang_btn = button
    elif select == 6: giam_btn = button


def show_lv():
    global exit_show_lv_frame

    global pvcFrame
    global pvpFrame
    global mayTrcFrame
    global nguoiTrcFrame
    global tangFrame
    global giamFrame
    #=================================
    #1/2 window - 1/2 hinh = vitricenter his
    width = 4/5*WINDOW_WIDTH
    height = 4/5*WINDOW_HEIGHT
    xhis = WINDOW_WIDTH//2 - width //2
    yhis = WINDOW_HEIGHT//2 - height//2
        
    border_width = 4 // DPI
    rect_show_his = (xhis,yhis,width,height)
    pygame.draw.rect(screen,YELLOW_NHAT_F3EFCA,rect_show_his,border_radius = 15 // DPI ) #hcn 
    pygame.draw.rect(screen,BLACK,rect_show_his,width = border_width,border_radius = 15 // DPI ) #khung den
    
    exitLVFrame = get_frame_and_blit_img(exit_red_btn,xhis+width-3,yhis + 3, 3)
    exit_show_lv_frame = exitLVFrame
        
    render_text(screen, fontSelectSizeBoard, "Select Size Board", BLACK, xhis+30, yhis + 80+50)
    giam_frame = get_frame_and_blit_img(giam_btn, xhis + 350, yhis + 30 +50,1)
    tang_frame = get_frame_and_blit_img(tang_btn,xhis + 650, yhis + 30+50,1)
     
    x1 = 590
    y1 =y2 = 231 +50
    x2 = 792
    if sizeBoard < 20:
        x_so = (x1+x2)/2 - 70 #x số
        y_so = y1 - 160
    elif sizeBoard >= 20:
        x_so = (x1+x2)/2 - 90 #x số
        y_so = y1 - 160
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 5)
    text_num = str(sizeBoard)
    render_text(screen, fontThuong, text_num, BLACK,x_so,y_so)
        
        
    giamFrame = giam_frame
    tangFrame = tang_frame

    checkPVC(check_pvc)
        
        
    pvc_btn_frame = get_frame_and_blit_img(pvc_btn, xhis + 22//DPI, yhis+620//DPI , 1)
    pvp_btn_frame = get_frame_and_blit_img(pvp_btn, xhis + 1016//DPI, yhis+620//DPI ,1)
        
    if check_pvc == True: 
        checkAI_move_first(check_move_first)
        mayTrc_frame = get_frame_and_blit_img(mayDanhTrc_btn,xhis + 22//DPI, yhis+850//DPI ,1)
        nguoiTrc_frame = get_frame_and_blit_img(nguoiDanhTrc_btn, xhis + 1016//DPI, yhis+ 850//DPI ,1 )
        mayTrcFrame = mayTrc_frame
        nguoiTrcFrame = nguoiTrc_frame
    pvcFrame = pvc_btn_frame
    pvpFrame = pvp_btn_frame
        
def show_hd():
    global exitHDFrame
    width = 4/5*WINDOW_WIDTH
    height = 4/5*WINDOW_HEIGHT
    xhis = WINDOW_WIDTH//2 - width //2
    yhis = WINDOW_HEIGHT//2 - height//2
        
    border_width = 4 // DPI
    rect_show_his = (xhis,yhis,width,height)
    pygame.draw.rect(screen,YELLOW_NHAT_F3EFCA,rect_show_his,border_radius = 15 // DPI ) #hcn 
    pygame.draw.rect(screen,BLACK,rect_show_his,width = border_width,border_radius = 15 // DPI ) #khung den
    exit_hd_frame = get_frame_and_blit_img(exit_red_btn,xhis+width-3,yhis + 3, 3)
    exitHDFrame = exit_hd_frame

    nd_frame = get_frame_and_blit_img(content_hd, xhis+width//2, yhis+height//2,2)
    

def draw_menu():
    screen.blit(menu_background, (0,0))
    screen.blit(start_btn, start_button_frame)
    screen.blit(lv_btn, lv_btn_frame)
    screen.blit(hd_btn, hd_btn_frame)
    screen.blit(exit_btn, exit_btn_frame)
    if checkShowLV == True: 
        show_lv()

    if checkShowHD == True:
        show_hd()

def exitGame():
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()

def event():
    global checkShowLV , checkShowHD
    global check_pvc, check_move_first
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exitGame()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if checkShowLV == False and checkShowHD == False and start_button_frame.collidepoint(e.pos):
                    # nhấn = 1, nhả = 0
                    click_btn(1,1)
                   
                    from game import runPlayGame
                    runPlayGame(check_pvc,check_move_first)
                elif checkShowLV == False and checkShowHD == False and lv_btn_frame.collidepoint(e.pos):
                    click_btn(1,2)
                    click_btn(0,2)
                    checkShowLV = True 
            #================================
                elif checkShowLV == True and checkShowHD == False and exit_show_lv_frame.collidepoint(e.pos):
                    soundBtn.play()
                    checkShowLV = False
                elif checkShowLV == True and checkShowHD == False and pvcFrame.collidepoint(e.pos):
                    soundBtn.play()
                    check_pvc = True
                elif checkShowLV == True and checkShowHD == False and pvpFrame.collidepoint(e.pos):
                    soundBtn.play()
                    check_pvc = False
                elif checkShowLV == True and checkShowHD == False and mayTrcFrame and mayTrcFrame.collidepoint(e.pos):
                    soundBtn.play()
                    check_move_first = 1
                elif checkShowLV == True and checkShowHD == False and nguoiTrcFrame and nguoiTrcFrame.collidepoint(e.pos):
                    soundBtn.play()
                    check_move_first = 2
                elif checkShowLV == True and checkShowHD == False and tangFrame.collidepoint(e.pos):
                    click_btn(1,5)
                    tangSize()
                elif checkShowLV == True and checkShowHD == False and giamFrame.collidepoint(e.pos):
                    click_btn(1,6)
                    giamSize()
            #================================    
                elif checkShowLV == False and checkShowHD == False and hd_btn_frame.collidepoint(e.pos):
                    click_btn(1,3)
                    click_btn(0,3)
                    checkShowHD = True
                elif checkShowLV == False and checkShowHD == True and exitHDFrame.collidepoint(e.pos):
                    soundBtn.play()
                    checkShowHD = False
            #================================
                elif checkShowLV == False and checkShowHD == False and exit_btn_frame.collidepoint(e.pos):
                    click_btn(1,4)
                    exitGame()

            if e.type == pygame.MOUSEBUTTONUP:
                if  checkShowLV == False and checkShowHD == False and start_button_frame.collidepoint(e.pos):
                    click_btn( 0,1)
                # elif checkShowLV == False and lv_btn_frame.collidepoint(e.pos):
                #     click_btn(0,2)
                # elif checkShowLV == False and checkShowHD == False and hd_btn_frame.collidepoint(e.pos):
                #     click_btn(0,3)
                elif checkShowLV == False and checkShowHD == False and exit_btn_frame.collidepoint(e.pos):
                    click_btn(0,4)
                elif checkShowLV == True and checkShowHD == False and tangFrame.collidepoint(e.pos):
                    click_btn(0,5)
                elif checkShowLV == True and checkShowHD == False and giamFrame.collidepoint(e.pos):
                    click_btn(0,6)
                
        
def main_menu():
    global start_btn ,lv_btn
    start_btn = start_button
    lv_btn = lv_button
    global checkShowLV ,checkShowHD
    while True:
        event() 
        draw_menu()
        pygame.display.flip()

# main_menu()