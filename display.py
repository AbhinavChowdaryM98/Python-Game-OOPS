from colorama import Back
from time import time

#c_score = {Back.GREEN:1, Back.YELLOW:2, Back.RED:3, Back.WHITE:-1}
#c = [Back.GREEN, Back.YELLOW, Back.RED, Back.WHITE]

class screen:
    def __init__(duck):
        duck.lives = 5
        #duck.lives_print = ['*' for i in range(5)]
        duck.width = 102
        duck.height = 24
        duck.display = [[' ' for d in range(duck.width)] for s in
                        range(duck.height)]
        #duck.color = [[Back.RESET for a in range(duck.width)] for b in
                      #range(duck.height)]
        duck.s_time = time()
        duck.ballx = 23
        duck.bally = 46
        duck.points_scored = [0 for i in range(3)]
        duck.level=1
        duck.prev_l = 0
    
    #def fallbricks(duck,i):

    def showball(duck,x,y):
        duck.ballx = x
        duck.bally = y
        duck.display[x][y] = 'O'
    
    def updateball(duck,x,y):
        duck.display[duck.ballx][duck.bally] = ' ' + Back.RESET
        duck.bally = y
        duck.ballx = x
        duck.display[duck.ballx][duck.bally] = 'O' + Back.RESET
    
    '''def collapse_brick(duck,x,y):
        score = c_score(duck.display[x][y][0])
        if score==1:
            duck.display[x][y:3] = 3*[' ']
        elif score > 1:
            duck.display[x][y] = [c[score-2]+'#', '#', '#' + Back.RESET]
        duck.points_scored+=1'''
    
    def remove_ball(duck,x,y):
        duck.display[x][y] = ' ' + Back.RESET
        duck.display[duck.ballx][duck.bally] = ' ' + Back.RESET

    def update_brick_block(duck,block,l=0):
        for j in block:
            if duck.prev_l != l:
                duck.display[j.x+l-1][j.y:j.y+3] = 3*[' ']
            duck.display[j.x+l][j.y:j.y+3] = j.render()
            #duck.color[i][j] = color[i][j]

    def update_paddle(duck, paddle):
        duck.display[-1] = paddle.render()


    def render(duck):
        print((duck.width + 2) * ' ')
        for i in range(duck.height):
            print('  ', end="")
            for j in range(duck.width):
                print(duck.display[i][j], end="")
            print(Back.RESET + '  ')
        print((duck.width + 2) * ' ')
        print("Time: {0:.2f}".format(time() - duck.s_time), end="   ")
        print("\n\t\t" + "a:move left\td:move right\tp:to start\tq:quit")
        print("\t\tScore: {}".format(duck.points_scored[duck.level-1]))