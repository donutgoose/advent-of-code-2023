import copy
exampledata = list(map(list, open('exampledata', 'r').read().split('\n')))

m_up = ['|','7','F']
m_down = ['|', 'L', 'J']
m_l = ['-', 'L', 'F']
m_r = ['-', '7', 'J']

d_l = ["UP", "RIGHT"]
d_7 = ["LEFT", "DOWN"]
d_f = ["RIGHT", "DOWN"]
d_j = ["UP", "LEFT"]
d_vpipe = ["UP", "DOWN"]
d_hpipe = ["LEFT", "RIGHT"]

def chase(data, v_index, h_index,step):
    if data[v_index][h_index] == 'S':
        return step
    n_l = data[v_index][h_index-1]
    n_r = data[v_index][h_index+1]
    n_u = data[v_index+1][h_index]
    n_d = data[v_index-1][h_index]
    d = data[v_index][h_index]
    if d == '7':
        mirrorlist = copy.deepcopy(d_7)
    if d == 'f':
        mirrorlist = copy.deepcopy(d_f)
    if n_l in m_l:
        data[v_index][h_index] = step
        return chase(data, v_index, h_index-1, step+1)
    elif n_r in m_r:
        data[v_index][h_index] = step
        return chase(data, v_index, h_index+1, step+1)
    elif n_u in m_up:
        data[v_index][h_index] = step
        return chase(data, v_index+1, h_index, step+1)
    elif n_d in m_down:
        data[v_index][h_index] = step
        return chase(data, v_index-1, h_index, step+1)

def p1(data):
    for index, d in enumerate(data):
        if 'S' in d:
            ind_v = data.index(d)
            ind_h = d.index('S')
            n_l = d[ind_h-1]
            n_r = d[ind_h+1]
            n_u = data[ind_v-1][ind_h]
            n_d = data[ind_v-1] 
            #print(n_l)
            #print(n_r)
            if n_l in m_l:
                return chase(data, ind_v, ind_h-1, 1)
            elif n_r in m_r:
                return chase(data, ind_v, ind_h+1, 1)
            elif n_u in m_up:
                return chase(data, ind_v+1, ind_h, 1)
            elif n_d in m_down:
                return chase(data, ind_v-1, ind_h, 1)

print(p1(exampledata))
