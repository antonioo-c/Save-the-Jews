import pygame
from settings import *
from entity import Entity
from support import *
from debug import pic, caption
import time, sys

class NPC(Entity):
    def __init__(self, npc_type, pos, groups):

        super().__init__(groups)
        self.npc_type = npc_type
        self.status = 'idle'
        self.import_graphics(npc_type)
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.collide_cnt = 0
        # print('npc created!')

    def import_graphics(self, name):
        self.animations = {'none': [], 'appear': [], 'idle': [], 'gone': []}
        main_path = f'../graphics/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_status(self, level):
        if not level.win:
            self.status = 'none'
            return
        if level.win and self.status == 'none':
            self.status = 'appear'
            return
        if self.status == 'appear':
            self.status = 'idle'
            return
        if self.status == 'idle' and level.player.hitbox.colliderect(self.hitbox):
            self.status = 'gone'
            return
        if not level.player.hitbox.colliderect(self.hitbox):
            self.status = 'idle'
            self.collide_cnt = 0
            return
        if self.status == 'gone' and level.player.hitbox.colliderect(self.hitbox):
            self.collide_cnt += 1
            print(self.collide_cnt)
            if self.collide_cnt >= 100:
                level.finish = True
            return

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'appear':
                self.status = 'idle'
            if self.status == 'gone':
                self.status = 'idle'
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

        self.rect = self.image.get_rect(center=self.hitbox.center)

        # alpha = self.wave_value()
        self.image.set_alpha(255)

    def update(self):
        self.animate()

    def npc_update(self, level):
        self.get_status(level)
        # print(self.status)

