example_seeds = [79,14,55,13]
example_1 = [[50,98,2],[52,50,48]]
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
    #print(f'ACC > {acc}')
    return acc

def convert(seeds, ranges):
    out = []
    seeds2 = seeds
    for d in ranges:
        destination = list(range(d[0], d[0] + d[2]))
        source = list(range(d[1], d[1] + d[2]))
        print(f'DESTINATION > {destination}')
        print(f'SOURCE > {source}')
        for index, sour in enumerate(source):
            if sour in seeds:
                out.append(destination[index])
                del(seeds2[seeds2.index(sour)])
        # for seed in seeds:
        #     print(f'{seed} > ')
        #     if seed in source:
        #         out.append(destination[source.index(seed)])
        #         del(seeds2[seeds2.index(seed)])
    out.extend(seeds2)
    print('\n')
    return out

parse_text(data)
ranges = [soil,fert,water,light,temp,humid,location]

# print(f'SOIL > {soil}')
# print(f'FERT > {fert}')
# print(f'WATER > {water}')
# print(f'LIGHT > {light}')
# print(f'TEMP > {temp}')
# print(f'HUMIDITY > {humid}')
# print(f'LOCATION > {location}')

ranges = ranges[1:]
#print(ranges)

print("its runnin lol")

seeds = convert(seeds, soil)
#print(seeds)
seeds = convert(seeds, fert)
#print(seeds)
seeds = convert(seeds, water)
#print(seeds)
seeds = convert(seeds, light)
#print(seeds)
seeds = convert(seeds, temp)
#print(seeds)
seeds = convert(seeds, humid)
#print(seeds)
seeds = convert(seeds, location)
#print(seeds)


print(seeds)