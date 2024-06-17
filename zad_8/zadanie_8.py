def generate_subsets(S):
    n = len(S)
    all_subsets = []

    for i in range(1 << n):  
        subset = []

        for j in range(n):
            if i & (1 << j):
                subset.append(S[j])
        
        all_subsets.append(subset)
    
    return all_subsets

elements = ['a', 'b', 'c']
subsets = generate_subsets(elements)

for subset in subsets:
    print(subset)
