import functools

import pygame
import sys
from button import Button
import tkinter
from tkinter import filedialog
import glob
import os
import os.path

WIDTH, HEIGHT = 1280, 900
BASE_TEXT_COLOR = "#6fffe9"
BACKGROUND_IMAGE = pygame.image.load("../assets/background.png")
WINDOW_ICON = pygame.image.load("../assets/window_icon.png")
MAIN_MENU_BUTTON_BACKGROUND = pygame.image.load("../assets/main_menu_button_bg.png")
REWIND_ICON_SURFACE = pygame.image.load("../assets/rewind_icon.png")
PAUSE_ICON_SURFACE = pygame.image.load("../assets/pause_icon.png")
PLAY_ICON_SURFACE = pygame.image.load("../assets/play_icon.png")
SEEK_ICON_SURFACE = pygame.image.load("../assets/seek_icon.png")
# LOAD_NEW_ALBUM_SURFACE = pygame.image.load("../assets/load_new_album_icon.png")


def bold_font(size):
    os.chdir(sys.path[0])
    return pygame.font.Font("../assets/calibri-bold.ttf", size)

def regular_font(size):
    return pygame.font.SysFont("calibri", size)

def rewind_button(current_image_index):
    if current_image_index > 0:
        current_image_index -= 1
    rewind_button_pressed = True
    return rewind_button_pressed, current_image_index

def seek_button(current_image_index, image_names):
    if current_image_index+1 < len(image_names):
        current_image_index += 1
    seek_button_pressed = True
    return seek_button_pressed, current_image_index

def play_button():
    paused = False
    unpaused = True
    return paused, unpaused

def pause_button():
    paused = True
    unpaused = False
    return paused, unpaused

def quit_button():
    pygame.quit()
    sys.exit()

