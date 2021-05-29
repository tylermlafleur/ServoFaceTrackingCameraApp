import pygame
import serial
import math

pygame.init()

width = 1024
height = 768
screen = pygame.display.set_mode([width, height])

servRange = 180

ser = serial.Serial('/dev/ttyACM0')
SERIALEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SERIALEVENT, 15)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == SERIALEVENT:
            data = "X{0:.0f}Y{1:.0f}"
            x, y = pygame.mouse.get_pos()
            data = data.format(servRange/width * x, servRange/height * y)
            print(data)
            ser.write(data.encode())
    
    screen.fill((122,122,122))
    pygame.draw.circle(screen, (255, 0 ,0), pygame.mouse.get_pos(), 20, 2)
    pygame.draw.circle(screen, (255, 0 ,0), pygame.mouse.get_pos(), 2)
    pygame.display.flip()
            

