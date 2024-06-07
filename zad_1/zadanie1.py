# Wczytaj graf z pliku
FILE_NAME = 'dane.txt'

def load_graf_definition():
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
        no = lines[0]
        
        graf = {}

        for i in range(1, len(lines)):
            line =  lines[i].strip().split(' ')
            graf[line[0]] = [int(x) for x in line[1:]]

        return graf

graf = load_graf_definition()
#print(graf)

def showListaSasiedztwa(graf):
    print('Lista sąsiedztwa:')
    for i in graf:
        print(f'{i}: {graf[i]}')

def showMaciezSasiedztwa(graf):
    print('Macież sąsiedztwa')

    colNo = len(graf) 

    print('X ',end='')
    for i in range(colNo):
        print(str(i) + ' ',end='')
        
    print('')
    for i in graf:
        nodes = graf[i]
        print(f'{i} ' ,end='')
        
        for j in range(colNo):
            b = j in nodes 
            print(f'{int(b)} ', end='')

        print('')



showListaSasiedztwa(graf)
showMaciezSasiedztwa(graf)



