from random import randint
import math

class ball:
    def __init__(duck):
        duck.y = 46 + randint(5,6)
        duck.x = 22
        duck.vy = 0
        duck.vx = 1
    def change_direction(duck,x,y):
        if(x):
            duck.vx *= -1
        if(y):
            duck.vy *= -1