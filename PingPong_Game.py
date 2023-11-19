from pygame import *

#CLass definition
class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, speed, img, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 20:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    def shoot(self):
        global num_fire
        bullet = Bullet(self.rect.centerx, self.rect.top , -10 , "bullet.png", 20, 15)
        num_fire += 1
        bullets.add(bullet)

background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode ((win_width, win_height))
window.fill(background)

clock = time.Clock()
FPS = 60
game = True

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)