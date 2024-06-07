# Wczytaj graf z pliku
FILE_NAME = 'dane.txt'

def load_graf_definition():
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
        no = lines[0]
        
        graf = []

        for i in range(1, len(lines)):
            graf.append([int(x) for x in lines[i].strip().split(' ')])

        return graf



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

def algorytm_DFS(graf, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(f'->{start}', end='')

    for neighbor in graf[start]:
        if neighbor not in visited:
            algorytm_DFS(graf,neighbor, visited)




listaKraw = load_graf_definition()

graf = {}

for i in listaKraw:
    graf[i[0]] = []

for i in listaKraw:
    graf[i[0]].append(i[1])

showListaSasiedztwa(graf)
showMaciezSasiedztwa(graf)

print('DFS:')
algorytm_DFS(graf,0)



