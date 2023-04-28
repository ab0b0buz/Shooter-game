from pygame import *
import sys
sys.setrecursionlimit(10000)

mixer.init()




clock = time.Clock()
FPS = 60
clock.tick(FPS)
#создаём окно

#sprite1 = sprite.Group()


win = display.set_mode((852,480))
display.set_caption('Гонки')
background = transform.scale(image.load('psdf.jpg'), (852, 480))



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




class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #прописываем движение машины
        if keys[K_UP] and self.rect.y >= 5:

            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y <= 600:

            self.rect.y += self.speed


sprite1 = Player(('pngegg.png'),(150 ,100 ,2))

run = True
while run:
    win.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False

    sprite1.reset()
    sprite1.update()
    display.update()