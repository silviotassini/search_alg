from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    traversal_order = []

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            traversal_order.append(current_node)
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order
