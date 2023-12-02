red, green, blue = [], [], []
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cubes = [12, 13, 14]

example1 = "Game 13: 3 red, 11 green, 1 blue; 11 green, 1 red, 3 blue; 12 blue, 5 red, 2 green; 1 blue, 8 red, 5 green; 8 red, 12 blue, 1 green; 1 blue, 4 green, 6 red"
example2 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
example3 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
example4 = "Game 66: 1 red, 3 green, 4 blue; 3 green, 5 red, 14 blue; 1 blue, 3 red, 2 green; 4 blue, 1 green, 2 red; 8 red, 2 green, 13 blue"
example5 = "Game 100: 13 green, 12 red; 14 blue, 12 red, 13 green; 14 blue, 12 red, 13 green; 1 blue, 5 green, 1 red; 2 red, 1 green"

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
            if 'red' in _str and outnum > cubes[0]:
                acc = [outnum, acc[1], acc[2]]
            if 'green' in _str and outnum > cubes[1]:
                acc = [acc[0], outnum, acc[2]]
            if 'blue' in _str and outnum > cubes[2]:
                acc = [acc[0], acc[1], outnum]
        else:
            skipNextNum = False
    #out.append(acc)
    #return out[1:]
    return acc == [0,0,0]

# def compare(li):
#     lists = parse(li)
#     for l in lists:
#         if (l[0] > cubes[0]) or (l[1] > cubes[1]) or (l[2] > cubes[2]):
#             return False
#     return True

print(parse(example1))
print(parse(example2))


accum = 0
with open('data', 'r') as file:
    for line in file:
        _line = line.strip()
        if parse(_line):
            num = _line[5]
            if _line[6] in nums:
                num = f'{num}{_line[6]}'
            if _line[7] in nums:
                num = f'{num}{_line[7]}'
            accum += int(num)
        #print(f'{_line[5]} > {parse(_line)}')
print(accum)

#print(compare(example5))