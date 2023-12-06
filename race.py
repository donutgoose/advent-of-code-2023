import math

file = open('data', 'r').read().split('\n')

times = list(map(int, list(filter(lambda x: x != '', file[0].split(' ')))[1:]))
distances = list(map(int, list(filter(lambda x: x != '', file[1].split(' ')))[1:]))

acc = ''
for t in times:
    acc += str(t)
times = [int(acc)]

acc = ''
for d in distances:
    acc += str(d)
distances = [int(acc)]

print(times)
print(distances)

def halfOrSomething(n):
    return math.floor(n/4)

acc = 0
vals = []
for index, t in enumerate(times):
    record = distances[index]
    for i in range(t):
        
        speed = i
        time = t - i
        if (speed * time) > record:
            acc += 1
    vals.append(acc)
    acc = 0

acc = 1
for val in vals:
    acc *= val
print(acc)