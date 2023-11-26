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
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 370:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed

background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode ((win_width, win_height))
window.fill(background)

font.init()
font = font.SysFont('Arial', 40)
lose1 = font.render(
    'PLAYER 1 LOSE T-T', True, (255, 215, 0))
lose2 = font.render(
    'PLAYER 2 LOSE T-T', True, (255, 215, 0))

ball = GameSprite(280, 200, 2, "tennis_ball_0.png", 50 , 50)
paddle_l = Player(515, 170, 5, "racket_0.png", 50 , 120)
paddle_r = Player(25, 170, 5, "racket_0.png", 50 , 120)

clock = time.Clock()
FPS = 60
game = True
finish = False
speed_x = 3
speed_y = 3

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        paddle_l.update_l()
        paddle_r.update_r()
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(paddle_l, ball) or sprite.collide_rect(paddle_r, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (150,200))
        if ball.rect.x >  win_width-50:
            finish = True
            window.blit(lose2, (150,200))
        ball.reset()
        paddle_l.reset()
        paddle_r.reset()
    
    display.update()
    clock.tick(FPS)