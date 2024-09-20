def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set if not already provided
    
    # Mark the current node as visited and print it
    visited.add(start)
    print(start)
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Sample usage: Start DFS from vertex 'A'
dfs(graph, 'A')
