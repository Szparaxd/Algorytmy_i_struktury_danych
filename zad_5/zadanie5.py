class Node:
    def __init__(self, Name):
        self.name = Name
        self.color = -1
        self.connects = set()
    
    def __str__(self) -> str:
        return f'vertex {self.name} has color {self.color}'
    
    def __repr__(self):
        return str(f'\n{self}')


def greedy_coloring(graph):
    nodes = []

    for g in graph:
        nodes.append(Node(g))

    for node in nodes:
        connectIds = graph[node.name]
        for idx in connectIds:
            temp_node = nodes[int(idx)]
            node.connects.add(temp_node)
            temp_node.connects.add(node)


    for node in nodes:
        busy_colors = set()
        #print(f'{node}')
        for conn in node.connects: 
            #print(f'    {conn}')
            busy_colors.add(conn.color)

        #print(f'    {busy_colors}')
        i = 0
        while True:
            if not (i in busy_colors):
                node.color = i
                break
            i+=1

        #print(f'{node}')
        #print('-------------')

    print(nodes)

# Przykładowy graf w postaci słownika
graph = {
    '0': ['1', '4'],
    '1': ['2', '4', '5'],
    '2': ['3'],
    '3': ['4', '5'],
    '4': ['5'],
    '5': []
}

if __name__ == '__main__':
    greedy_coloring(graph)



