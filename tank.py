import pygame
import random

class Tank(pygame.sprite.Sprite):
    def __init__(self, game, n):
        super().__init__()
        self.screen = game.screen
        self.game = game
        self.n = n
        self.moving = False
        self.weapon = 1
        self.shot1 = 0
        self.shot2 = 0
        self.w1max = 20
        self.w2max = 10
        if n == 1:
            self.direction = random.randint(1,4)
        elif n == 2:
            self.direction = random.randint(5,8)
        self.check_image()
        self.rect = self.image.get_rect()
        self.reset()

    def check_image(self):
        if self.n == 1:
            if self.direction == 4:
                self.image = pygame.image.load(r"Tank Game\images\Tank1left.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
            if self.direction == 1:
                self.image = pygame.image.load(r"Tank Game\images\Tank1up.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
            if self.direction == 2:
                self.image = pygame.image.load(r"Tank Game\images\Tank1right.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
            if self.direction == 3:
                self.image = pygame.image.load(r"Tank Game\images\Tank1down.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
        elif self.n == 2:
            if self.direction == 8:
                self.image = pygame.image.load(r"Tank Game\images\Tank2left.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
            if self.direction == 5:
                self.image = pygame.image.load(r"Tank Game\images\Tank2up.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
            if self.direction == 6:
                self.image = pygame.image.load(r"Tank Game\images\Tank2right.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
            if self.direction == 7:
                self.image = pygame.image.load(r"Tank Game\images\Tank2down.bmp")
                self.image = pygame.transform.scale(self.image, (self.image.get_rect().width*2, self.image.get_rect().height*2))
                    
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.centery = random.randint(0, 800)
        if self.n == 1:
            self.rect.centerx = random.randint(int(self.game.screen_width/2), self.game.screen_width)
        elif self.n == 2:
            self.rect.centerx = random.randint(0, int(self.game.screen_width/2))
    
    def update(self):
        if self.moving:
            if self.direction == 1:
                self.rect.y -= 1
            elif self.direction == 2:
                self.rect.x += 1
            elif self.direction == 3:
                self.rect.y += 1
            elif self.direction == 4:
                self.rect.x -= 1
            if self.direction == 5:
                self.rect.y -= 1
            elif self.direction == 6:
                self.rect.x += 1
            elif self.direction == 7:
                self.rect.y += 1
            elif self.direction == 8:
                self.rect.x -= 1