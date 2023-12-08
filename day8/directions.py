import math
data = open('/home/donutgoose/day8/data', 'r').read().split('\n')
step = 0
dirs = data[0]
currentLocation = "AAA"
adresses = list(map(lambda balls: [balls.split(' ')[0],balls.split(' ')[2][1:4],balls.split(' ')[3][:3]], (data[2:][::-1][1:][::-1])))
adresses_first = list(map(lambda x: x[0], adresses))
def p1():
    global currentLocation; global step
    while currentLocation != "ZZZ":
        for d in dirs:
            if currentLocation == 'ZZZ':break
            if d == 'L': step += 1; currentLocation = adresses[adresses_first.index(currentLocation)][1]
            if d == 'R': step += 1; currentLocation = adresses[adresses_first.index(currentLocation)][2]
p1(); print(f'Part 1: {step}')
adr_a = [lo for lo in adresses_first if lo.endswith('A')]
print(adr_a)
def p2(location):
    step = 0
    while not(location.endswith('Z')):
        #breakpoint()
        for d in dirs:
            if location.endswith('Z'):
                break
            elif d == 'L':
                step += 1
                location = adresses[adresses_first.index(location)][1]
            elif d == 'R':
                step += 1
                location = adresses[adresses_first.index(location)][2]
    return step
out = list(map(p2, adr_a))
print(f'Part 2: {math.lcm(*out)}')
