import random as rnd
import numpy as np

x1 = rnd.randint(0,10)
y1 = rnd.randint(0,10)
x2 = rnd.randint(0,10)
y2 = rnd.randint(0,10)

p1 = [x1,y1]
p2 = [x2,y2]

def distance(p1,p2):

    return np.sqrt( (p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2 ) 

dist = distance(p1,p2)
print(f'p1 = {p1}\np2 = {p2}')
print(f'the distance between them is {round(dist,2)}')