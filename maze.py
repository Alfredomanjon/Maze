
visited = [] 
queue = [] 

def maze_bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)