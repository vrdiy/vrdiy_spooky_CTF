''' Made by vrdiy (Anthony Verdi) '''



import math as m
EPSILON = 0.001
e = {'L':'E','T':'G'}

def magic(v)->bool:
    
    f = getattr(m,divinations.__name__[-5:-8:-1])
    c = m.radians(ord(v[9]))
    if (abs(f(c)-1.0) > EPSILON):
        return False
    return spells(v) if (ord(v[10]) & 0b11111110) == 76 else False

def spells(r)->str:
    try:
        m = int(r[0]) == len(r)/4
    except Exception as e:
        m = False

    if not m:
        return False
    return divinations(r)


def divinations(y)->bool:
    d = y[1:9]
    if d[0] != d[-1]:
        return False
    if int((ord(d[0])*2)/13) != len(y):
        return False
    if y[7:2:-2] != "EH1":
        return False
    
    try:
        if e[y[2]] != y[11]:
            return False
        if e[y[6]] != y[4]:
            return False
    except:
        return False
    
    return True

def main():
    solved = False
    while not solved:
        p = input("Password: ")
        if m.sqrt(len(p) / 3) == 2:
            solved = magic(p)
        if solved:
            print("Nice work!")
            break
        if p == '':
            break
                

if __name__ == '__main__':
    main()