import pygame, sys
from pygame.locals import *
import win32api 
import win32con
import win32gui
from pygame._sdl2.video import Window
import random



pygame.init()
screen = pygame.display.set_mode((55, 30), pygame.NOFRAME)

pygame.display.set_caption('Slime')
source = pygame.image.load("IdleFront.png").convert_alpha()

WHITE = (255,255,255)
BLACK = (0,0,0)
fuchsia = (255, 0, 128)

def get_image(source, width, height, color, x):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(source, (0,0), (x*64,0,width, height))
    image.set_colorkey(color)
    return image

frame_list = []
frame_amount = 12
for x in range(frame_amount):
    frame_list.append(get_image(source, 64,64, BLACK, x))

last_update = pygame.time.get_ticks()
animation_countdown = 100
frame = 0

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

while True: 
    screen.fill(fuchsia)
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_countdown:
        frame += 1
        if frame >= len(frame_list) :
            frame = 0
        last_update = current_time

    screen.blit(frame_list[frame], (-5,-18))
    window = Window.from_display_module()
    window.position = (current_time/50,300)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
