import pygame
from game import Game
from player import Player
pygame.init()
icon = pygame.image.load('T.PNG')  # Replace with your image file path
pygame.display.set_icon(icon)





pygame.display.set_caption("The Destroyer")
screen = pygame.display.set_mode((1080,566))

game = Game()
running = True
background = pygame.image.load('w.PNG')

#charger notre player
player = Player(game)
while running:
    screen.blit(background, (0,0))
    screen.blit(game.player.image, game.player.rect)
    
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    for monster in game.all_monsters:
        monster.forward()
    game.player.all_projectiles.draw(screen)
    game.all_monsters.draw(screen)
    
    if game.pressed.get(pygame.K_RIGHT)  :
         game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) :
         game.player.move_left()     
    
    pygame.display.flip()
    
    for event in pygame.event.get() :
    
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key]  = True
            if event.key == pygame.K_SPACE :
                game.player.launch_projectile()
                
        
            
        elif event.type == pygame.KEYUP :
            game.pressed[event.key]  = False    