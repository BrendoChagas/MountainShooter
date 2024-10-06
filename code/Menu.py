#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        # Carrega a imagem de fundo do menu
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        # Carrega e reproduz a música do menu
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenha a imagem de fundo
            self.window.blit(source=self.surf, dest=self.rect)
            # Desenha o título do jogo
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            # Desenha as opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    # Destaca a opção selecionada em amarelo
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            # Adiciona o nome e RU no canto superior direito da tela
            self.menu_text(15, "Brendo Chagas - RU: 4522012", C_WHITE, (WIN_WIDTH - 10, 10), align='topright')

            pygame.display.flip()

            # Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Tecla Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, align='center'):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect()
        # Alinha o texto de acordo com o parâmetro 'align'
        if align == 'center':
            text_rect.center = text_pos
        elif align == 'topright':
            text_rect.topright = text_pos
        elif align == 'topleft':
            text_rect.topleft = text_pos
        elif align == 'bottomleft':
            text_rect.bottomleft = text_pos
        elif align == 'bottomright':
            text_rect.bottomright = text_pos
        self.window.blit(source=text_surf, dest=text_rect)
