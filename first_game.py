

import pygame
import random
import math as m
import time
from threading import Timer
pygame.init()

def bg_settings():
    bg_color = (0,0,10)
    return bg_color

def is_collided(enemy_x, enemy_y, bullet_x, bullet_y, target):
    distance = m.sqrt((m.pow(enemy_x - bullet_x,2)) + (m.pow(enemy_y - bullet_y, 2)))
    if distance <= target:
        return True
    else:
        return False

# PROGRAM ENTRY POINT
def main():
    RUNNING = True
    START_TIMER = pygame.time.get_ticks()

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
            self.has_bullet_powerups = False

        # TO DISPLAY THE CHARACTER
        def display_character(self,x,y):
            # From now on, we have to strictly convert 
            # x,y values to integers or floats using 
            # int() or round()
            screen_init.screen.blit(self.character_img, (round(x), round(y)))
    character_init = Character()
    character_init_properties = vars(character_init)

    # BULLET VARIABLES
    class Bullet():
        def __init__(self, x, y, x_change, y_change):
            # When we are dealing with 2 or more bullets,
            # we had to set the x,y and x_change,y_change values
            # dynamically so that we can implement collision detection
            # for each bullet 
            self.bullet_img = pygame.image.load("assets/bullet30.png")
            self.bullet_x = x
            self.bullet_y = y
            self.bullet_x_change = x_change
            self.bullet_y_change = y_change

            # self.rockets_shot = []
            # self.out_of_rockets = False
            # self.number_of_rockets = 0
                
        # TO DISPLAY THE BULLET
        def display_bullet(self,x,y):
            # From now on, we have to strictly convert 
            # x,y values to integers or floats using 
            # int() or round()
            screen_init.screen.blit(self.bullet_img, (round(x), round(y)))

        
        # bullet_init_properties = vars(bullet_init)
    bullet_init = Bullet(character_init.character_x + 19, character_init.character_y + 20, 0, 0)
    bullet_2 = Bullet(bullet_init.bullet_x + 15, bullet_init.bullet_y + 15, 0, 0)
    bullet_3 = Bullet(bullet_init.bullet_x + -13, bullet_init.bullet_y + 15, 0, 0)

    # ENEMY VARIABLES 
    class Enemy():
        def __init__(self,img_path,x,y,x_change,y_change):
            self.enemy_img = pygame.image.load(img_path)
            self.enemy_x = x 
            self.enemy_x_change = x_change
            self.enemy_y = y
            self.enemy_y_change = y_change
            self.explosion_img = pygame.image.load("assets/explosion56.png")
            self.is_exploded = False

        # TO DISPLAY THE ENEMY
        def display_enemy(self,x,y):
            screen_init.screen.blit(self.enemy_img, (round(x), round(y)))

        # TO DISPLAY THE EXPLOSION
        def display_explosion(self,x,y):
            screen_init.screen.blit(self.explosion_img, (round(x), round(y)))
    enemy_array = []
    max_enemy_count = 10000
    enemy_spawn_event = pygame.USEREVENT + 0
    enemy_spawn_time_interval = 1000

    def spawn_enemy_easy():
        img_path = "assets/tiefighter55.png"
        x =  random.randrange(50, 750)
        y = -10
        x_change = 0
        y_change = 0
        enemy_array.append(Enemy(img_path, x ,y,x_change,y_change))
    pygame.time.set_timer(enemy_spawn_event, enemy_spawn_time_interval) # Event for enemy spawning

    # POWERUP VARIABLES
    class PowerUp():
        def __init__(self):
            self.powerup_x = random.randrange(100,700)
            self.powerup_y = 510
            self.powerup_img = pygame.image.load("assets/gunpowerup50.png")
        def display_powerup(self,x,y):
            screen_init.screen.blit(self.powerup_img,(x,y))
    powerup_init = PowerUp()


    # TO MAKE SURE GAME IS QUITTABLE (while loop)
    while RUNNING == True:
        milliseconds = pygame.time.get_ticks() - START_TIMER
        seconds = milliseconds / 1000
        # print(seconds)
        

        # PYGAME EVENTS (Keyboard press, Exit, Custom Events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            
            if event.type == enemy_spawn_event:
                if max_enemy_count > 0:
                    spawn_enemy_easy()
                max_enemy_count -= 1
                     
            # WHEN CERTAIN KEY IS PRESSED
            if event.type == pygame.KEYDOWN:

                # MOVEMENT KEYS
                if event.key == pygame.K_LEFT:
                    character_init.character_x_change = -0.3
                    bullet_init.bullet_x_change = -0.3

                    if character_init.has_bullet_powerups:
                        bullet_2.bullet_x_change = -0.3
                        bullet_3.bullet_x_change = -0.3

                if event.key == pygame.K_RIGHT:
                    character_init.character_x_change = 0.3 
                    bullet_init.bullet_x_change = 0.3

                    if character_init.has_bullet_powerups:
                        bullet_2.bullet_x_change = 0.3
                        bullet_3.bullet_x_change = 0.3

                # OTHER FUNCTIONS KEYS
                if event.key == pygame.K_SPACE:
                    bullet_init.bullet_y_change = (-1)
            
            # WHEN CERTAIN KEY IS RELEASED
            if event.type == pygame.KEYUP:

                # MOVEMENT STOPPER KEY FUNCTIONS
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_init.character_x_change = 0
                    bullet_init.bullet_x_change = 0
                    if character_init.has_bullet_powerups:
                        bullet_2.bullet_x_change = 0
                        bullet_3.bullet_x_change = 0

        # BACKGROUND COLOR DISPLAY 
        screen_init.screen.fill(bg_settings())
     
        # CHARACTER MOVEMENT
        character_init.character_x += character_init.character_x_change

        # BULLETS MOVEMENT
        bullet_init.bullet_x += bullet_init.bullet_x_change
        bullet_init.bullet_y += bullet_init.bullet_y_change
        
        bullet_2.bullet_x += bullet_2.bullet_x_change
        bullet_2.bullet_y += bullet_2.bullet_y_change

        bullet_3.bullet_x += bullet_3.bullet_x_change
        bullet_3.bullet_y += bullet_3.bullet_y_change

        # EXTRA BULLETS WILL ALWAYS FOLLOW THE CHARACTER MOVEMENT
        bullet_2.bullet_x = bullet_init.bullet_x + 15
        bullet_3.bullet_x = bullet_init.bullet_x + -13

        bullet_2.bullet_y = bullet_init.bullet_y + 15
        bullet_3.bullet_y = bullet_init.bullet_y + 15

        # IF BULLETS HIT THE TOP OF THE SCREEN
        if bullet_init.bullet_y <= 0:
            bullet_init.bullet_x = character_init.character_x + 19
            bullet_init.bullet_y = character_init.character_y + 20
            
            bullet_2.bullet_x = bullet_init.bullet_x + 15
            bullet_2.bullet_y = bullet_init.bullet_y + 15
             
            bullet_3.bullet_x = bullet_init.bullet_x + -13
            bullet_3.bullet_y = bullet_init.bullet_y + 15
            
        # DISPLAY THE BULLET
        bullet_init.display_bullet(bullet_init.bullet_x,bullet_init.bullet_y)

        # DISPLAY THE CHARACTER
        character_init.display_character(character_init.character_x,character_init.character_y)

        # DISPLAY THE ENEMY
        for enemy in enemy_array:
           
            enemy.display_enemy(enemy.enemy_x, enemy.enemy_y)

            # ENEMY MOVEMENT
            enemy.enemy_y += enemy.enemy_y_change

            # LEVELS

            # level 1
            if seconds >= 3:
                enemy.enemy_y_change = 0.08

            # level 2
            if seconds >= 20:
                enemy.enemy_y_change = 0.15

            # level 3
            if seconds >= 40:
                enemy.enemy_y_change = 0.3

            # level 4
            if seconds >= 60:
                enemy.enemy_y_change = 0.5
        
            # IF ENEMY GOT HIT BY ONE OF THE BULLETS
            bullet_init_collided = is_collided(enemy.enemy_x,enemy.enemy_y,bullet_init.bullet_x,bullet_init.bullet_y, 30)
            bullet_2_collided = is_collided(enemy.enemy_x,enemy.enemy_y,bullet_2.bullet_x,bullet_2.bullet_y, 30)
            bullet_3_collided = is_collided(enemy.enemy_x,enemy.enemy_y,bullet_3.bullet_x,bullet_3.bullet_y, 30)

            if bullet_init_collided or bullet_2_collided or bullet_3_collided:
                # SHOW EXPLOTION
                enemy.display_explosion(enemy.enemy_x, enemy.enemy_y)

                # REMOVE THE ENEMY
                enemy_array.remove(enemy)

                # RESET THE BULLETS POSITION
                bullet_init.bullet_x = character_init.character_x + 19
                bullet_init.bullet_y = character_init.character_y + 20

                bullet_2.bullet_x = character_init.character_x + 19
                bullet_2.bullet_y = character_init.character_y + 20

                bullet_3.bullet_x = character_init.character_x + 19
                bullet_3.bullet_y = character_init.character_y + 20
                
        # DISPLAY THE POWERUPS
        if seconds >= 2:
            powerup_init.display_powerup(powerup_init.powerup_x,powerup_init.powerup_y)

            # IF THE CHARACTER GETS A POWERUP
            if is_collided(character_init.character_x,character_init.character_y,powerup_init.powerup_x,powerup_init.powerup_y, 50):
                character_init.has_bullet_powerups = True
                powerup_init.powerup_y = -1000             

        # IF THE CHARACTER HAS BULLET POWERUPS
        if character_init.has_bullet_powerups:
            bullet_2.bullet_y_change = bullet_init.bullet_y_change
            bullet_3.bullet_y_change = bullet_init.bullet_y_change

            bullet_2.display_bullet(bullet_2.bullet_x, bullet_2.bullet_y)
            bullet_3.display_bullet(bullet_3.bullet_x,bullet_3.bullet_y)
            
        # UPDATING THE DISPLAY SCREEN
        pygame.display.update()

main()

# master main

# ideas
# when character x = certain number like when the player hovers over

# note
# when seconds is greater than or equal to 5 then the boxes will appear 
# based on https://nerdparadise.com/programming/pygameblitopacity there will be a box which there is 
# so follow instructions and rename when necessary







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