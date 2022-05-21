import random
from brick import brick
from colorama import Back

class brick_block:
    def __init__(duck):
        duck.block = [[] for i in range(3)]
        duck.bricks = [{} for i in range(3)]
        duck.max_score = [0 for i in range(3)]
        for l in range(3):
            exclude = []
            vis = [True for z in range(171)]
            k = 0
            val = (5-l)**3
            while k < val:
                tmp1 = random.randint(1,170)
                if vis[tmp1]:
                    exclude.append(tmp1)
                    vis[tmp1] = False
                    k+=1
            for i in range(10):
                for j in range(17):
                    if (i*17+j+1) in exclude:
                        continue
                    else:
                        if i%2:
                            tmp = random.randint(1, 4)
                        else:
                            tmp = random.randint(1, 3)
                        temp = brick(tmp, i, j*6 + (i%2)*3)
                        duck.bricks[l][(i, j*6 + (i%2)*3)] = temp
                        duck.block[l].append(temp)
                        if tmp < 4:
                            duck.max_score[l]+=tmp

    def render(duck):
        #level = 1
        '''exclude = []
        vis = [True for i in range(1,103)]
        k = 0
        while k < (5-level)**3:
            tmp = random.randint(1,102)
            if vis[tmp]:
                exclude.append(tmp)
                vis[tmp] = False
                k+=1'''
        display = []
        #color = []
        for i in range(10):
            temp_dis = []
            #temp_col = []
            l=0
            for j in duck.block[i]:
                l+=1
                temp = (i*10 + l)
                if temp in exclude:
                    temp_dis = temp_dis + 6 * [' ']
                else:
                    if i%2:
                        rend = j.render()
                        temp_dis = temp_dis + 3 * [' '] + rend
                        #temp_col = temp_col + [Back.RESET] * 3 + col
                        print(i)
                    else:
                        rend = j.render()
                        temp_dis = temp_dis + rend + 3 * [' ']
                        #temp_col = temp_col + col + 3 * [Back.RESET]
            display.append(temp_dis)
            #color.append(temp_col)
        return display