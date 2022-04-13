import cv2
import pygame
from pygame.locals import *
import time

lib = 'Map1.png'
lib2 = 'Map2.png'
lib3 = ()
coordenatesx = ()
coordenatesy = ()

Read = list(cv2.imread(lib).astype("int"))
Read2 = list(cv2.imread(lib2).astype("int"))

counter = 0

pygame.init()

flags = DOUBLEBUF
screen = pygame.display.set_mode((500,500), flags, 4)

start = time.process_time()
for y in range(len(Read)):#y coords
    for x in range(len(Read[y])):#x coords
        all = list(Read[y][x])[0]
        all2 = list(Read2[y][x])[0]
        difference = (all)-(all2)
        if difference > 10 or difference < -10:
            counter+=1
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 1, 1))

pygame.display.update()
print(time. process_time() - start)

if counter >= (y * x) * 0.75:
    print('They are similar images')
    print('They are different by only :', str((counter / (y * x)) * 100), '%')
else:
    print('They are different')
    print('They are different by:', str((counter / (y * x)) * 100), '%')

pygame.display.update()
