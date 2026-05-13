# DFS and BFS with user input graph

graph = {}

# Number of vertices
n = int(input("Enter number of vertices: "))

# Input graph
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[vertex] = neighbors

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

# Starting node
start = input("Enter starting vertex: ")

# DFS Output
print("\nDFS Traversal:")
dfs(start)

# BFS Output
print("\nBFS Traversal:")
bfs(start)
