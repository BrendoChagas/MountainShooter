#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy, Enemy3  # Importamos a classe Enemy3
from code.Player import Player

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                # Cria a lista de backgrounds para o Level 1
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                # Cria a lista de backgrounds para o Level 2
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':
                # Cria a lista de backgrounds para o Level 3
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                # Cria o jogador 1
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                # Cria o jogador 2
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                # Cria o Enemy1 em uma posição vertical aleatória
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                # Cria o Enemy2 em uma posição vertical aleatória
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3':
                # Cria o Enemy3 em uma posição vertical aleatória
                return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
