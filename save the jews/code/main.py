import time

import pygame, sys
from settings import *
from level import Level
from debug import debug, caption, pic
from button import Button
from album_player import album_player

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Save the jews!')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

		self.BG = pygame.image.load("../assets/Background.png")

	def get_font(self, size):  # Returns Press-Start-2P in the desired size
		return pygame.font.Font("../assets/font.ttf", size)

	def pause(self):
		loop = 1
		# write("PAUSED", 500, 150)
		# write("Press Space to continue", 500, 250)
		# caption()
		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					loop = 0
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						loop = 0
					if event.key == pygame.K_SPACE:
						self.screen.fill((0, 0, 0))
						loop = 0
			self.pause_image()
			pygame.display.update()
			# screen.fill((0, 0, 0))
			self.clock.tick(FPS)
		self.level.pause = False

	def pause_image(self):
		if self.level.status == 'level1':
			pic('../graphics/scenes/托拉1.png')
		elif self.level.status == 'level2':
			pic('../graphics/scenes/托拉2.png')
		elif self.level.status == 'level3':
			pic('../graphics/scenes/托拉3.png')
		elif self.level.status == 'win':
			pic('../graphics/scenes/ending.png')

	def run(self):
		while True:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()
				if self.level.pause:
					self.pause()
					#####
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
						album_player('../demo_album',self.screen)
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()

			self.screen.fill(WATER_COLOR)
			self.level.run()

			###
			MENU_MOUSE_POS = pygame.mouse.get_pos()
			option_image = pygame.image.load("../assets/Options Rect.png")
			option_image = pygame.transform.scale(option_image, (110, 30))
			OPTIONS_BUTTON = Button(image=option_image, pos=(60, 100),
									text_input="BOOK", font=self.get_font(15), base_color="#d7fcd4",
									hovering_color="White")
			exit_image = pygame.image.load("../assets/Quit Rect.png")
			exit_image = pygame.transform.scale(exit_image, (110, 30))
			QUIT_BUTTON = Button(image=exit_image, pos=(60, 150),
								 text_input="QUIT", font=self.get_font(15), base_color="#d7fcd4",
								 hovering_color="White")
			for button in [OPTIONS_BUTTON, QUIT_BUTTON]:
				button.changeColor(MENU_MOUSE_POS)
				button.update(self.screen)
			#####

			pygame.display.update()
			self.clock.tick(FPS)

	def options(self):
		while True:
			OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

			self.screen.fill("white")

			text = 'Be the Moses of our time!'
			OPTIONS_TEXT = self.get_font(40).render(text, True, "Black")
			OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 200))
			self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

			text = 'Produced by Anthony Chen, PKU'
			OPTIONS_TEXT = self.get_font(30).render(text, True, "Black")
			OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 400))
			self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

			OPTIONS_BACK = Button(image=None, pos=(640, 600),
								  text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

			OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
			OPTIONS_BACK.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
						return

			pygame.display.update()

	def main_menu(self):
		while True:
			self.screen.blit(self.BG, (0, 0))

			MENU_MOUSE_POS = pygame.mouse.get_pos()

			MENU_TEXT = self.get_font(80).render("Save the Jews!", True, "#b68f40")
			MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

			PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(640, 250),
								 text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Options Rect.png"), pos=(640, 400),
									text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4",
									hovering_color="White")
			QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550),
								 text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

			self.screen.blit(MENU_TEXT, MENU_RECT)

			for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
				button.changeColor(MENU_MOUSE_POS)
				button.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						self.run()
					if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
						self.options()
						# album_player('../demo_album', self.screen)
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()

			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.main_menu()