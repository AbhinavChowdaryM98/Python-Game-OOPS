import colorama
from colorama import Back
from termcolor import colored
import os
import time
import random
from ball import ball
from input import *
from display import screen
from block import brick_block
from paddle import paddle
from getch import *
import math
import random

colorama.init()

#Required Functions
def maximum(a,b):
    if a>b:
        return a
    return b

#Constants
sc = screen()
brick_board = brick_block()
paddle = paddle()
ball = ball()
game_over = True
'''
#Movement
inp = False
inc = 1
prev_inp = 's'
t = time.time()

#Add Bricks
sc.update_brick_block(brick_board.block[sc.level])

sc.update_paddle(paddle)
sc.showball(ball.x, ball.y)
'''
first = True
while sc.lives and sc.level<4:
    sc.display[ball.x][ball.y] = ' '
    #Movement
    inp = False
    inc = 1
    prev_inp = 's'
    prev_level = 1
    t = time.time()
    ball.x = 22
    ball.y = paddle.x + random.randint(5,6)
    ball.vy = 0
    ball.vx = 1
    if prev_level != sc.level or first:
        #Add Bricks
        first = False
        for i in range(sc.height):
            for j in range(sc.width):
                sc.display[i][j] = ' '
        sc.update_brick_block(brick_board.block[sc.level-1])
        prev_level = sc.level

    sc.update_paddle(paddle)
    sc.showball(ball.x, ball.y)
    while True:
        if time.time() - t >= 0.15:
            t = time.time()
            letter = user_input(0.15)
            if letter == 'a':
                if prev_inp == 'a':
                    inc+=1
                    paddle.x-=inc
                    ball.y-=inc
                else:
                    inc=1
                    prev_inp = 'a'
                    paddle.x-=1
                    ball.y-=inc
                #sc.update_paddle(paddle)
            elif letter == 'd':
                if prev_inp == 'd':
                    inc+=1
                    paddle.x+=inc
                    ball.y+=inc
                else:
                    prev_inp = 'd'
                    inc=1
                    paddle.x+=1
                    ball.y+=inc
                #sc.update_paddle(paddle)
            elif letter == 'p':
                break
            elif letter == 'q':
                sc.lives = 0
                game_over = False
                break
            else:
                prev_inp = 's'
            if paddle.x > sc.width - paddle.size:
                paddle.x = sc.width - paddle.size
                ball.y-=inc
            elif paddle.x < 0:
                paddle.x=0
                ball.y+=inc 
            sc.update_paddle(paddle)
            sc.updateball(ball.x,ball.y)
            #block_display, block_color = brick_board.render()
            os.system("clear")
            sc.render()
    
    t_temp = time.time()
    i_temp = 0

    while True and game_over:
        if time.time() - t >= 0.15:
            t = time.time()
            if time.time() - t_temp >= 30:
                #sc.fallbricks()
                t_temp = time.time()
                i_temp+=1
                sc.update_brick_block(brick_board.block[sc.level-1],i_temp)
            if ball.y <=0 or ball.y > sc.width - 2:
                ball.change_direction(0,1)
            if ball.x <= 0:
                ball.change_direction(1,0)
            if ball.x == sc.width - 2:
                if ball.y < paddle.x + paddle.size and paddle.x <= ball.y:
                    ball.change_direction(1,0)
                    ball.vy += (floor((ball.y - paddle.x + 1)/2) - 3)
                else:
                    print('Game Over')
                    break
            if ball.x <= 10:
                if ball.vx < 0:
                    if ball.x:
                        if '#' in sc.display[ball.x-1][ball.y]:
                            brick_x = ball.x - 1
                            if (ball.x - i_temp) % 2:
                                brick_y = ball.y - (ball.y) % 6
                            else:
                                brick_y = ball.y - (ball.y - 3) % 6
                            temp = brick_board.bricks[sc.level-1][(brick_x - i_temp , brick_y)].score
                            if temp != 4:
                                temp-=1
                                sc.points_scored[sc.level-1]+=1
                            brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)]\
                                .score = temp
                            sc.update_brick_block(brick_board.block[sc.level-1],i_temp)
                            ball.change_direction(1,0)
                else:
                    if '#' in sc.display[ball.x + 1][ball.y]:
                        brick_x = ball.x + 1
                        if (brick_x - i_temp) % 2:
                            brick_y = ball.y - (ball.y - 3) % 6
                        else:
                            brick_y = ball.y - ball.y % 6
                        if brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)].score != 4:
                            sc.points_scored[sc.level-1]+=1
                            brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)].score-=1
                        sc.update_brick_block(brick_board.block[sc.level-1],i_temp)
                        ball.change_direction(1,0)
                if ball.vy < 0:
                    if ball.y>0:
                        if '#' in sc.display[ball.x][ball.y-1]:
                            if (ball.x - i_temp) % 2:
                                brick_y = ball.y - (ball.y - 3) % 6
                            else:
                                brick_y = ball.y - ball.y % 6
                            brick_x=ball.x
                            temp = brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)].score
                            if temp != 4:
                                temp-=1
                                sc.points_scored[sc.level-1]+=1
                                brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)].score = temp
                            sc.update_brick_block(brick_board.block[sc.level-1],i_temp)
                            ball.change_direction(0,1)
                elif ball.vy > 0:
                    if ball.y < sc.width - 1:
                        if '#' in sc.display[ball.x][ball.y+1]:
                            brick_x = ball.x
                            '''if (brick_x-i_temp)%2:
                                brick_y = ball.y - ball.y%6
                            else:
                                brick_y = ball.y - (ball.y - 3)%6'''
                            brick_y = ball.y+1
                            temp = brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)]\
                                .score
                            if temp != 4:
                                temp-=1
                                sc.points_scored[sc.level-1]+=1
                                brick_board.bricks[sc.level-1][(brick_x-i_temp,brick_y)].score = temp
                            sc.update_brick_block(brick_board.block[sc.level-1], i_temp)
                            ball.change_direction(0,1)
            ball.x = ball.x + ball.vx
            ball.y = ball.y + ball.vy
            if ball.y >= sc.width - 1:
                ball.y = sc.width - 1
                ball.vy *= -1
            if ball.y <= 0:
                ball.y = 0
                ball.vy *= -1
            if ball.x < 0 :
                ball.x = 0
                ball.vx *= -1
            if ball.x >= sc.height - 2:
                if ball.y - paddle.x > paddle.size - 1 or ball.y < paddle.x:
                    sc.lives-=1
                    sc.remove_ball(ball.x,ball.y)
                    #sc.lives_print.pop(sc.lives)
                    break
                else:
                    ball.x = sc.height - 2
                    ball.vx *= -1
                    '''tmp_vy = maximum(ball.y-paddle.x, paddle.x + paddle.size - 1 - ball.y)
                    if tmp_vy == 9 or tmp_vy == 8:
                        ball.vy+=2
                    elif tmp_vy == 6 or tmp_vy == 7:
                        ball.vy+=1
                    elif tmp_vy == 5:
                        #ball.vy-=1'''
                    tmp_vy = math.ceil((ball.y-paddle.x+1)/2)
                    tmp_vy = tmp_vy - 3
                    ball.vy+=tmp_vy
                    #print("Yes")
                    #sc.lives = 0
                    #break
            if '#' in sc.display[ball.x][ball.y]:
                ball.x-=1
            sc.updateball(ball.x,ball.y)
            letter = user_input(0.15)
            if letter == 'a':
                if prev_inp == 'a':
                    inc+=1
                    paddle.x-=inc
                else:
                    inc=1
                    prev_inp = 'a'
                    paddle.x-=1
                #sc.update_paddle(paddle)
            elif letter == 'd':
                if prev_inp == 'd':
                    inc+=1
                    paddle.x+=inc
                else:
                    prev_inp = 'd'
                    inc=1
                    paddle.x+=1
                #sc.update_paddle(paddle)
            elif letter == 'q':
                sc.lives = 0
                break
            else:
                prev_inp = 's'
            if paddle.x > sc.width - paddle.size:
                paddle.x = sc.width - paddle.size
            elif paddle.x < 0:
                paddle.x=0
            sc.update_paddle(paddle)
            if i_temp == 12:
                sc.lives-=1
                break
            if sc.points_scored[sc.level-1] == brick_board.max_score[sc.level-1]:
                sc.level+=1
                break
            #sc.updateball(ball.x,ball.y)
            #block_display, block_color = brick_board.render()
            os.system("clear")
            sc.render()