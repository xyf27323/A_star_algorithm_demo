# random_map.py

import numpy as np

import point

class RandomMap:
    def __init__(self, size=50):
        self.size = size
        self.obstacle = size//8
        self.GenerateObstacle()

    def GenerateObstacle(self):
        self.obstacle_point = []
        self.obstacle_point.append(point.Point(self.size//2, self.size//2))
        self.obstacle_point.append(point.Point(self.size//2, self.size//2-1))


        # Generate an obstacle in the middle   以25,25对称斜向的障碍
        for i in range(self.size//2-4, self.size//2):  #21-25 不包括25
            self.obstacle_point.append(point.Point(i, self.size-i))   #21,29 22,28 23,27 24,26 
            self.obstacle_point.append(point.Point(i, self.size-i-1)) #21,28 22,27 23,26 24,25 
            self.obstacle_point.append(point.Point(self.size-i, i))   #29,21 28,22 27,23 26,24 
            self.obstacle_point.append(point.Point(self.size-i, i-1)) #29,20 28,21 27,22 26,23 

        for i in range(self.obstacle-1):  #0-5
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(point.Point(x, y))

            if (np.random.rand() > 0.5): # Random boolean
                for l in range(self.size//4):  #0-12
                    self.obstacle_point.append(point.Point(x, y+l))  #竖向
                    pass
            else:
                for l in range(self.size//4):
                    self.obstacle_point.append(point.Point(x+l, y))  #横向
                    pass

    def IsObstacle(self, i ,j):
        for p in self.obstacle_point:
            if i==p.x and j==p.y:
                return True
        return False