text = 'ACBECAHCADFEGAFAGACBBADAAFAAEAGACAFABEFBCCFA'

text = input('Podaj text do zaszyfrowania: ')

class Node:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.parent = None
        self.childs = []

    def __str__(self):
        return f'{self.name}:{self.value}'
    
    def __repr__(self):
        return str(f'{self}')

def zlicz_znaki(text):
    words_count = { }
    for i in text:
        if i in words_count:
            words_count[i] += 1
        else:
            words_count[i] = 1

    return words_count

def print_tree(node, code):
    if len(node.childs) == 0:
        print(f'{node.name}:{code}')
    else:
        print_tree(node.childs[0], code+'0')
        print_tree(node.childs[1], code+'1')

words_count = zlicz_znaki(text)
nodes = []

for w in words_count:
    name = w 
    value =  words_count[w]
    nodes.append(Node(value, name))

nodes = sorted(nodes, key=lambda item: (item.value, item.name))
print(nodes)

while len(nodes) > 1:
    n1 = nodes[0]
    n2 = nodes[1]

    sum_child_value = n1.value + n2.value

    parent = Node(sum_child_value, '?')
    n1.parent = parent
    n2.parent = parent
    
    parent.childs.append(n1)
    parent.childs.append(n2)
    parent.childs = sorted(parent.childs, key=lambda item: (item.value, item.name))

    nodes.remove(n1)
    nodes.remove(n2)
    nodes.append(parent)

    nodes = sorted(nodes, key=lambda item: (item.value, item.name))
    print(nodes)

print_tree(nodes[0], '')

def code_t(char, node, code):
    if len(node.childs) == 0:
        if char is not node.name:
            return False
        else:
            print(code, end='')
            return True
    else:
        return code_t(char, node.childs[0], code+'0') or code_t(char, node.childs[1], code+'1')

def code_huffman(node, text):
    for c in text:
        code_t(c, node, '')

code_huffman(nodes[0], text)