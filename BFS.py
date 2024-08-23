def BFS(graph, key):
    queue = [key]
    visited = set()
    visited.add(key)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


graph = {
    'A': ['C', 'B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

BFS(graph, 'A')
