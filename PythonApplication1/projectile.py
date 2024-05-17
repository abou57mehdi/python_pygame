import pygame

class Projectile(pygame.sprite.Sprite) :
    def __init__(self, player) :
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("fiy.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 100
    def remove (self):
        self.player.all_projectiles.remove(self)
                    
        
    def move(self) :
        
        self.rect.x += self.velocity
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            
        if self.rect.x > 1080 :
            
            self.remove()
            
        

