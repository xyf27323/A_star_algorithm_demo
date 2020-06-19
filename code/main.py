# main.py

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import random_map
import a_star

plt.figure(figsize=(5, 5))  #生成画布

map = random_map.RandomMap()  #生成整个地图网格和6个障碍物

ax = plt.gca()   #当前坐标轴
ax.set_xlim([0, map.size])
ax.set_ylim([0, map.size])

for i in range(map.size):
    for j in range(map.size):
        if map.IsObstacle(i,j):
            rec = Rectangle((i, j), width=1, height=1, color='gray') #是障碍物画1*1灰方格
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w') #不是障碍物画1*1白方格
            ax.add_patch(rec)

rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')  #起点蓝色
ax.add_patch(rec)

rec = Rectangle((map.size-1, map.size-1), width = 1, height = 1, facecolor='r') #终点红色
ax.add_patch(rec)

plt.axis('equal')
plt.axis('off')
plt.tight_layout()
#plt.show()

a_star = a_star.AStar(map)
a_star.RunAndSaveImage(ax, plt)

