import pygame

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.game = game
        self.font = pygame.font.SysFont("Arial", 20)
        self.p1_text()
        self.p2_text()

    def p1_text(self):
        p1s = f"Score: {self.game.t2score}"
        p1a1 = f"Weapon 1 ammo:{self.game.tank2.w1max-self.game.tank2.shot1}"
        p1a2 = f"Weapon 2 ammo:{self.game.tank2.w2max-self.game.tank2.shot2}"
        self.p1s_img = self.font.render(p1s, False, "black", "white")
        self.p1a1_img = self.font.render(p1a1, False, "black", "white")
        self.p1a2_img = self.font.render(p1a2, False, "black", "white")
        self.p1s_rect = self.p1s_img.get_rect()
        self.p1s_rect.topleft = self.game.screen_rect.topleft
        self.p1a1_rect = self.p1a1_img.get_rect()
        self.p1a1_rect.topleft = self.p1s_rect.bottomleft
        self.p1a2_rect = self.p1a2_img.get_rect()
        self.p1a2_rect.topleft = self.p1a1_rect.bottomleft
    
    def p2_text(self):
        p2s = f"Score: {self.game.t1score}"
        p2a1 = f"Weapon 1 ammo:{self.game.tank1.w1max-self.game.tank1.shot1}"
        p2a2 = f"Weapon 2 ammo:{self.game.tank1.w2max-self.game.tank1.shot2}"
        self.p2s_img = self.font.render(p2s, False, "black", "white")
        self.p2a1_img = self.font.render(p2a1, False, "black", "white")
        self.p2a2_img = self.font.render(p2a2, False, "black", "white")
        self.p2s_rect = self.p2s_img.get_rect()
        self.p2s_rect.topright = self.game.screen_rect.topright
        self.p2a1_rect = self.p2a1_img.get_rect()
        self.p2a1_rect.topright = self.p2s_rect.bottomright
        self.p2a2_rect = self.p2a2_img.get_rect()
        self.p2a2_rect.topright = self.p2a1_rect.bottomright

    def draw(self):
        self.screen.blit(self.p1s_img, self.p1s_rect)
        self.screen.blit(self.p1a1_img, self.p1a1_rect)
        self.screen.blit(self.p1a2_img, self.p1a2_rect)
        self.screen.blit(self.p2s_img, self.p2s_rect)
        self.screen.blit(self.p2a1_img, self.p2a1_rect)
        self.screen.blit(self.p2a2_img, self.p2a2_rect)