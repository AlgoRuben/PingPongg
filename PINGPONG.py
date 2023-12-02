from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect =  self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(slef):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_a] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


rocket_1 = Player('rocket_1.png', 25, 200, 25, 150, 5)
rocket_2 = Player('rocket_1.png', 550, 200, 25, 150, 5)
Ball = GameSprite('Ball.png', 200, 200, 50, 50, 5)

speed_x = 5
speed_y = 5

win_width = 600
win_height = 500
display.set_caption('П И Н Г - П О Н Г')
window = display.set_mode((win_width, win_height))
background = (55,155,100)
window.fill((background))

font.init()
font = font.Font(None, 36)
lose_1 = font.render('ЛЕВЫЙ ПРОИГРАЛ', True, (55,55,255))
lose_2 = font.render('ПРАВЫЙ ПРОИГРАЛ', True, (255,55,55))



game = True
finish = False
clock = time.Clock()
FPS = 90
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        rocket_1.update_l()
        rocket_2.update_r()
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y
        if sprite.collide_rect(rocket_1, Ball) or sprite.collide_rect(rocket_2, Ball):
            speed_x *= -1
            speed_y *= -1
        if Ball.rect.y > win_height-50 or Ball.rect.y < 0:
            speed_y *= -1
        if Ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (200, 200))
            game_over 
        if Ball.rect.x > win_width:
            finish = True
            window.blit(lose_2, (200, 200))
            game_over
        rocket_1.reset()
        rocket_2.reset()
        Ball.reset()  
    display.update()
    clock.tick(FPS)



