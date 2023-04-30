from pygame import *
from random import *
import math



mixer.init()


car100 = sprite.Group()  

clock = time.Clock()
FPS = 60
clock.tick(FPS)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


#создаём окно
win = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
display.set_caption('Гонки')
background = transform.scale(image.load('back.png'), (740, 600))
bg_width = background.get_width()

scroll = 0

tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1


class GameSprite(sprite.Sprite):
    def __init__(self, image_mode, size_image, player_x, player_y, player_speed):
        super().__init__()
        self.size_image = size_image
        if image_mode == 1:
            self.image = transform.scale(image.load('car1.png'), self.size_image)


        if image_mode == 2:
            self.image = transform.scale(image.load('car2.png'), self.size_image)


        if image_mode == 3:
            self.image = transform.scale(image.load('car3.png'), self.size_image)

        if image_mode == 4:
            self.image = transform.scale(image.load('car4.png'), self.size_image)



        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #прописываем движение машины
        if keys[K_UP] and self.rect.y >= 100:

            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y <= 430:

            self.rect.y += self.speed


class Enemy(GameSprite):
    
    def update(self):

        if self.rect.x >= -96:

            self.rect.x -= 4
        else: 
            
            self.rect.x = randint(1000, 1100)
            
            self.rect.y = randint(100, 430)

            
            
            

            




for i in range(4):

    cars = Enemy(randint(1,3), (95,70), randint(1000,1100),randint(100,300) , 2)

    car100.add(cars)


sprite1 = Player(4,(95,70),150 ,270,2)





run = True
while run:

    #win.blit(background, (0, 0))

    for i in range(0, tiles):
        win.blit(background,(i * bg_width + scroll,0)) 
    
    scroll -= 3


    if abs(scroll) > bg_width:
        scroll = 0




    for e in event.get():
        if e.type == QUIT:
            run = False

    sprite1.reset()
    sprite1.update()

    car100.draw(win)
    car100.update()

    display.update()