import pygame 


class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        super().__init__()
        self.health= 100
        self.max_health= 100
        self.attack = 5 
        self.image=pygame.image.load("mummy.png") 
        self.rect= self.image.get_rect()
        self.rect.x= 990
        self.rect.y= 410
        self.velocity= 5
        

    def forward(self) :
        if not self.game.check_collision(self,self.game.all_players) :
            self.rect.x -= self.velocity 
            
        
     