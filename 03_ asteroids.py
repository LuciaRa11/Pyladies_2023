import pyglet

import math
from random import random
window = pyglet.window.Window(1200,800)
bg = pyglet.resource.image('sky.png')
direction=set()

label = pyglet.text.Label("Crash! Game Over",
                          font_name='Arial',
                          font_size=35,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label.visible = False

class Spaceship:
    def __init__(self, x, y, x_speed, y_speed, sprite,radius):
        self.x = x
        self.y = y
        self.x_speed= x_speed
        self.y_speed= y_speed
        self.sprite=sprite
        self.rotation=0
        self.ROTATION_SPEED = 7
        self.ACCELERATION=50
        self.radius=radius

    def draw(self):
        self.sprite.x=self.x
        self.sprite.y=self.y
        self.sprite.rotation=self.rotation
        self.sprite.draw()
        
    def update_position(self, t):
        self.x+=self.x_speed*t
        self.y+=self.y_speed*t
        self.update()
        self.hold_update(t)

    def update(self):
        min_x = 0
        min_y = 0
        max_x = 1200
        max_y = 800
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def hold_update(self,pt):
        if 65361 in direction: #left
            self.rotation+=-pt*45
        elif 65363 in direction: #right
            self.rotation+=pt*45
        elif 65362 in direction: #speed up
            self.x_speed +=pt *self.ACCELERATION * math.sin(self.rotation/360*2*math.pi)
            self.y_speed +=pt* self.ACCELERATION * math.cos(self.rotation/360*2*math.pi)
        elif 65364 in direction: #speed down
            self.x_speed -=pt *self.ACCELERATION * math.sin(self.rotation/360*2*math.pi)
            self.y_speed -=pt* self.ACCELERATION * math.cos(self.rotation/360*2*math.pi)

def distance(a, b, wrap_size):
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result

def overlaps(a, b):
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2
    return distance_squared < max_distance_squared

class Meteor:
    def __init__(self, x, y, x_speed, y_speed, sprite,radius):
        self.x = x
        self.y = y
        self.x_speed= x_speed
        self.y_speed= y_speed
        self.sprite=sprite
        self.radius=radius

    def draw(self):
        self.sprite.x=self.x
        self.sprite.y=self.y
        self.sprite.draw()

    def update_position(self, t):
        self.x+=self.x_speed*t
        self.y+=self.y_speed*t
        self.update()

    def update(self):
        min_x = 0
        min_y = 0
        max_x = 1200
        max_y = 800
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
      
image = pyglet.image.load('playerShip1_red.png')
image.anchor_x = image.width // 2
image.anchor_y = image.height // 2

ship = pyglet.sprite.Sprite(image)

image2 = pyglet.image.load('meteorBrown_big1.png')
image2.anchor_x = image.width // 2
image2.anchor_y = image.height // 2

meteor = pyglet.sprite.Sprite(image2)


def draw():
    window.clear()
    bg.blit(0,0)
    ship1.draw()
    meteor1.draw()
    meteor2.draw()
    meteor3.draw()
    label.draw()

    
def update_position(t):
    shipOverlapsMeteor = False
    for meteor in [meteor1,meteor2,meteor3]:
       if overlaps(ship1, meteor):
           shipOverlapsMeteor = True
           label.visible=True
           break

    if shipOverlapsMeteor==False:
    # do the below only if ship does not overlap any meteor
        ship1.update_position(t)
        meteor1.update_position(t)
        meteor2.update_position(t)
        meteor3.update_position(t)
   
pyglet.clock.schedule_interval(update_position, 1/30)

def on_key_press(sym, mod): #move
    direction.add(sym)
    
def on_key_release(sym, mod): 
    direction.remove(sym)

ship1=Spaceship(100,100,0,30, ship,30)
meteor1=Meteor(500,800,0,-50,meteor,30)
meteor2=Meteor(0,700,40,0,meteor,30)
meteor3=Meteor(1000,300,-80,0,meteor,30)

objects=[ship1,meteor1,meteor2,meteor3]

window.push_handlers(
    on_draw=draw,
    on_key_press=on_key_press,
    on_key_release=on_key_release
)

pyglet.app.run()
