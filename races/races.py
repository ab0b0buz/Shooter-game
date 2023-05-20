#Мой проект
from pygame import *
from random import *
import math
#текст
font.init()
font = font.SysFont('Arial', 40)
#звуки
mixer.init()
mixer.music.load('backM.mp3')
mixer.music.play(-1)
hit = mixer.Sound('hit.wav')

sprite2 = sprite.Group()
#фпс
clock = time.Clock()
FPS = 60
clock.tick(FPS)
# даём имя координатам
c_y1 = 1000
c_y2 = 1300
c_x1 = 100
c_x2 = 150
c_x3 = 200
c_x4 = 280
c_x5 = 320
c_x6 = 416
sprite_x = 150
sprite_y = 270
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
# создаём окно и тд.
win = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
display.set_caption('Гонки')
background = transform.scale(image.load('back.png'), (740, 600))
minu = transform.scale(image.load('minu.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_width = background.get_width()
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
gameplay = True
#основной класс
class GameSprite(sprite.Sprite):
    def __init__(self, image_mode, size_image, player_x, player_y, player_speed):
        super().__init__()
        self.size_image = size_image
        #имменуем картинки
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
#класс игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #прописываем движение машины
        if keys[K_UP] and self.rect.y >= 100:
            self.rect.y -= 3

        if keys[K_DOWN] and self.rect.y <= 430:
            self.rect.y += 3
#класс машинок
class Enemy(GameSprite):
    
    def update(self):

        if self.rect.x >= -96:
            self.rect.x -= 4
        
        else: 

            self.rect.x = randint(c_y1, c_y2)
            self.rect.y = randint(c_x1,c_x2)
        
    def update1(self):

        if self.rect.x >= -96:
            self.rect.x -= 4
        
        else: 

            self.rect.x = randint(c_y1,c_y2)
            self.rect.y = randint(c_x3,c_x4)

    def update2(self):

        if self.rect.x >= -96:
            self.rect.x -= 4
        
        else: 

            self.rect.x = randint(c_y1,c_y2)
            self.rect.y = randint(c_x5,c_x6)
# машинки
cars = Enemy(1, (95,70), randint(c_y1,c_y2),randint(100,150) , 2)
cars1 = Enemy(2, (95,70), randint(c_y1,c_y2),randint(200,280) , 2)
cars2 = Enemy(3, (95,70), randint(c_y1,c_y2),randint(320,415) , 2)
# такси
sprite1 = Player(4,(95,70),sprite_x ,sprite_y,2)
sprite2.add(sprite1)
# основня функция
def main():
    global points , gameplay
    scroll = 0
    points = 0
    death_count = 0
    run = True
    # счёт
    def score():
        global points
        points +=1
        text = font.render('Очки:'+ str(points),True,(255,255,255))
        textRect = text.get_rect()
        textRect.center = (900,50)
        win.blit(text, textRect)
    # основ цикл
    while run:
        #движение заднего фона
        for i in range(0, tiles):
            win.blit(background,(i * bg_width + scroll,0)) 
        scroll -= 3
        if abs(scroll) > bg_width:
            scroll = 0
        if gameplay:
            # соприкосание машинок с такси
            sprite_collide = sprite.spritecollide(cars, sprite2, False)
            sprite_collide1 = sprite.spritecollide(cars1, sprite2, False)
            sprite_collide2 = sprite.spritecollide(cars2, sprite2, False)
            # действие после соприкосания машинок
            if sprite_collide:
                mixer.music.pause()
                hit.play()
                time.delay(1000)
                gameplay = False
            # действие после соприкосания машинок
            if sprite_collide1:
                mixer.music.pause()
                hit.play()
                time.delay(1000)
                gameplay = False
            # действие после соприкосания машинок
            if sprite_collide2:
                mixer.music.pause()
                hit.play()
                time.delay(1000)
                gameplay = False
            # обновление движения
            sprite2.draw(win)
            sprite2.update()
            score()
            cars.reset()
            cars.update()
            cars1.reset()
            cars1.update1()
            cars2.reset()
            cars2.update2()
            display.update()
        else:
            # надпись после проигроша
            win.blit(minu,(0,0)) 
            lose_label = font.render('Вы проиграли!',True,(242, 2, 2))
            win.blit(lose_label, (400,200))
        
            text = font.render('Ваши счёт:'+ str(points),True,(242, 2, 2))
            textRect = text.get_rect()
            textRect.center = (510,300)
            win.blit(text, textRect)
        # обновления дисплея
        display.update()

        for e in event.get():
            if e.type == QUIT:
                run = False
        
main()