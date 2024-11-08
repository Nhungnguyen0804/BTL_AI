'''
carogame/
--- main.py
--- menu.py
--- game.py
--- constants.py
'''

from menuGame import main_menu 
from constants import background_music
import pygame
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1, 0.0)  # Phát âm nhạc nền liên tục
if __name__ == "__main__":
    main_menu()
