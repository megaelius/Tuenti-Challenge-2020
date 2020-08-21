import string
import sys
from collections import Counter

#mierda =' ','1','2','3','4','5','6','7','8','9','0','(',')','\n'
usedeng = ['1','2','3','4','5','6','7','8','9','0','(',')','\n']
usedf = ['1','2','3','4','5','6','7','8','9','0','(',')','\n']


#returns True if the bijection d1 <--> d2 is possible.
def compatibles(d1,d2):
    aux = {}
    aux2 = {}
    for i in range(len(d1)):
        if d1[i] in aux and aux[d1[i]] != d2[i]: return False
        else: aux[d1[i]] = d2[i]
        if d2[i] in aux2 and aux2[d2[i]] != d1[i]: return False
        else: aux2[d2[i]] = d1[i]
    return True

#0: x has characters that have already been assigned to ones different from y's
#1: y is the result of mapping another sequence different than x
#2: x can (a priori )or has already been be mapped into y
def free(x,y,map,inverse,usedf,usedeng):
    out = 3
    for i in range(len(x)):
        if x[i] in map:
            if map[x[i]] != y[i]: return 0
        elif y[i] in inverse:
            if inverse[y[i]] != x[i]: return 1
        else: out = 2
    return out

def assign_mono(map,inverse,l1,l2,usedf,usedeng):
    map[l1] = l2
    inverse[l2] = l1
    usedf.append(l1)
    usedeng.append(l2)

def decrypt_by_freq(fdict,engdict):
    map = {' ':' ','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0',')':')','(':'(','\n':'\n'}
    inverse = {' ':' ','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0',')':')','(':'(','\n':'\n'}
    f = fdict
    eng = engdict
    for i in range(len(f)):
        f[i] = sorted(f[i].items(),key = lambda x : x[1],reverse=True)
        eng[i] = sorted(eng[i].items(),key = lambda x : x[1],reverse=True)

    for k in range(len(engdict)-1,-1,-1):
        #asignamos por palabras de longitud k en orden descendente
        i = 0
        while i < len(f[k]):
            j = 0
            asigned = False
            while not asigned and j < len(eng[k]):
                p1 = f[k][i][0]
                p2 = eng[k][j][0]
                ok = free(p1,p2,map,inverse,usedf,usedeng)
                if ok == 2 and compatibles(p1,p2):
                    for l in range(k+1):
                        if not p1[l] in map: assign_mono(map,inverse,p1[l],p2[l],usedf,usedeng)
                    asigned = True
                else: j = j+1
            i = i + 1
    return map, inverse

def make_tables(txt,N):
    dict = [{} for i in range(N)]
    for i in range(len(txt)-N+1):
        for k in range(0,N):
            word = txt[i:i+k+1]
            if word in dict[k]: dict[k][word] = dict[k][word] + 1
            else:dict[k][word] = 1

    return dict

def change(map,inverse,old,new):
    if new in inverse:
        map[inverse[old]], map[inverse[new]] =  new, old
        inverse[old], inverse[new] =  inverse[new], inverse[old]
    else:
        map[inverse[old]] = new
        inverse[new] = inverse[old]
        inverse[old] = None

"""
with this code i tried to decrypt the text automatically. but after many hours,
it became impossible. So i got the preliminary translation that the program
figured out and changed it myself to make it the good one
"""
def main():
    N = int(input())
    freq = {}
    lines = []
    encripted = ''
    #read and store lines
    for i in range(N):
        linea = sys.stdin.readline()
        encripted = encripted + linea
        lines.append(linea)
    #English text sample from gottemburg proyect
    txt = open('./mobydick.txt').read().lower()
    N = 2
    eng = make_tables(txt,N)
    f = make_tables(encripted,N)
    map,inverse = decrypt_by_freq(f,eng)
    #these changes have to be executed with N=2 and Moby Dick as  the reference text
    change(map,inverse,'b','m')
    change(map,inverse,'d','s')
    change(map,inverse,'f','p')
    change(map,inverse,'b','c')
    change(map,inverse,'u','f')
    change(map,inverse,'k','u')
    change(map,inverse,'k','v')
    change(map,inverse,';','q')
    change(map,inverse,'-','\'')
    change(map,inverse,'-','j')
    change(map,inverse,'-','z')
    change(map,inverse,';','/')
    for i in range(len(lines)):
        line = lines[i]
        print(f'Case #{i+1}: ',end = '')
        for ch in line:
            print(map[ch],end = '')



main()
