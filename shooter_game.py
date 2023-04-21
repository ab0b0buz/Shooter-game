#Создай собственный Шутер!
from pygame import *
from random import *

#Звуки
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')

#Отрисовка статистики
score = 0
scoreMiss = 0

font.init()
font = font.SysFont('Arial', 36)

monters = sprite.Group()  
bullets = sprite.Group()    

clock = time.Clock()
FPS = 60
clock.tick(FPS)
#создаём окно
win = display.set_mode((700,500))
display.set_caption('Шутер')
#даём картинку задниму фону
background = transform.scale(image.load('galaxy.jpg'), (700, 500))


#Базовый класс
class GameSprite(sprite.Sprite):
    #денаем супер класс
    def __init__(self, image_mode, size_image, player_x, player_y, player_speed):
        super().__init__()
        self.size_image = size_image
        #номирум каждую картинку
        if image_mode == 1:
            self.image = transform.scale(image.load('rocket.png'), self.size_image)
        if image_mode == 2:
            self.image = transform.scale(image.load('bullet.png'), self.size_image)
        if image_mode == 3:
            self.image = transform.scale(image.load('ufo.png'), self.size_image)
        if image_mode == 4:
            self.image = transform.scale(image.load('asteroid.png'), self.size_image)

        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
       #прописываем х,у окну
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

#Класс ракеты
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #прописываем движение ракеты
        if keys[K_LEFT] and self.rect.x >= 5:

            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x <= 600:

            self.rect.x += self.speed
            
        #выстрел
    def fire(self):
        bullet = Bullet(2, (15, 30), self.rect.centerx - 10, self.rect.top, 1)
        bullets.add(bullet)
        if self.rect.y <= -50.0:
            bullet.kill()
    
#Класс монстров
class Enemy(GameSprite):
    
    def update(self):
        global scoreMiss

        if self.rect.y <= 500.0:

            self.rect.y += 1
        else: 
            self.rect.x = randint(50, 650)

            self.rect.y = randint(-400, -200)

            scoreMiss += 1

#Класс пуль
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.y <= -50.0:
            self.kill()

sprite1 = Player(1, (70, 80), 300 ,420 ,2)
                                                #Создаём  группу монстров


for i in range(5):
    monster = Enemy(randint(3, 4), (80,60), randint(50, 600), randint(-400, -200), 1)
    monters.add(monster)
    
                            
                                                #Основной цикл
run = True
while run:
    
    fontRender1 = font.render(f'Счёт: {score}' , True, (255, 255, 255))
    fontRender2 = font.render(f'Пропущено: {scoreMiss} ' , True, (255, 255, 255))
    sprites_list = sprite.groupcollide(monters, bullets, True, True)
    sprite_collide = sprite.spritecollide(sprite1, monters, False)
    
    if sprite_collide:
        print('Ты програл')
        run = False 

    if sprites_list:
        monster = Enemy(randint(3, 4), (80,60), randint(50, 600), randint(-400, -200 ), 1)
        monters.add(monster)
        score += 1

    if score >= 10:
        print('Ты победил')
        run = False

    if scoreMiss >= 3:
        print('Ты проиграл')
        run = False    
      

    win.blit(background, (0, 0))
    win.blit(fontRender1, (20, 20))
    win.blit(fontRender2,(20, 50))

    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                                                     
                sprite1.fire()

    sprite1.reset()
    bullets.draw(win)
    monters.draw(win)
    
    bullets.update()
    sprite1.update()
    monters.update()

    display.update()