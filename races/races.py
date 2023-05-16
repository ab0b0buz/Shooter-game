from pygame import *
from random import *
import math
font.init()
font = font.SysFont('freesansbold.ttf', 36)
mixer.init()


car100 = sprite.Group()
sprite2 = sprite.Group()

clock = time.Clock()
FPS = 60
clock.tick(FPS)

min_x = 1000
max_x = 1300


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


#создаём окно
win = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
display.set_caption('Гонки')
background = transform.scale(image.load('back.png'), (740, 600))
bg_width = background.get_width()



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

            self.rect.y -= 3

        if keys[K_DOWN] and self.rect.y <= 430:

            self.rect.y += 3



class Enemy(GameSprite):
    
    def update(self):

        if self.rect.x >= -96:

            self.rect.x -= 4
        
        else: 

            self.rect.x = randint(1000, 1100)
            
            self.rect.y = randint(100,150)
        
    def update1(self):

        if self.rect.x >= -96:

            self.rect.x -= 4
        
        else: 

            self.rect.x = randint(1200,1300)
            
            self.rect.y = randint(200,280)

    def update2(self):

        if self.rect.x >= -96:

            self.rect.x -= 4
        
        else: 

            self.rect.x = randint(1000,1400)
            
            self.rect.y = randint(320,415)

            



cars = Enemy(1, (95,70), randint(1000,1300),randint(100,150) , 2)
cars1 = Enemy(2, (95,70), randint(1000,1300),randint(200,280) , 2)
cars2 = Enemy(3, (95,70), randint(1000,1300),randint(320,415) , 2)
   


sprite1 = Player(4,(95,70),150 ,270,2)


sprite2.add(sprite1)

def main():
    global points
    scroll = 0
    points = 0
    death_count = 0
    
    run = True
    def score():
        global points
        points +=1

        text = font.render('Очки:'+ str(points),True,(255,255,255))
        textRect = text.get_rect()
        textRect.center = (900,50)
        win.blit(text, textRect)

    while run:


 
        sprite_collide = sprite.spritecollide(cars, sprite2, False)
        sprite_collide1 = sprite.spritecollide(cars1, sprite2, False)
        sprite_collide2 = sprite.spritecollide(cars2, sprite2, False)
    
   
        if sprite_collide:
            time.delay(2000)
            death_count += 1
            print('Ты проиграл')
            menu(death_count)
           
            #run = False

        if sprite_collide1:
            time.delay(2000)
            death_count += 1
            print('Ты проиграл')
            menu(death_count)
            
            #run = False

        if sprite_collide2:
            time.delay(2000)
            death_count += 1
            print('Ты проиграл')
            menu(death_count)

            #run = False
    
    

        for i in range(0, tiles):
            win.blit(background,(i * bg_width + scroll,0)) 
    
        scroll -= 3


        if abs(scroll) > bg_width:
            scroll = 0


        for e in event.get():
            if e.type == QUIT:
                run = False

        sprite2.draw(win)
        sprite2.update()

        #машины
        score()
        cars.reset()
        cars.update()
        cars1.reset()
        cars1.update1()
        cars2.reset()
        cars2.update2()
        

        display.update()

#main()
def menu(death_count):
    global points
    run = True
    while run:
        win.fill((255,255,255))

        if death_count == 0:
            text = font.render('Нажми на любую клавищу для запуска',True,(0,0,0))
            
        elif death_count > 0:
            text = font.render('Нажми на любую клавищу для перезапуска',True,(0,0,0))
            score = font.render('Твой счёт:'+ str(points),True,(0,0,0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH //2, SCREEN_HEIGHT // 2 + 50)
            win.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        win.blit(text, textRect)
   

        display.update()
        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                main()
                
        



menu(death_count=0)





