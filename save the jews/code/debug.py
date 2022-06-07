import time

import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'Black')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)

def caption(text, pos = (100, 100), color = (0, 0, 255), size = 90):
	font1 = pygame.font.SysFont('chalkduster.ttf', size)
	img1 = font1.render(text, True, color)
	display_surface = pygame.display.get_surface()
	display_surface.blit(img1, pos)
	pygame.display.update()

def pic(path, pos=(200, 100), size=(1200, 700)):
	img = pygame.image.load(path).convert_alpha()
	img = pygame.transform.scale(img, size)
	display_surface = pygame.display.get_surface()
	rect = img.get_rect()
	rect.center = display_surface.get_rect().center
	display_surface.blit(img, rect)
	pygame.display.update()



