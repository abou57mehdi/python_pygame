import pygame
from  projectile import Projectile 


class Player(pygame.sprite.Sprite) :
    
    
    def __init__(self,game):
        super().__init__()  # Call initializer of Parent class
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('player.PNG')
        self.rect = self.image.get_rect()
        self.rect.x = 430
        self.rect.y = 370


    def launch_projectile(self) :
        
        self.all_projectiles.add(Projectile(self))
          
    def move_right(self):
        if not self.game.check_collision(self,self.game.all_monsters) :
            self.rect.x += self.velocity 
            
        
        
    def move_left(self):
        self.rect.x -= self.velocity    
