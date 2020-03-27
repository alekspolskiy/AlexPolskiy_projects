import time
import pygame
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

pygame.init()

screen = pygame.display.set_mode((850,150))
pygame.display.set_caption('WARNING!!!')
font = pygame.font.SysFont('Lucida Console', 20)
label = font.render("HELO, I'M A VIRUS", 1, (12,140,0,1))

while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
			time.sleep(0.10)
			screen = pygame.display.set_mode((850,150))
			pygame.display.set_caption('WARNING!!!')
			messagebox.showerror('LOOOOOOOOL', 'REMOVING DATA FROM THIS COMPUTER')

	screen.fill((0,0,0))
	screen.blit(label,(50,50))
	pygame.display.update()