from menuGame import main_menu 
from constants import background_music
import pygame
LINK_IMAGE_ICON_APP = "image//icon_game.png"
img_icon = pygame.image.load(LINK_IMAGE_ICON_APP) 
pygame.display.set_icon(img_icon)


pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1, 0.0)  # Phát âm nhạc nền liên tục
if __name__ == "__main__":
    main_menu()
