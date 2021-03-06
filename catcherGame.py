from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

game_over = False


catcher_x = 0
berry_x = random.randint(0,7)
berry_y = 0

score = 0

r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

sense.set_pixel(berry_x, berry_y, r)
#Intro text or animation
# 3,2,1 countdown
def move_left():
  global catcher_x
  if catcher_x >= 1:
    catcher_x -= 1
    
def move_right():
  global catcher_x
  if catcher_x <= 7:
    catcher_x += 1
    
def berry_fall():
  global berry_y, berry_x, r
  if berry_y < 7:
    berry_y += 1
    sense.set_pixel(berry_x, berry_y, r)
  else:
    sense.show_message("GAME OVER")
    game_over = True
  
def update():
  global berry_x, berry_y, catcher_x, game_over, r
  sense.clear()
  berry_fall()
  sense.set_pixel(catcher_x, 7, b)
  ##print(“berry x: ” + str(berry_x))
 # print(“berry y: ” + str(berry_y))
  
  
  
while game_over == False:

  for event in sense.stick.get_events():
    print(event)
    if event.action == "pressed" and event.direction == "left":
      move_left()
    elif event.action == "pressed" and event.direction == "right":
      move_right()
      
      
  sleep(1)
  update()
 
      
      