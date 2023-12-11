from itertools import combinations
import numpy as np
def getColumn(inp, index):
    inp = list(filter(lambda x: x != [], inp))
    return [x[index] for x in inp]

def getCoordinatePairs(data):
    coordinates = []
    for index_1, d in enumerate(data):
        if '#' in d:
            for index_2, z in enumerate(d):
                if z == '#':
                    coordinates.append([index_2, index_1])
    return coordinates

def expansion(data,coords,factor):
    count = 0
    for index, d in enumerate(data):
        if not('#' in d):
            print(f'ROW DUPED >>> {index+count}')
            coords = modifyCoords(index+count, coords, 1, factor)
            count += factor
    
    count = 0
    for index, d in enumerate(data[0]):
        if not('#' in getColumn(data, index)):
            print(f'COLUMN DUPED >> {index+count}')
            coords = modifyCoords(index+count, coords, 0, factor)
            count += factor
    return coords

def modifyCoords(ind, coords, xy, factor):
    for c in coords:
        if c[xy] > ind:
            c[xy] += factor
    return coords

def dist(n1,n2):
    return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

def calcPaths(coords):
    acc = 0
    for d in list(combinations(coords, 2)):
        acc += dist(d[0], d[1])
    return acc

exampledata = list(map(list, open('exampledata', 'r').read().split('\n')))
exampledata_correct = list(map(list, open('exampledata', 'r').read().split('\n')))
data = list(map(list, open('data', 'r').read().split('\n')))

fctor = int(input('Factor >> '))
coordinates = getCoordinatePairs(data)
print(coordinates)
coordinates = expansion(data, coordinates, fctor-1)
print(coordinates)
print(calcPaths(coordinates))
