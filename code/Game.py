#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        # Cria a janela do jogo
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Pontuação do Player1, Pontuação do Player2]

                # Level 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:
                    # Level 2
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return:
                        # Level 3
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)

                        if level_return:
                            # Salva o score após completar todos os níveis
                            score.save(menu_return, player_score)
                        else:
                            # Game Over no Level 3
                            pass
                    else:
                        # Game Over no Level 2
                        pass
                else:
                    # Game Over no Level 1
                    pass

            elif menu_return == MENU_OPTION[3]:
                # Exibe a tela de scores
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Fecha a janela
                quit()  # Encerra o pygame
            else:
                pygame.quit()
                sys.exit()
