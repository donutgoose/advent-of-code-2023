import copy

data = open('data', 'r')
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
seeds = []
soil = []
fert = []
water = []
light = []
temp = []
humid = []
location = []

def parse_text(file):
    global seeds
    global soil
    global fert
    global water
    global light
    global temp
    global humid
    global location

    data = file.read().split("\n")
    seeds = list(map(int, data[0].split(" ")[1:]))
    data = data[1:]

    acc = []
    counter = -1
    
    data = list(filter(lambda x: x != '', data))

    for d in data:
        if not(d[0] in nums):
            acc = list(map(lambda x: x.split(" "), acc))
            acc = list(map(lambda x: list(map(int, x)), acc))
            if counter == 0:
                soil = acc
            if counter == 1:
                fert = acc
            if counter == 2:
                water = acc
            if counter == 3:
                light = acc
            if counter == 4:
                temp = acc
            if counter == 5:
                humid = acc
            if counter == 6:
                location = acc
            acc = []
            counter += 1
        else:
            acc.append(d)
    location = list(map(lambda x: x.split(" "), acc))
    location = list(map(lambda x: list(map(int, x)), location))
    return acc

    print(out)
    out1 = out[0:1000]
    out2 = out[::-1]
    out2 = out2[0:1000]
    out2 = out2[::-1]
    out1.extend(out2)
    return out1

def convert(seeds, ranges):
    out = []
    fails = []
    fails = copy.deepcopy(seeds)
    for index, seed in enumerate(seeds):
        print(seeds)
        for d in ranges:
            destination = [d[0], d[0] + d[2]]
            source = [d[1], d[1] + d[2]]
            print(f'{seed} > {seed >= source[0] and source[1] >= seed}')
            if seed >= source[0] and source[1] >= seed and seed in fails:
                _ind = seed - source[0]
                print(f'\n{seed} > {destination[0] + _ind}\n')
                out.append(destination[0] + _ind)
                #breakpoint()
                fails[index] = -1
    out.extend(list(filter(lambda x: x != -1, fails)))
    print('\n')
    return out

parse_text(data)

seeds = convert(seeds, soil)
print(seeds)
seeds = convert(seeds, fert)
seeds = convert(seeds, water)
seeds = convert(seeds, light)
seeds = convert(seeds, temp)
seeds = convert(seeds, humid)
seeds = convert(seeds, location)

min = 99999999999999999999999
for seed in seeds:
    if seed < min:
        min = copy.deepcopy(seed)

print(min)
