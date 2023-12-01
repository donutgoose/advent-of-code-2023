nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
words = ['one', 'two', 'six', 'four', 'five', 'nine', 'three', 'seven', 'eight', 'eno', 'owt', 'xis', 'ruof', 'evif', 'enin', 'eerht', 'neves', 'thgie']

data = open('advent_day1_inputs', 'r')
example_data = open('example_data', 'r')
acc = 0

def convert(s):
    _words = {
        'one':'1',
        'eno':'1',
        'two':'2',
        'owt':'2',
        'three':'3',
        'eerht':'3',
        'four':'4',
        'ruof':'4',
        'five':'5',
        'evif':'5',
        'six':'6',
        'xis':'6',
        'seven':'7',
        'neves':'7',
        'eight':'8',
        'thgie':'8',
        'nine':'9',
        'enin':'9'
    }
    return _words[s]

def firstint(li, acc=''):
    for i in range(len(li)):
        try:
            if li[i:i+5] in words:
                return convert(li[i:i+5])
        except:
            pass
        
        try:
            if li[i:i+4] in words:
                return convert(li[i:i+4])
        except:
            pass
        
        try:
            if li[i:i+3] in words:
                return convert(li[i:i+3])
        except:
            pass
        
        if li[i] in nums:
            return li[i]



# example = "two1nine"
# print(firstint(example))
# print(firstint(example[::-1]))

for line in data:
    _line = line.strip()
    print(_line)
    first = firstint(_line)
    last = firstint(_line[::-1])
    _str = first + last
    print(_str)
    acc += int(_str)
print(acc)
