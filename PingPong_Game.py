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
    def update_l(self):
        keys = key.get_presses()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-5:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_presses()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-5:
            self.rect.y += self.speed

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