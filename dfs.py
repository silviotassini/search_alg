def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            traversal_order.append(current_node)
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order