def last(li): return li[::-1][0]
data = [list(filter(lambda x: x != ' ', y.split(' '))) for y in (open('data', 'r').read().split('\n'))][::-1][1:][::-1]
def predict(line):
    diffs = [list(map(int, line))]
    while len(set(last(diffs))) > 1:
        acc = []
        for index, l in enumerate(last(diffs)):
            if (index + 1) < len(last(diffs)):
                acc.append(last(diffs)[index+1] - l)
            else:
                diffs.append(acc)
                break
    diffs = diffs[::-1]
    diffs[0].append(diffs[0][0])
    poopy = diffs[1:]
    for index, d in enumerate(poopy):
        poopy[index].append(last(d)+last(diffs[index]))
    return last(last(poopy))
print(f'Part 1: {sum([predict(d) for d in data])}')
print(f'Part 2: {sum([predict(d[::-1]) for d in data])}')