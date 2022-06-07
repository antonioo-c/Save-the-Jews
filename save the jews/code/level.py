import pygame

from settings import *
from tile import Tile
from player import Player
from debug import debug, caption, pic
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from npcs import NPC
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from button import Button
import time
import sys

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.changable_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()
		self.magic_player = MagicPlayer(self.animation_player)

		#captions
		self.level1 = False
		self.level2 = False
		self.level3 = False
		self.pause = False
		self.status = 'level1'
		self.win = False
		self.finish = False

	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('../map/map_boundary.csv'),
			'grass': import_csv_layout('../map/map_Grass.csv'),
			'gate': import_csv_layout('../map/map_gate.csv'),
			'object': import_csv_layout('../map/map_objects.csv'),
			'entities': import_csv_layout('../map/map_entities.csv'),
			'citizens': import_csv_layout('../map/map_citizens.csv'),
			'prisoners': import_csv_layout('../map/map_prisoners.csv'),
		}
		graphics = {
			'grass': import_folder('../graphics/Grass'),
			'gate': import_folder('../graphics/gate'),
			'objects': import_folder('../graphics/objects'),
			'citizens': import_folder('../graphics/civilians/citizens'),
			'prisoners': import_folder('../graphics/civilians/prisoners')
		}

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')

						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'grass',
								random_grass_image)

						if style == 'gate':
							surf = graphics['gate'][int(col)-528]
							Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'grass',
								surf)

						if style == 'object':
							if int(col) <= 1:
								surf = graphics['objects'][int(col)]
								Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
							else:
								surf = graphics['objects'][int(col)]
								Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.changable_sprites], 'object', surf)

						if style == 'citizens':
							surf = graphics['citizens'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

						if style == 'prisoners':
							surf = graphics['prisoners'][int(col)-462]
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

						if style == 'entities':
							if col == '0':
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic)
							else:
								if col == '1': monster_name = 'bamboo'
								elif col == '2': monster_name = 'spirit'
								elif col == '3': monster_name = 'squid'
								elif col == '4': monster_name = 'raccoon'
								elif col == '6':
									NPC(
										'portal',
										(x, y),
										[self.visible_sprites]
									)
								if col in ['1', '2', '3', '4']:
									Enemy(
										monster_name,
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player,
										self.trigger_death_particles,
										self.add_exp)


	def create_attack(self):
		
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def create_magic(self,style,strength,cost):
		if style == 'heal':
			self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

		if style == 'flame':
			self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0,75)
							for leaf in range(randint(3,6)):
								self.animation_player.create_grass_particles(pos - offset,[self.visible_sprites])
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)

	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites], False)

	def trigger_death_particles(self,pos,particle_type):

		self.animation_player.create_particles(particle_type,pos,self.visible_sprites, False)

	def add_exp(self,amount):

		self.player.exp += amount

	def toggle_menu(self):

		self.game_paused = not self.game_paused

	def check_gameover(self):
		if self.player.health <= 0:
			self.status = 'dead'
			rect = self.display_surface.get_rect()
			caption('YOU ARE DEAD', (rect.centerx-400, rect.centery-50), (255, 0, 0), 150)
			time.sleep(1)
			pygame.quit()
			sys.exit()

	def check_gamewin(self):
		if not self.win:
			sprites = self.visible_sprites
			enemy_sprites = [sprite for sprite in sprites if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
			self.win = True
			for enemy in enemy_sprites:
				if enemy.monster_name == 'raccoon':
					self.win = False
			if self.win:
				self.win_effect()

	def win_effect(self):
		sprites = self.changable_sprites
		cnt = 1
		graphics = import_folder('../graphics/changed_objects')
		for ob in sprites:
			if cnt <= 3:
				self.animation_player.create_particles(f'pic{cnt}', ob.rect.center, [self.visible_sprites], False)
				ob.image = graphics[cnt-1]
			else:
				self.animation_player.create_particles(f'statue{cnt}', ob.rect.center, [self.visible_sprites], False)
				ob.image = graphics[cnt-1]
			cnt += 1

	def check_finish(self):
		if self.finish:
			pic('../graphics/scenes/ending.png')
			time.sleep(5)
			pygame.quit()
			sys.exit()

	def check_player_pos(self):
		player_x = self.player.rect.left
		player_y = self.player.rect.top
		rect = self.display_surface.get_rect()
		if not self.level1:
			if 110 <= player_x <= 1158:
				self.level1 = True
				self.status = 'level1'
				# pic('../托拉1.png')
				self.pause = True
				# 	self.level1 = True
				# caption('level1', (rect.centerx-400, rect.centery-50), (255, 0, 0), 150)
				# time.sleep(50)
		if not self.level2:
			if 1659 < player_x < 2310:
				self.level2 = True
				self.status = 'level2'
				# pic('../托拉2.png')
				self.pause = True
				# caption('level2', (rect.centerx - 400, rect.centery - 50), (255, 0, 0), 150)
				# time.sleep(30)
		if not self.level3 and self.level2:
			if 1868 <= player_y <= 2394:
				self.level3 = True
				self.status = 'level3'
				# pic('../托拉3.png')
				self.pause = True
				# caption('level3', (rect.centerx - 400, rect.centery - 50), (255, 0, 0), 150)
				# time.sleep(20)

	def function_continue(self):
		self.pause = False
		print('continue')

	def run(self):
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player)
		
		if self.game_paused:
			self.upgrade.display()
		else:
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.visible_sprites.npc_update(self)
			self.player_attack_logic()
		self.check_gameover()
		self.check_gamewin()
		self.check_finish()
		self.check_player_pos()

		

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)

	def npc_update(self, level):
		npc_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'npc_type') and sprite.npc_type == 'portal']
		for npc in npc_sprites:
			npc.npc_update(level)