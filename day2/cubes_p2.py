red, green, blue = [], [], []
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cubes = [12, 13, 14]

example1 = "Game 1: 3 red, 3 blue, 2 green; 1 red, 7 blue, 1 green"

def parse(li):
    acc = [0,0,0]
    #out = []
    skipNextNum = False
    for i in range(len(li)):
        if li[i] == ';' or li[i] == ':':
            #out.append(acc)
            #acc = [0, 0, 0]
            pass
        elif li[i] in nums and skipNextNum == False:
            ind = 7
            outnum = int(li[i])
            if li[i+1] in nums:
                ind += 1
                outnum = int(li[i] + li[i+1])
                skipNextNum = True
            _str = li[i+2:i+ind]
            if 'red' in _str and outnum > acc[0]:
                acc = [outnum, acc[1], acc[2]]
            if 'green' in _str and outnum > acc[1]:
                acc = [acc[0], outnum, acc[2]]
            if 'blue' in _str and outnum > acc[2]:
                acc = [acc[0], acc[1], outnum]
        else:
            skipNextNum = False
    #out.append(acc)
    #return out[1:]
    return acc

print(parse(example1))

with open('data', 'r') as file:
    accum = 0
    for line in file:
        _line = line.strip()
        _lns = parse(_line)
        accum += _lns[0] * _lns[1] * _lns[2]
    print(accum)



# accum = 0
# with open('data', 'r') as file:
#     for line in file:
#         _line = line.strip()
#         if parse(_line):
#             num = _line[5]
#             if _line[6] in nums:
#                 num = f'{num}{_line[6]}'
#             if _line[7] in nums:
#                 num = f'{num}{_line[7]}'
#             accum += int(num)
#         #print(f'{_line[5]} > {parse(_line)}')
# print(accum)

#print(compare(example5))
