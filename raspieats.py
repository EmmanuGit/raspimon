from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

g = (0,255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255,255,255) #white
##NEW CODE

class Game:
    def __init__(self):
        self.player_x = 1
        self.player_y = 1
        self.food_x = 6
        self.food_y = 6
        self.is_hungry = True

    def down(self):
        if self.player_y <7:
            self.player_y += 1
            print("y:" + str(self.player_y))

    def up(self):
        if self.player_y > 0:
            self.player_y -= 1
            print("y:" + str(self.player_y))

    def left(self):
        if self.player_x  > 0:
            self.player_x -= 1
            print("x:" + str(self.player_x))

    def right(self):
        if self.player_x <7:
            self.player_x += 1
            print("x:" + str(self.player_x))




        
    def update(self):
        sense.clear()
        sense.set_pixel(self.player_x,self.player_y, g)
        sense.set_pixel(self.food_x,self.food_y, b)

    

    def run(self):
        self.update()
        while self.is_hungry:
            for event in sense.stick.get_events():
                if event.direction  == "down" and event.action == "released":
                    self.down()
                    self.update()
                elif event.direction  == "up" and event.action == "released":
                    self.up()
                    self.update()
                elif event.direction == "left" and event.action == "released":
                    self.left()
                    self.update()
                elif event.direction == "right" and event.action == "released":
                    self.right()
                    self.update()
                elif self.player_x == self.food_x and self.food_y == self.player_y:
                    self.player_x = random.choice(range(8))
                    self.player_y = random.choice(range(8))
                    self.food_x = random.choice(range(8))
                    self.food_y = random.choice(range(8))
                    self.update()

                    
                    ##self.is_hungry == False
                    ##sense.show_message("GAME OVER")










                   
        

        


#my_game = Game()

#my_game.run()

"""
###Old Code

#variables for player & itioning
player_x = 1
player_y = 1
sense.set_pixel(player_x,player_y,g)

food_x = 6
food_y = 6
sense.set_pixel(food_x,food_y,k)

is_hungry = True 

def down():
    global player_y
    if player_y <7:
        player_y += 1
        print("y:" + str(player_y))

def update():
    sense.clear()
    sense.set_pixel(player_x,player_y, g)
    sense.set_pixel(food_x,food_y, k)



while is_hungry:
    for event in sense.stick.get_events():
        #print(event)




       
        if event.direction  == "down" and event.action == "released":
            down()
###
            update()
###
"""