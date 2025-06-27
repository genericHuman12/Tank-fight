import pygame
import pygame.sprite

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, d, speed):
        super().__init__()
        self.screen = game.screen
        self.color = "black"
        self.direc(d, game)
        self.speed = speed
        
    def direc(self,d, game):
        if d == 1:
            self.rect = pygame.rect.Rect(0,0,5,15)
            self.d = 1
            self.rect.midbottom = game.tank1.rect.midtop
        if d == 2:
            self.rect = pygame.rect.Rect(0,0,15,5)
            self.d = 2
            self.rect.midleft = game.tank1.rect.midright
        if d == 3:
            self.rect = pygame.rect.Rect(0,0,5,15)
            self.d = 3
            self.rect.midtop = game.tank1.rect.midbottom
        if d == 4:
            self.rect = pygame.rect.Rect(0,0,15,5)
            self.d = 4
            self.rect.midright = game.tank1.rect.midleft
        if d == 5:
            self.rect = pygame.rect.Rect(0,0,5,15)
            self.d = 1
            self.rect.midbottom = game.tank2.rect.midtop
        if d == 6:
            self.rect = pygame.rect.Rect(0,0,15,5)
            self.d = 2
            self.rect.midleft = game.tank2.rect.midright
        if d == 7:
            self.rect = pygame.rect.Rect(0,0,5,15)
            self.d = 3
            self.rect.midtop = game.tank2.rect.midbottom
        if d == 8:
            self.rect = pygame.rect.Rect(0,0,15,5)
            self.d = 4
            self.rect.midright = game.tank2.rect.midleft
    
    def update(self):
        if self.d == 1:
            self.rect.y -= self.speed
        elif self.d == 2:
            self.rect.x += self.speed
        elif self.d == 3:
            self.rect.y += self.speed
        elif self.d == 4:
            self.rect.x -= self.speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)