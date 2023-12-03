#example1 = '\n' + open('exampledata', 'r').read() + '\n'
line_len = 10 # 10
example1 = [(line_len * '.')]
example1.extend(open('exampledata', 'r').read().split('\n'))
stri = ('.' * 10) + 'END'
example1.append(stri)
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '=', '+', '-']
symbol_memory = []

readable = open('data', 'r').read()
example1 = f'\n{readable}\n'
print(readable)
print(example1)

def isNumber(num):
    return num in nums

three = False
line_len = 140 + 1
#line_len = 10 + 1 
acc = 0
for i in range(len(example1)):
    if not(example1[i]) in nums: three = False
    #if True: print(example1[i])
    try:
        if (example1[i] in nums) and (example1[i+1] in nums) and (example1[i+2] in nums):
            symbol = []
            three = True
            included = False
            out = int(f'{example1[i]}{example1[i+1]}{example1[i+2]}')
            try:
                print(str(out) + " > " + example1[i-1])
                if example1[i-1] in symbols:
                    included = True
                    symbol.append([example1[i-1], (i-2), out])
            except: pass
            
            try:
                print(str(out) + " > " + example1[i+3])
                if example1[i+3] in symbols:
                    print('jhgjgjgjhgjhgjhgjhgjhgjhgjhg')
                    included = True
                    print(included)
                    print(example1[i+3])
                    print(str(i+3))
                    print(out)
                    symbol.append([example1[i+3], (i+2), out])
                    print([example1[i+3], (i+3), out])
            except: pass
            
            try:
                print(str(out) + " > " + example1[(i-1)-line_len:(i+4)-line_len].replace('\n','<NEWLINE>'))
                for index, d in enumerate(example1[(i-1)-line_len:(i+4)-line_len]):
                    if d in symbols:
                        included = True
                        symbol.append([d, (i - line_len + index - 2), out])
            except: pass
            
            try:
                print(str(out) + " > " + example1[(i-1)+line_len:(i+4)+line_len].replace('\n','<NEWLINE>'))
                for index, d in enumerate(example1[(i-1)+line_len:(i+4)+line_len]):
                    if d in symbols:
                        included = True
                        symbol.append([d, (i + line_len + index - 2), out])
            except: pass

            print(f'{out} > {included}')# \n')
            print(f'{out} > {symbol} \n')
            if included:
                acc += out
                for sym in symbol:
                    symbol_memory.append(sym)
                #symbol_memory.extend(symbol)
    except: pass
    #print("SDLFJSDFKJ")
    try:
        if (example1[i] in nums) and (example1[i+1] in nums) and not(example1[i-1] in nums) and not(example1[i+2] in nums):
            print(f'{example1[i]}{example1[i+1]} pass')
            symbol = []
            included = False
            two = True
            out = int(f'{example1[i]}{example1[i+1]}')
            try:
                if example1[i-1] in symbols:
                    included = True
                    symbol.append([example1[i-1], (i-2), out])
            except: pass
            
            try:
                if example1[i+2] in symbols:
                    print("fhsdkfdsh")
                    included = True
                    symbol.append([example1[i+2], (i+1), out])
            except: pass
            
            try:
                print(str(out) + " > " + example1[(i-1)-line_len:(i+3)-line_len].replace('\n','<NEWLINE>'))
                for index, d in enumerate(example1[(i-1)-line_len:(i+3)-line_len]):
                    if d in symbols:
                        included = True
                        symbol.append([d, (i - line_len + index - 2), out])
            except: pass
            
            try:
                print(str(out) + " > " + example1[(i-1)+line_len:(i+3)+line_len].replace('\n','<NEWLINE>'))
                for index, d in enumerate(example1[(i-1)+line_len:(i+3)+line_len]):
                    if d in symbols:
                        included = True
                        symbol.append([d, (i + line_len + index - 2), out])
            except: pass

            print(f'{out} > {included} \n')
            print(f'{out} > {symbol} \n')
            if included:
                acc += out
                for sym in symbol:
                    symbol_memory.append(sym)
               #symbol_memory.extend(symbol)
    except: pass

    try:
        if example1[i] in nums and not(example1[i-1] in nums) and not(example1[i+1] in nums):
            symbol = []
            out = int(example1[i])        
            included = False
            try:
                if example1[i+1] in symbols:
                    included = True
                    symbol.append([example1[i+1], (i), out])
            except: pass

            try:
                if example1[i-1] in symbols:
                    included = True
                    symbol.append([example1[i-1], (i-2), out])
            except: pass

            try:
                print(str(out) + " > " + example1[(i-1)-line_len:(i+2)-line_len].replace('\n','<NEWLINE>'))
                for index, d in enumerate(example1[(i-1)-line_len:(i+2)-line_len]):
                    if d in symbols:
                        included = True
                        symbol.append([d, (i - line_len + index - 2), out])
            except: pass
            
            try:
                print(str(out) + " > " + example1[(i-1)+line_len:(i+2)+line_len].replace('\n','<NEWLINE>'))
                for index, d in enumerate(example1[(i-1)+line_len:(i+2)+line_len]):
                    if d in symbols:
                        included = True
                        symbol.append([d, (i + line_len + index - 2), out])
            except: pass

            print(f'{out} > {included}')# \n')
            print(f'{out} > {symbol} \n')
            if included:
                acc += out
                for sym in symbol:
                    symbol_memory.append(sym)
    except: pass
print(acc)

print(symbol_memory)

def isGear(plist):
    return plist[0] == '*'

correctId = 0
def isCorrectId(plist):
    return plist[1] == id
    #return plist[2] == "375" or plist[2] == '770'

symbol_memory = list(filter(isGear, symbol_memory))
print(symbol_memory)

#correctId = 
#symbol_memory=list(filter(isCorrectId, symbol_memory))
#print(f'\n\n{symbol_memory}')

ids = []
for balls in symbol_memory:
    if not(balls[1] in ids):
        ids.append(balls[1])
print(ids)

acc = 0
for id in ids:
    correctId = id
    _symbol = list(filter(isCorrectId, symbol_memory))
    print(_symbol)
    if len(_symbol) == 2:
        plist1 = _symbol[0]
        plist2 = _symbol[1]
        acc += int(plist1[2]) * int(plist2[2])
print(acc)

