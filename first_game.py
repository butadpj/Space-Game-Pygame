

import pygame
import random
import math as m
import time
pygame.init()

def main():

    transparent = (0,0,0,0)

# SCREEN DISPLAY SIZE, TITLE, AND OTHERS
    class Screen():
        screen = pygame.display.set_mode((800,600))
        reload_font = pygame.font.Font("freesansbold.ttf",50)
        reload_text = reload_font.render("Out of ammo", True, (255,255,255))

        def set_screen_caption(self):
            pygame.display.set_caption("My first Pygame")

        def display_reload_text(self, x,y):
            self.screen.blit(self.reload_text, (x,y))
    screen_init = Screen()
    screen_init.set_screen_caption

# CHARACTER VARIABLES
    class Character():
        def __init__(self):
            self.character_img = pygame.image.load("assets/xwing50.png")
            self.character_x = 375
            self.character_y = 500
            self.character_x_change = 0


    # TO DISPLAY THE CHARACTER

        def display_character(self,x,y):
            screen_init.screen.blit(self.character_img,(x,y))

    character_init = Character()
    character_init_properties = vars(character_init)

# BULLET VARIABLES
    bullet_count = 10

    class Bullet():
        def __init__(self):
            self.bullet_img = pygame.image.load("assets/bullet30.png")
            
            self.bullet_x = character_init.character_x + 10
            self.bullet_y = character_init.character_y + 10
            self.bullet_x_change = 0
            self.bullet_y_change = 0
            self.rockets_shot = []
            self.out_of_rockets = False
            self.number_of_rockets = 0



    # TO DISPLAY THE BULLET

        def display_bullet(self,x,y):
            screen_init.screen.blit(self.bullet_img, (x,y))

    bullet_init = Bullet()
    bullet_init_properties = vars(bullet_init)

# ENEMY VARIABLES (not done fix random)
    class Enemy():
        def __init__(self,img_path,x,y,x_change,y_change):
            self.enemy_img = pygame.image.load(img_path)
            self.enemy_x = x 
            self.enemy_x_change = x_change
            self.enemy_y = y
            self.enemy_y_change = y_change
            self.explosion_img = pygame.image.load("assets/explosion56.png")


    # TO DISPLAY THE ENEMY

        def display_enemy(self,x,y):
            screen_init.screen.blit(self.enemy_img,(x,y))

    # TO DISPLAY THE EXPLOSION

        def display_explosion(self,x,y):
            screen_init.screen.blit(self.explosion_img, (x,y))
            

    enemy_count = 5
    enemy_array = []
    x = random.randrange(20,300)

    for enemy in range(enemy_count):
        img_path = "assets/tiefighter55.png"
        x +=80
        
        y = 150
        x_change = 0
        y_change = 0
        enemy_array.append(Enemy(img_path,x,y,x_change,y_change))
    
# BACKGROUND SETTINGS

    def bg_settings():
        bg_color = (0,0,10)
        return bg_color

# COLLISION DETECTION
    def is_collided(enemy_x, enemy_y, bullet_x, bullet_y):
        distance = m.sqrt((m.pow(enemy_x - bullet_x,2)) + (m.pow(enemy_y - bullet_y, 2)))
       
        if distance < 55:
            return True
        else:
            return False

# TO MAKE SURE GAME IS QUITTABLE (while loop)
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
# KEYBINDS AND FUNCTIONS OF EACH 
            
            if event.type == pygame.KEYDOWN:

    # MOVEMENT KEYS

                if event.key == pygame.K_LEFT:
                    character_init.character_x_change = -2
                    bullet_init.bullet_x_change = -2

                if event.key == pygame.K_RIGHT:
                    character_init.character_x_change = 2
                    bullet_init.bullet_x_change = 2

    # OTHER FUNCTIONS KEYS

                if event.key == pygame.K_SPACE:
                        bullet_init.bullet_y_change = -5

            if event.type == pygame.KEYUP:

    # MOVEMENT STOPPER KEY FUNCTIONS
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_init.character_x_change = 0
                    bullet_init.bullet_x_change = 0
        
# OTHER SETTINGS

    # BACKGROUND COLOR DISPLAY 
        screen_init.screen.fill(bg_settings())

    # COLLISION FUNCTION CALLS
        for enemy in enemy_array:
            collision_detect = is_collided(enemy.enemy_x,enemy.enemy_y,bullet_init.bullet_x,bullet_init.bullet_y)

            if collision_detect == True:
                bullet_init.bullet_x = character_init.character_x + 10
                bullet_init.bullet_y = character_init.character_y + 10
                enemy.enemy_img.fill(transparent)
                
                enemy.display_explosion(enemy.enemy_x,enemy.enemy_y)
                
                enemy.enemy_y = -1000
                
    # VALUES THAT ARE UNDECLARABLE AT THE START 

        character_init.character_x += character_init.character_x_change
      
        bullet_init.bullet_x += bullet_init.bullet_x_change
        bullet_init.bullet_y += bullet_init.bullet_y_change

        if bullet_init.bullet_y == 0:
            bullet_init.bullet_x = character_init.character_x + 10
            bullet_init.bullet_y = character_init.character_y + 10

    # BULLET, SHIP, AND ENEMY DISPLAY CODE

        bullet_init.display_bullet(bullet_init.bullet_x,bullet_init.bullet_y)
        # bullet_init.display_bullet(bullet_init.bullet_x + 15,bullet_init.bullet_y + 10)
        # bullet_init.display_bullet(bullet_init.bullet_x - 13,bullet_init.bullet_y +10 )
        
        character_init.display_character(character_init.character_x,character_init.character_y)

        for enemy in enemy_array:
            enemy.display_enemy(enemy.enemy_x, 150)

    # CODE THAT UPDATES THE DISPLAY SCREEN
        pygame.display.update()


main()






# ideas
# when character x = certain number like when the player hovers over



# unused settings, just copy paste

    # K_UP and K_DOWN
                # if event.key == pygame.K_UP:
                #     character_init.character_y_change = -2              

                # if event.key == pygame.K_DOWN:
                #     character_init.character_y_change = 2


    # OUT OF AMMO FOR K_SPACE
                    # if len(bullet_init.bullets_shot) == 10:
                    #     bullet_init.out_of_ammo = True

                    # else:
                    #     bullet_init.number_of_bullets += 1
                    #     bullet_init.bullets_shot.append(bullet_init.number_of_bullets)

    # RELOADING FUNCTION FOR K_R
                # if event.key == pygame.K_r:
                    # if bullet_init.out_of_ammo == True:
                    #     bullet_init.bullets_shot = []

                    #     bullet_init.out_of_ammo = False
         
                    # print("Reloading...cover me!")

    # OUT OF AMMO TEXT
        # if bullet_init.out_of_ammo == True:
        #     screen_init.display_reload_text(225 , 300)