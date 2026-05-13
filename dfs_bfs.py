# DFS and BFS in a single program

# Undirected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# ---------------- DFS ----------------
visited = set()

# Recursive DFS Function
def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

# ---------------- BFS ----------------
def bfs(start):
    visited_bfs = []
    queue = []

    visited_bfs.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited_bfs:
                visited_bfs.append(neighbor)
                queue.append(neighbor)

# ---------------- Main Program ----------------
print("DFS Traversal:")
dfs('A')

print("\n")

print("BFS Traversal:")
bfs('A')
