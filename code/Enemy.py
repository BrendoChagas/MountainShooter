#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Configura o delay entre os tiros
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        # Movimento horizontal para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        # Controla o delay entre os tiros
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Cria um tiro inimigo
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Velocidade vertical inicial
        self.vertical_speed = ENTITY_SPEED[self.name] / 2
        # Direção inicial: -1 para cima, 1 para baixo
        self.direction = -1  # Começa subindo

    def move(self):
        # Movimento horizontal para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.direction == -1:  # Movendo para cima
            # Sobe com velocidade normal
            self.rect.centery -= self.vertical_speed
            if self.rect.top <= 0:
                # Ao bater na borda superior, muda direção para baixo
                self.direction = 1
        else:  # Movendo para baixo
            # Desce com o dobro da velocidade
            self.rect.centery += self.vertical_speed * 2
            if self.rect.bottom >= WIN_HEIGHT:
                # Ao bater na borda inferior, muda direção para cima
                self.direction = -1

    # O método shoot() é herdado da classe Enemy e não precisa ser modificado
