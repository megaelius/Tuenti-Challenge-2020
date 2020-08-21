import string
# load text
file = open('pg17013.txt', 'rt')

count = {}
accepted = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's' \
, 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ñ', 'ó', 'ú', 'ü']
for line in file:
    word = ''
    #incrementamos la palabra hasta encontrar un carácter que no nos gusta
    #y entonces la añadimos al diccionario
    for ch in line.lower():
        if(ch in accepted):word = word + ch
        elif len(word) > 2:
            if word in count:
                count[word] = count[word] + 1
            else: count[word] = 1
            word = ''
        else: word = ''

count_sort = sorted(count.items(), key=lambda element: (-element[1], element[0]))
file.close()

cases = int(input())
for i in range(0,cases):
    word = input()
    if word in count:
        pos = 0
        while count_sort[pos][0] != word: pos = pos + 1
        print("Case #",i + 1,": ",count_sort[pos][1]," #",pos + 1,sep = '')
    else:
        index = int(word)-1
        elem = count_sort[index]
        print("Case #",i + 1,": ",elem[0]," ",elem[1],sep = '')
