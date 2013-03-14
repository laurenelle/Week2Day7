#create a dictionary to store the inventory of things we pick up
#different colored gems 
# add hearts
#complete maze
# out of bounds loops 
# create a small obstacle
# import images for anything
# create easter egg :D of a key combination?

import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

"""

0 1 2 3 4 5 6 7 8 9
* - - | - - - - - - 
- - - | - - - - - - 
| | - | - - - - - - 
- / - | - - - - - - 
- | - - | - - - - - 
- | - 3 | K - - - - 
- | | | | - - - - - 
- - - - 3 - - - - - 
- - - - - - - - - - 
- - - - - - - - - W 


"""

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Heart(GameElement):
    IMAGE = "Heart"

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just collected a heart! You have %d points."%(len(player.inventory)))

class Key(GameElement):
    IMAGE = "Key"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("Congratulations, you found the key! Continue your quest to find the treasure chest!")


# class OpenChest(GameElement):
#   IMAGE = "OpenChest"
#   SOLID =  False  
#   def interact(self, player):
#       player.inventory.append(self)
#       GAME_BOARD.draw_msg("You just found the chest! Now use the key to open it up.")
#       GAME_BOARD.del_el(chest.x, chest.y, CHEST)
#       GAME_BOARD.set_el(9, 9, open_chest)
#       GAME_BOARD.draw_msg("You win!")

class GreenGem(GameElement):
    IMAGE = "GreenGem"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You win!")



# class GemWinner(GameElement)
#     IMAGE = "GreenGem"
#         def interaction(self, player):
#             play
    
        # GAME_BOARD.set_el(9, 9, GreenGem)
        # GAME_BOARD.draw_msg("You win!")


class BlueGem(GameElement):
    IMAGE = "BlueGem"

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just found a treasure! You have %d items."%(len(player.inventory)))

class Character(GameElement):
    
    IMAGE = "Princess"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
        print self.inventory


    def next_pos(self, direction):
        print "next_pos direction is: " + direction
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

        

###   End class definitions    ####

def keyboard_handler():

    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        # X = range(0, GAME_WIDTH)
        # Y = range(0, GAME_WIDTH)
    
        if next_x < 0:
            next_x = GAME_WIDTH -1
        if next_x > GAME_WIDTH -1:
            next_x = 0
        if next_y < 0:
            next_y = GAME_WIDTH - 1
        if next_y > GAME_WIDTH -1:
            next_y = 0
        existing_el = GAME_BOARD.get_el(next_x, next_y)
        if existing_el:
            existing_el.interact(PLAYER)

        if next_x == 9 and next_y == 9:
        
            green_gem_winner = GreenGem()
            GAME_BOARD.register(green_gem_winner)    
            #loop through a tuple    
            for i, X in enumerate (range(0, GAME_WIDTH)):
                for j, Y in enumerate (range (0, GAME_WIDTH)):


                    GAME_BOARD.del_el(X, Y)
    
                    GAME_BOARD.set_el(X, Y, green_gem_winner) 
            return

        

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)   

        next_move = [next_x, next_y]
        print next_move


def initialize():
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(0, 0, PLAYER)

    rock_positions = [
        (0, 2),
        (1, 2),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (4, 4),
        (4, 5),
        (4, 6),
        (3, 6),
        (2, 6),
        (1, 6),
        (1, 4),
        (1, 5),
        (1, 3)

    ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    GAME_BOARD.draw_msg("Collect all the treasures. Then put them into the chest to win!")
    blue_gem = BlueGem()
    GAME_BOARD.register(blue_gem)
    GAME_BOARD.set_el(4, 7, blue_gem)

    GAME_BOARD.draw_msg("Test")
    green_gem = GreenGem()
    GAME_BOARD.register(green_gem)
    GAME_BOARD.set_el(9, 9, green_gem)



    key = Key()
    GAME_BOARD.register(key)
    GAME_BOARD.set_el(5, 5, key)

    # open_chest = OpenChest()
    # GAME_BOARD.register(open_chest)

    chest_positions = [ 
    (9,9)
    ]


    heart_1 = Heart()
    GAME_BOARD.register(heart_1)
    GAME_BOARD.set_el(3, 5, heart_1)



                
            #   GAME_BOARD.draw_msg("testing")
            # open_the_chest()
            
            



#   rock4 = Rock()
#   GAME_BOARD.register(rock4)
#   GAME_BOARD.set_el(4, 4, rock4)

#   rock5 = Rock()
#   GAME_BOARD.register(rock5
#   GAME_BOARD.set_el(5, 5, rock5)

# initialize() engine initializes by pulling the game.py 

# print "The first rock is at", (rock1.x, rock1.y)
# print "The second rock is at", (rock2.x, rock2.y)
# print "Rock 1 image", rock1.IMAGE 
# print "Rock 2 image", rock2.IMAGE


#    pass
