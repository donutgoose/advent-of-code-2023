exampledata = open('data', 'r').read().split('\n')

def removePrefix(something):
    ind = 0
    for index, d in enumerate(something):
        if d == ":":
            ind = index
    return something[ind+2:]

def removeSpaces(li):
    acc = []
    for d in li:
        if d == '':
            pass
        else:
            acc.append(d)
    return acc

def convertToPlist(d):
    d = d.split(' ')
    ideal = []
    real = []
    first = True
    for p in d:
        if p == '|':
            first = False
        if first:
            ideal.append(p)
        else:
            if p != '|':
                real.append(p)
    return [ideal, real]

def commonElements(plist):
    l1 = plist[0]
    l2 = plist[1]
    acc = [1]
    for d in l1:
        if d in l2:
            acc.append(d)
    return removeSpaces(acc)

exampledata = list(map(removePrefix, exampledata)) # remove Card X: 
exampledata = list(map(convertToPlist, exampledata)) # convert from string
exampledata = list(map(commonElements, exampledata)) # turn into only common elements

#remove last element bc it was adding one idk why lol
exampledata = exampledata[::-1]
exampledata = exampledata[1:]
exampledata = exampledata[::-1]

_len = 0
acc = 0
for index, d in enumerate(exampledata):
    _len = len(d) - 1
    if _len != 0:
        for i in range(d[0]):
            for i in range(_len):
                exampledata[index + i + 1][0] += 1
acc = 0
for d in exampledata:
    acc += d[0]
print(acc)
