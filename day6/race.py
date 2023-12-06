import math
file = open('data', 'r').read().split('\n')
times = [int(''.join(list(filter(lambda x: x != '', file[0].split(' ')))[1:]))]
distances = [int(''.join(list(filter(lambda x: x != '', file[1].split(' ')))[1:]))]
acc = 1
for index, t in enumerate(times):
    acc *= (math.floor(((-1*t)-math.sqrt((t*t)-(4*distances[index])))/-2)-math.floor((((-1*t)+math.sqrt((t*t)-(4*distances[index])))/-2)))
print(acc)
