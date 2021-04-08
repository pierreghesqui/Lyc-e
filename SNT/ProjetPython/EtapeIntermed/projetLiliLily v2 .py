TITLE = 'Jumpy Bee'
WIDTH = 300
HEIGHT = 600

def update():
    barry_the_bee.speed += gravity
    barry_the_bee.y += barry_the_bee.speed
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed
    if top_pipe.right < 0:
        top_pipe.left = WIDTH
        bottom_pipe.left = WIDTH
    if barry_the_bee.y > HEIGHT or barry_the_bee.y < 0:
        reset()
    if (barry_the_bee.colliderect(top_pipe) or barry_the_bee.colliderect(bottom_pipe)):
        hit_pipe()

def draw():
    screen.blit('background', (0, 0))
    barry_the_bee.draw()
    top_pipe.draw()
    bottom_pipe.draw()

def on_mouse_down():
    if (barry_the_bee.alive):
        barry_the_bee.speed = -6.5

def reset():
    print ("Back to the start...")
    barry_the_bee.speed = 1
    barry_the_bee.center = (75, 100)
    barry_the_bee.image = "bird1"
    barry_the_bee.alive = True
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)

def hit_pipe():
    print ("Hit pipe!")
    barry_the_bee.image = "beedead"
    barry_the_bee.alive = False

import random
print (random.randint(1,6))

barry_the_bee = Actor('bee1')
gap = 140
top_pipe = Actor('top')
bottom_pipe = Actor('bottom')
scroll_speed = -1
gravity = 0.3
reset()

str(7),
color='white',
midtop =(20, 10),
fontsize=(70)