import math
import random

level = 1
exclude = []
vis = [True for i in range(1,104)]
k = 0
while k < (5-level)**3:
    tmp = random.randint(1,102)
    if vis[tmp]:
        exclude.append(tmp)
        vis[tmp] = False
        k+=1
print(exclude)
