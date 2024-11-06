# Constant
DPI = 2 # 1.995 #điểm trên inch thực tế

#window
WINDOW_WIDTH = 1260 # 1200 
WINDOW_HEIGHT = 810 # 800 

# màu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
PINK = (255,105,180)
RED = (255,0,0)
GREEN = (0, 255, 0)
GREEN_DAM_5E7B6F = (94,123,111)
GREEN_NHAT_DDE5D0 = (221,229,208) 
GREEN_CCDDA7 = (204,221,167)
YELLOW_NHAT_F3EFCA = (243,239,202)

doi_thu = { 1:2, 2:1}

import pygame 
pygame.init()
pygame.mixer.init()

# Tải âm thanh
sound = pygame.mixer.Sound("audio//danh_co.mp3")  # Âm thanh hiệu ứng
soundBtn = pygame.mixer.Sound("audio//pick.mp3")
background_music = "audio//background_music.mp3"  # Âm nhạc nền

