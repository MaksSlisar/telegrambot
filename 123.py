import random
import time

from pynput import keyboard
from pynput.keyboard import Listener

from app import sendMessage, editMsgtxt

height=15
width=30
eatfood=False

def snakesfood():
    x = random.randint(0, width)
    y = random.randint(0, height)
    return Point(x, y)




b="right"
def on_press(key):
    global b
    if key.name=="right":
        b="right"

    if key.name=="left":
        b="left"

    if key.name=="down":
        b="down"

    if key.name=="up":
        b="up"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

food = snakesfood()

snakepoints=[Point(6,3),Point(5,3),Point(4,3)]


def isSnake(x, y):
    for point in snakepoints:
        if point.x==x and point.y==y:
            return True
    return False



def printsnake():
    data=""
    for i in range(height):
        for j in range(width):
            if isSnake(j,i)or food.x==j and food.y==i :
                data+="*"
            else:
                data+=" "
        data+="\n"
    editMsgtxt(1204383766,1204 ,data)


def move():
    global b,eatfood

    for i in range(len(snakepoints) - 1, 0, -1):
        if eatfood==True and len(snakepoints) - 1 == i :
            eatfood=False
        else:
            snakepoints[i].y = snakepoints[i - 1].y
            snakepoints[i].x = snakepoints[i - 1].x


    if b=="right":
        if snakepoints[0].x==width-1:
            snakepoints[0].x=0
        else:
            snakepoints[0].x+=1


    if b=="left":
        if snakepoints[0].x==0:
            snakepoints[0].x=width-1
        else:
            snakepoints[0].x-= 1


    if b=="up":
        if snakepoints[0].y==0:
            snakepoints[0].y=height - 1
        else:
            snakepoints[0].y -= 1

    if b=="down":
        if snakepoints[0].y == height - 1:
            snakepoints[0].y = 0
        else:
            snakepoints[0].y += 1

    eat()

def eat():
    global  snakepoints, food, eatfood
    if food.x  == snakepoints[0].x and food.y == snakepoints[0].y :
        snakepoints.append(Point(snakepoints[len(snakepoints)-1].x, snakepoints[len(snakepoints)-1].y))
        eatfood=True
        food=snakesfood()





listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys

while(True):
    printsnake()
    move()
    time.sleep(0.5)


