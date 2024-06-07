import heapq

def dijkstra(start, vertices, graph):
    min_heap = [(0, start)]
    shortest_paths = {vertex: (float('inf'), []) for vertex in range(vertices)}
    shortest_paths[start] = (0, [start])
    
    while min_heap:
        current_dist, current_vertex = heapq.heappop(min_heap)

        if current_dist > shortest_paths[current_vertex][0]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight

            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_vertex][1] + [neighbor])
                heapq.heappush(min_heap, (distance, neighbor))

    return shortest_paths

def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        start, vertices, edges = map(int, lines[0].strip().split())
        for i in range(1, edges + 1):
            x, y, w = map(int, lines[i].strip().split())
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            graph[x].append((y, w))
    return start, vertices, graph

def main():
    filename = 'graph.txt'
    start, vertices, graph = read_graph_from_file(filename)
    shortest_paths = dijkstra(start, vertices, graph)

    for vertex in range(vertices):
        dist, path = shortest_paths[vertex]
        if dist < float('inf'):
            print(f"Najkrótsza ścieżka z {start} do {vertex} jest przez {path} z kosztem {dist}")
        else:
            print(f"Brak ścieżki z {start} do {vertex}")

if __name__ == '__main__':
    main()
