from pygame import *


#Отрисовка статистики

clock = time.Clock()
FPS = 60
clock.tick(FPS)
#создаём окно
win = display.set_mode((700,600))
display.set_caption('Пин Понг')
#даём картинку задниму фону
color = (0, 255, 255)


class GameSprite(sprite.Sprite):
    def init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.pect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

 
#Класс ракеты
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #прописываем движение ракеты
        if keys[K_UP] and self.rect.y >= 5:

            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y <= 600:

            self.rect.y += self.speed
            
#sprite1 = Player('eCbWxL6.png', 100, 300, 2)
                            
                                                #Основной цикл
run = True
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False





    win.fill(color)
    #sprite1.reset()
    #sprite1.update()
    display.flip()
    
    
