import sys
import copy
import numpy
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
sys.setrecursionlimit(2000000000)

def buffer(data):
    line_len = len(data[0]) + 2
    buffer_t_b = ['.'] * line_len
    for d in data:
        d.append('.')
        d.insert(0, '.')
    data.append(buffer_t_b)
    data.insert(0, buffer_t_b)
    return data

exampledata = buffer(list(map(list, open('exampledata', 'r').read().split('\n'))))
data = buffer(list(map(list, open('data', 'r').read().split('\n'))))
coordinates = []

m_up = ['|','7','F']
m_down = ['|', 'L', 'J']
m_l = ['-', 'L', 'F']
m_r = ['-', '7', 'J']

d_l = ["UP", "RIGHT"]
d_7 = ["LEFT", "DOWN"]
d_f = ["RIGHT", "DOWN"]
d_j = ["UP", "LEFT"]
d_vpipe = ["UP", "DOWN"]
d_hpipe = ["LEFT", "RIGHT"]

def chase(data, v_index, h_index,step):
    coordinates.append([h_index, v_index])
    if data[v_index][h_index] == 'S':
        return step
    n_l = data[v_index][h_index-1]
    n_r = data[v_index][h_index+1]
    n_d = data[v_index+1][h_index]
    n_u = data[v_index-1][h_index]
    d = data[v_index][h_index]
    mirrorlist = []
    if d == '7':
        mirrorlist = copy.deepcopy(d_7)
    if d == 'F':
        mirrorlist = copy.deepcopy(d_f)
    if d == 'J':
        mirrorlist = copy.deepcopy(d_j)
    if d == 'L':
        mirrorlist = copy.deepcopy(d_l)
    if d == '|':
        mirrorlist = copy.deepcopy(d_vpipe)
    if d == '-':
        mirrorlist = copy.deepcopy(d_hpipe)
    if ((n_l in m_l) or (n_l == 'S' and step > 1)) and "LEFT" in mirrorlist:
        data[v_index][h_index] = step
        return chase(data, v_index, h_index-1, step+1)
    elif ((n_r in m_r) or (n_r == 'S' and step > 1)) and "RIGHT" in mirrorlist:
        data[v_index][h_index] = step
        return chase(data, v_index, h_index+1, step+1)
    elif ((n_u in m_up) or (n_u == 'S' and step > 1)) and "UP" in mirrorlist:
        data[v_index][h_index] = step
        return chase(data, v_index-1, h_index, step+1)
    elif ((n_d in m_down) or (n_d == 'S' and step > 1)) and "DOWN" in mirrorlist:
        data[v_index][h_index] = step
        return chase(data, v_index+1, h_index, step+1)

def p1(data):
    for index, d in enumerate(data):
        if 'S' in d:
            ind_v = data.index(d)
            ind_h = d.index('S')
            n_l = d[ind_h-1]
            n_r = d[ind_h+1]
            n_u = data[ind_v-1][ind_h]
            n_d = data[ind_v+1][ind_h]
            if n_l in m_l:
                return chase(data, ind_v, ind_h-1, 1)/2
            elif n_r in m_r:
                return chase(data, ind_v, ind_h+1, 1)/2
            elif n_u in m_up:
                return chase(data, ind_v-1, ind_h, 1)/2
            elif n_d in m_down:
                return chase(data, ind_v+1, ind_h, 1)/2
def p2(data, polygon):
    count = 0
    for y, d in enumerate(data):
        for x, c in enumerate(d):
            point = Point(x,y)
            print(point)
            if polygon.contains(point):
                count += 1
    return count

print(p1(data))
coordinates = [[x-2, y-2] for [x,y] in coordinates]
Scoord = coordinates[::-1][0]
coordinates.insert(0, Scoord)
print(p2(data, Polygon(coordinates)))
