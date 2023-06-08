from pygame import *
from random import randint

font.init()
window_x = 700
window_y = 500
game = True
FPS = 60
finicsh = False
font2 = font.SysFont('Arial',36)
game_over_1 = font.SysFont('Arial',36)
clock = time.Clock()
counter = 0
e = 1
speed_car = 10
YELLOW = (255, 255, 0)
BLUE = (80, 80, 255)



window = display.set_mode((window_x, window_y))
display.set_caption('гонки')
background = transform.scale(image.load('фон.png'), (window_x,window_y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def colliderect(self, reck):
        return self.rect.colliderect(rect)

class Birdie(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_y-50:
            self.rect.y +=self.speed

class Car_enemy(GameSprite):
    def management_car(self):
        if self.rect.x > -70:
            self.rect.x -= self.speed
        else:
            self.rect.x = randint(670, 1300)
            self.rect.y = randint(0, 450)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    
    def color(self,new_color):
        self.fill_color = new_color

    def fill(self):
        draw.rect(background, self.fill_color, self.rect)

    def outline(self, frame_color, thickess):
        draw.rect(background, frame_color, self.rect, thickess)
    
    def collidepoint_1(self, x, y):
        return self.rect.collidepoint_1(x, y)


class Label(Area):
    def set_text(self, text, fsize, text_color=(0,0,0)):
        self.image = font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x =0, shift_y = 0):
        self.fill()
        background.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

card = Label(100, 170, 488, 100, YELLOW)
birdie = Birdie('птичка.png', 200, 200, 60, 50, 14)
car = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car) 
car_2 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car)   
car_3 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car)   
car_4 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car)  

car_5 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car) 
car_6 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car) 
car_7 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car) 
car_8 = Car_enemy('птичка_2 (1).png',randint(670, 1300), randint(0,450), 60, 50, speed_car) 
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
         #   x, y = event.pos

    window.blit(background,(0,0))

    keys = key.get_pressed()

    if (
        birdie.rect.colliderect(car) or birdie.rect.colliderect(car_2) or 
    birdie.rect.colliderect(car_3) or birdie.rect.colliderect(car_4)
    ):
        car.rect.x = randint(670, 1300)
        car_2.rect.x = randint(670, 1300)
        car_3.rect.x = randint(670, 1300)
        car_4.rect.x = randint(670, 1300)
        counter = 0
        finicsh = False
    killed_counter  =  font2.render("Счёт: "+ str(counter), 1, (0,25,0))
    window.blit(killed_counter, (10,20))
    if finicsh != True:
        card.outline(BLUE, 5)
        card.set_text('Для новой игры нажмите на кнопку', 26)
        card.reset()
        #if card.collidepoint_1(x, y):
        
        if keys[K_SPACE]:
            finicsh = True

    else:
        birdie.update()
        car.management_car()
        car_2.management_car()
        car_3.management_car()
        car_4.management_car()
        birdie.reset()
        car.reset()
        car_2.reset()
        car_3.reset()
        car_4.reset()

    if car.rect.x <= -69 or car_2.rect.x <= -69 or car_3.rect.x <= -69 or car_4.rect.x <= -69:
        counter += 1


        
    display.update()
    clock.tick(FPS)
