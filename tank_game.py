import pygame
import sys
from tank import Tank
from bullet import Bullet
from scoreboard import Scoreboard

class Tank_Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.tank1= Tank(self, 1)
        self.tank2 = Tank(self, 2)
        self.bullets = pygame.sprite.Group()
        self.tanks1 = pygame.sprite.Group()
        self.tanks2 = pygame.sprite.Group()
        self.tanks1.add(self.tank1)
        self.tanks2.add(self.tank2)
        self.t1score = 0
        self.t2score = 0
        self.scoreboard = Scoreboard(self) 

    def run(self):
        while True:
            self.check_events()
            self.tank1.check_image()
            self.tank1.update()
            self.tank2.check_image()
            self.tank2.update()
            self.update_bullet()
            self.check_collide()
            self.scoreboard.p1_text()
            self.scoreboard.p2_text()
            self.update_screen()
                
    def update_bullet(self):
        for bullet in self.bullets:
            bullet.update()
    
    def update_screen(self):
        self.screen.fill("white")
        self.tank1.draw()
        self.tank2.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.scoreboard.draw()
        pygame.display.flip()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_downs(event)
            if event.type == pygame.KEYUP:
                self.check_ups(event)
    
    def reset(self):
        self.tank1.reset()
        self.tank2.reset()
        self.tank1.shot1, self.tank1.shot2 = 0,0
        self.tank2.shot2, self.tank2.shot1 = 0,0
        self.bullets.empty()
        self.tank1.direction = 4
        self.tank2.direction = 6
        self.tank1.moving = False
        self.tank2.moving = False
            
    def check_downs(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_i:
            self.tank1.direction = 1
            self.tank1.moving = True
        elif event.key == pygame.K_j:
            self.tank1.direction = 4
            self.tank1.moving = True
        elif event.key == pygame.K_k:
            self.tank1.direction = 3
            self.tank1.moving = True
        elif event.key == pygame.K_l:
            self.tank1.direction = 2
            self.tank1.moving = True
        elif event.key == pygame.K_m:
            if self.tank1.shot1 < self.tank1.w1max:
                bullet = Bullet(self, self.tank1.direction, 2)
                self.bullets.add(bullet)
                self.tank1.shot1 += 1
        elif event.key == pygame.K_n:
            if self.tank1.shot2 < self.tank1.w2max:
                    bullet = Bullet(self, self.tank1.direction, 5)
                    self.bullets.add(bullet)
                    self.tank1.shot2 += 1
        elif event.key == pygame.K_w:
            self.tank2.direction = 5
            self.tank2.moving = True
        elif event.key == pygame.K_d:
            self.tank2.direction = 6
            self.tank2.moving = True
        elif event.key == pygame.K_s:
            self.tank2.direction = 7
            self.tank2.moving = True
        elif event.key == pygame.K_a:
            self.tank2.direction = 8
            self.tank2.moving = True
        elif event.key == pygame.K_SPACE:
            if self.tank1.shot1 < self.tank2.w1max:
                bullet = Bullet(self, self.tank2.direction, 2)
                self.bullets.add(bullet)
                self.tank2.shot1 += 1
        elif event.key == pygame.K_LALT:
            if self.tank2.shot2 < self.tank2.w2max:
                    bullet = Bullet(self, self.tank2.direction, 5)
                    self.bullets.add(bullet)
                    self.tank2.shot2 += 1
    
    def check_ups(self, event):
        if event.key == pygame.K_i:
            if self.tank1.direction == 1:
                self.tank1.moving = False
        if event.key == pygame.K_j:
            if self.tank1.direction == 4:
                self.tank1.moving = False
        if event.key == pygame.K_k:
            if self.tank1.direction == 3:
                self.tank1.moving = False
        if event.key == pygame.K_l:
            if self.tank1.direction == 2:
                self.tank1.moving = False
        if event.key == pygame.K_w:
            if self.tank2.direction == 5:
                self.tank2.moving = False
        if event.key == pygame.K_a:
            if self.tank2.direction == 8:
                self.tank2.moving = False
        if event.key == pygame.K_s:
            if self.tank2.direction == 7:
                self.tank2.moving = False
        if event.key == pygame.K_d:
            if self.tank2.direction == 6:
                self.tank2.moving = False
    
    def check_collide(self):
        if self.tank1.rect.right >= self.screen_rect.right:
            self.tank1.moving = False
            self.tank1.rect.x -= 5
        elif self.tank1.rect.bottom >= self.screen_rect.bottom:
            self.tank1.moving = False
            self.tank1.rect.y -= 5
        elif self.tank1.rect.left <= self.screen_rect.left:
            self.tank1.moving = False
            self.tank1.rect.x += 5
        elif self.tank1.rect.top <= self.screen_rect.top:
            self.tank1.moving = False
            self.tank1.rect.y += 5
        if self.tank2.rect.right >= self.screen_rect.right:
            self.tank2.moving = False
            self.tank2.rect.x -= 5
        elif self.tank2.rect.bottom >= self.screen_rect.bottom:
            self.tank2.moving = False
            self.tank2.rect.y -= 5
        elif self.tank2.rect.left <= self.screen_rect.left:
            self.tank2.moving = False
            self.tank2.rect.x += 5
        elif self.tank2.rect.top <= self.screen_rect.top:
            self.tank2.moving = False
            self.tank2.rect.y += 5
        for bullet in (self.bullets):
            if bullet.rect.right <= self.screen_rect.left:
                self.bullets.remove(bullet)
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
            if bullet.rect.bottom <= self.screen_rect.top:
                self.bullets.remove(bullet)
            if bullet.rect.top >= self.screen_rect.bottom:
                self.bullets.remove(bullet)
        if self.tank1.rect.colliderect(self.tank2.rect):
            self.reset()
        collide = pygame.sprite.groupcollide(self.tanks1, self.bullets, False, True)
        collide2 = pygame.sprite.groupcollide(self.tanks2, self.bullets, False, True)
        if collide:
            self.t2score += 1
            self.reset()
        if collide2:
            self.t1score += 1
            self.reset()

tarnk = Tank_Game()
tarnk.run()