def file_cmp(file1, file2):
    id1 = int(file1.split('.')[0])
    id2 = int(file2.split('.')[0])
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def album_player(folder_path, SCREEN):

    WIDTH, HEIGHT = 1280, 720
    BASE_TEXT_COLOR = "#6fffe9"
    BACKGROUND_IMAGE = pygame.image.load("../assets/background.png")
    WINDOW_ICON = pygame.image.load("../assets/window_icon.png")
    MAIN_MENU_BUTTON_BACKGROUND = pygame.image.load("../assets/main_menu_button_bg.png")
    REWIND_ICON_SURFACE = pygame.image.load("../assets/rewind_icon.png")
    PAUSE_ICON_SURFACE = pygame.image.load("../assets/pause_icon.png")
    PLAY_ICON_SURFACE = pygame.image.load("../assets/play_icon.png")
    SEEK_ICON_SURFACE = pygame.image.load("../assets/seek_icon.png")
    exit_image = pygame.image.load("../assets/Quit Rect.png")
    exit_image = pygame.transform.scale(exit_image, (110, 30))

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    image_file_paths = []
    image_names = []
    current_image_index = 0
    paused = False
    unpaused = False
    seek_button_pressed = False
    rewind_button_pressed = False

    os.chdir(folder_path)
    files = sorted(glob.glob('*'), key=functools.cmp_to_key(file_cmp))
    print(files)
    for file in files:
        current_image_path = f"{folder_path}/{file}"
        image_file_paths.append(current_image_path)
        name = file.split('.')[1]
        image_names.append(name)

    REWIND_BUTTON = Button(
        image=REWIND_ICON_SURFACE, pos=(WIDTH / 2 - 100, HEIGHT - 50), text_input="",
        font=bold_font(50), base_color=BASE_TEXT_COLOR, hovering_color="white"
    )
    PAUSE_BUTTON = Button(
        image=PAUSE_ICON_SURFACE, pos=(WIDTH / 2, HEIGHT - 50), text_input="",
        font=bold_font(50), base_color=BASE_TEXT_COLOR, hovering_color="white"
    )
    PLAY_BUTTON = Button(
        image=PLAY_ICON_SURFACE, pos=(WIDTH / 2, HEIGHT - 50), text_input="",
        font=bold_font(50), base_color=BASE_TEXT_COLOR, hovering_color="white"
    )
    SEEK_BUTTON = Button(
        image=SEEK_ICON_SURFACE, pos=(WIDTH / 2 + 100, HEIGHT - 50), text_input="",
        font=bold_font(50), base_color=BASE_TEXT_COLOR, hovering_color="white"
    )
    QUIT_BUTTON = Button(
        image=exit_image, pos=(WIDTH - 100, HEIGHT - 50), text_input="Back",
        font=bold_font(50), base_color=BASE_TEXT_COLOR, hovering_color="white"
    )

    previous_time = pygame.time.get_ticks()
    COOLDOWN = 5000

    photo_title_text_surface = bold_font(60).render(image_names[current_image_index], True, BASE_TEXT_COLOR)
    photo_title_text_rect = photo_title_text_surface.get_rect(center=(WIDTH / 2, 50))

    image_count_text_surface = regular_font(50).render(f"IMG {current_image_index + 1}/{len(image_names)}", True,
                                                       BASE_TEXT_COLOR)
    image_count_text_rect = image_count_text_surface.get_rect(center=(100, HEIGHT-50))

    new_image_surface = pygame.image.load(image_file_paths[current_image_index])
    if new_image_surface.get_height() > 500:
        new_image_surface = pygame.transform.scale(new_image_surface, (
        new_image_surface.get_width() * (500 / new_image_surface.get_height()), 500))
    elif new_image_surface.get_width() > 800:
        new_image_surface = pygame.transform.scale(new_image_surface, (
        800, new_image_surface.get_height() * (800 / new_image_surface.get_width())))
    new_image_rect = new_image_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    SCREEN.blit(new_image_surface, new_image_rect)
    SCREEN.blit(photo_title_text_surface, photo_title_text_rect)
    SCREEN.blit(image_count_text_surface, image_count_text_rect)

    REWIND_BUTTON.update(SCREEN)
    PAUSE_BUTTON.update(SCREEN)
    SEEK_BUTTON.update(SCREEN)
    QUIT_BUTTON.update(SCREEN)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_mouse_pos = pygame.mouse.get_pos()
                if REWIND_BUTTON.checkForInput(current_mouse_pos):
                    rewind_button_pressed, current_image_index = rewind_button(current_image_index)
                if SEEK_BUTTON.checkForInput(current_mouse_pos):
                    seek_button_pressed, current_image_index = seek_button(current_image_index, image_names)
                if paused:
                    if PLAY_BUTTON.checkForInput(current_mouse_pos):
                        paused, unpaused = play_button()
                else:
                    if PAUSE_BUTTON.checkForInput(current_mouse_pos):
                        paused, unpaused = pause_button()
                if QUIT_BUTTON.checkForInput(current_mouse_pos):
                    return

        current_time = pygame.time.get_ticks()

        if current_time - previous_time >= COOLDOWN or rewind_button_pressed or seek_button_pressed or paused or unpaused:
            unpaused = False
            if current_image_index < len(
                    image_file_paths) - 1 and not seek_button_pressed and not rewind_button_pressed and not paused:
                current_image_index += 1

            SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
            REWIND_BUTTON.update(SCREEN)
            if paused:
                PLAY_BUTTON.update(SCREEN)
            else:
                PAUSE_BUTTON.update(SCREEN)
            SEEK_BUTTON.update(SCREEN)
            QUIT_BUTTON.update(SCREEN)

            new_image_surface = pygame.image.load(image_file_paths[current_image_index])
            if new_image_surface.get_height() > 500:
                new_image_surface = pygame.transform.scale(new_image_surface, (
                new_image_surface.get_width() * (500 / new_image_surface.get_height()), 500))
            elif new_image_surface.get_width() > 800:
                new_image_surface = pygame.transform.scale(new_image_surface, (
                800, new_image_surface.get_height() * (800 / new_image_surface.get_width())))
            new_image_rect = new_image_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

            SCREEN.blit(new_image_surface, new_image_rect)

            photo_title_text_surface = bold_font(60).render(image_names[current_image_index], True, BASE_TEXT_COLOR)
            photo_title_text_rect = photo_title_text_surface.get_rect(center=(WIDTH / 2, 50))

            SCREEN.blit(photo_title_text_surface, photo_title_text_rect)

            image_count_text_surface = regular_font(50).render(f"IMG {current_image_index + 1}/{len(image_names)}",
                                                               True, BASE_TEXT_COLOR)
            image_count_text_rect = image_count_text_surface.get_rect(center=(100, HEIGHT-50))

            SCREEN.blit(image_count_text_surface, image_count_text_rect)

            pygame.display.update()
            previous_time = pygame.time.get_ticks()
            seek_button_pressed = False
            rewind_button_pressed = False