import copy
from test import sort
symbols = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
data = open('/home/donutgoose/day7/data', 'r').read().split('\n')
acc = []
for d in data:
    acc.append(d.split(' '))
data = acc[::-1][1:][::-1]
def getHands(line):
    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(line)
    for ind, c in enumerate(line[0]):
        nums[symbols.index(c[0])] += 1
    jIndex = 0
    maxim = max(nums[0:12])
    #breakpoint()
    for index, n in enumerate(nums):
        if index != 12 and n == maxim:
            #breakpoint()
            print(f'{index} > {n}')
            #print(symbols[index])
            nums[index] += nums[12]
            #print(nums[index])
            nums[12] = 0
            #print(nums[12])
    #print(nums)
    nums = list(filter(lambda x: x != 0, nums))
    nums.sort()
    if nums == [1,1,1,1,1]:
        line.append(6)
    elif nums == [1,1,1,2]:
        line.append(5)
    elif nums == [1,2,2]:
        line.append(4)
    elif nums == [1,1,3]:
        line.append(3)
    elif nums == [2,3]:
        line.append(2)
    elif nums == [1,4]:
        line.append(1)
    elif nums == [5]:
        line.append(0)
    return line
for index, d in enumerate(data):
    data[index] = getHands(d)
l0 = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
for d in data:
    #print(d)
    d[2] = f'0x{d[2]}{hex(symbols.index(d[0][0]))[2:]}{hex(symbols.index(d[0][1]))[2:]}{hex(symbols.index(d[0][2]))[2:]}{hex(symbols.index(d[0][3]))[2:]}{hex(symbols.index(d[0][4]))[2:]}'
for d in data:
    if d[2][2:][0] == '0':
        l0.append(d)
    if d[2][2:][0] == '1':
        l1.append(d)
    if d[2][2:][0] == '2':
        l2.append(d)
    if d[2][2:][0] == '3':
        l3.append(d)
    if d[2][2:][0] == '4':
        l4.append(d)
    if d[2][2:][0] == '5':
        l5.append(d)
    if d[2][2:][0] == '6':
        l6.append(d)
#print(l4)
#print(l3)
#print(l1)
l0 = sort(l0)
l1 = sort(l1)
l2 = sort(l2)
l3 = sort(l3)
l4 = sort(l4)
l5 = sort(l5)
l6 = sort(l6)
data2 = []
data2.extend(l0)
data2.extend(l1)
data2.extend(l2)
data2.extend(l3)
data2.extend(l4)
data2.extend(l5)
data2.extend(l6)
data2 = data2[::-1]
acc = 0
for index, d in enumerate(data2):
    acc += (index + 1) * int(d[1])
    print(f'{d[0]} >> {d[2][2]} | {index + 1} * {d[1]} ')
print(acc)
print(f'Corect: 245461700 {acc == 245461700}')

