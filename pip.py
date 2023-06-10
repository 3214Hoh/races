from pygame import *
from random import randint

font.init()
window_x = 700
window_y = 500
game = True
FPS = 60
finicsh = False
font2 = font.SysFont('Arial',36)
font3 = font.SysFont('Arial',36)
clock = time.Clock()
counter = 0
e = 0
speed_car = 8
YELLOW = (255, 255, 0)
BLUE = (80, 80, 255)
card_deleted = False
GREE = (0, 255, 0)
rer = False
best_account = 0


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
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize, text_color=(0,0,0)):
        self.image = font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x =0, shift_y = 0):
        self.fill()
        background.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

card = Label(100, 170, 488, 100, YELLOW)
card_level_ezze = Label(0, 440, 150, 60, YELLOW)
card_level_normal = Label(150, 440, 150, 60, YELLOW)
card_level_hard = Label(300, 440, 150, 60, YELLOW)
birdie = Birdie('главаная_машина.png', 200, 200, 60, 50, 14)

car = Car_enemy('белая_машина.png',randint(670, 1300), randint(0,450), 70, 60, speed_car) 
car_2 = Car_enemy('белая_синия_машина.png',randint(670, 1300), randint(0,450), 40, 30, speed_car)   
car_3 = Car_enemy('красная_машина.png',randint(670, 1300), randint(0,450), 80,60, speed_car)   
car_4 = Car_enemy('зелёная_машина.png',randint(670, 1300), randint(0,450), 70, 50, speed_car)  
car_5 = Car_enemy('красно_белая_машина.png',randint(670, 1300), randint(0,450), 60, 50, speed_car) 
car_6 = Car_enemy('желто_черная_машина.png',randint(670, 1300), randint(0,450), 60, 50, speed_car)

car_7 = Car_enemy('синия_белая_машина.png',randint(670, 1300), randint(0,450), 70, 60, speed_car) 
car_8 = Car_enemy('чёрная_машина .png',randint(670, 1300), randint(0,450), 40, 30, speed_car) 

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            x, y = i.pos

            if card.collidepoint(x, y):
                finicsh = True
                background = transform.scale(image.load('фон.png'), (window_x,window_y))

            if card_level_ezze.collidepoint(x, y):
                card_level_ezze = Label(0, 440, 150, 60, GREE)
                card_level_normal = Label(150, 440, 150, 60, YELLOW)
                card_level_hard = Label(300, 440, 150, 60, YELLOW)
                
            if card_level_normal.collidepoint(x, y):
                card_level_normal = Label(150, 440, 150, 60, GREE)
                card_level_ezze = Label(0, 440, 150, 60, YELLOW)
                card_level_hard = Label(300, 440, 150, 60, YELLOW)
                e = 2

            if card_level_hard.collidepoint(x, y):
                card_level_hard = Label(300, 440, 150, 60, GREE)
                card_level_normal = Label(150, 440, 150, 60, YELLOW)
                card_level_ezze = Label(0, 440, 150, 60, YELLOW)
                e = 3

    window.blit(background,(0,0))

    keys = key.get_pressed()

    if (
        birdie.rect.colliderect(car) or birdie.rect.colliderect(car_2) or 
    birdie.rect.colliderect(car_3) or birdie.rect.colliderect(car_4) or
     birdie.rect.colliderect(car_5) or birdie.rect.colliderect(car_6) or
      birdie.rect.colliderect(car_7) or birdie.rect.colliderect(car_8)
    ):
        birdie.rect.y = 200
        car.rect.x = randint(670, 1300)
        car_2.rect.x = randint(670, 1300)
        car_3.rect.x = randint(670, 1300)
        car_4.rect.x = randint(670, 1300)
        if e == 2:
            car_5.rect.x = randint(670, 1300)
            car_6.rect.x = randint(670, 1300)
        if e == 3:
            car_5.rect.x = randint(670, 1300)
            car_6.rect.x = randint(670, 1300)
            car_7.rect.x = randint(670, 1300)
            car_8.rect.x = randint(670, 1300)
        card_level_ezze = Label(0, 440, 150, 60, YELLOW)
        card_level_normal = Label(150, 440, 150, 60, YELLOW)
        card_level_hard = Label(300, 440, 150, 60, YELLOW)
        e = 0
        if counter >= best_account:
            best_account = counter
        counter = 0
        finicsh = False
        rer  =False

    if finicsh != True:
        card.outline(BLUE, 5)
        card.set_text('Для новой игры нажмите на кнопку', 26)
        card.draw()

        card_level_ezze.outline(BLUE, 5)
        card_level_ezze.set_text('Легко', 26)
        card_level_ezze.draw()

        card_level_normal.outline(BLUE, 5)
        card_level_normal.set_text('Нормально', 26)
        card_level_normal.draw()

        card_level_hard.outline(BLUE, 5)
        card_level_hard.set_text('Тяжело', 26)
        card_level_hard.draw()
    else:
        if e == 2:
            car.speed = 10
            car_2.speed = 10
            car_3.speed = 10
            car_4.speed = 10
            car_5.speed = 10
            car_6.speed = 10

            car_5.management_car()
            car_6.management_car()

            car_5.reset()
            car_6.reset()
        if e == 3:
            car.speed = 12
            car_2.speed = 12
            car_3.speed = 12
            car_4.speed = 12
            car_5.speed = 12
            car_6.speed = 12
            car_7.speed = 12
            car_8.speed = 12

            car_5.management_car()
            car_6.management_car()
            car_7.management_car()
            car_8.management_car()

            car_5.reset()
            car_6.reset()
            car_7.reset()
            car_8.reset()

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

    if (
        car.rect.x <= -69 or car_2.rect.x <= -69 or
         car_3.rect.x <= -69 or car_4.rect.x <= -69
          or car_5.rect.x <= -69 or car_6.rect.x <= -69
           or car_7.rect.x <= -69 or car_8.rect.x <= -69
    ):
        counter += 1

    killed_counter  =  font2.render("Счёт: "+ str(counter), 1, (139, 0, 0))
    window.blit(killed_counter, (10,20))

    killed_counter_2  =  font3.render("Рекорд: "+ str(best_account), 1, (139,0,0))
    window.blit(killed_counter_2, (550,20))
    
    display.update()
    clock.tick(FPS)
