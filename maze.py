START_X = 0
START_Y = 1


def can_go_right(maze, y):
    return len(maze[0]) - 1 >= y + 1


def can_go_left(y):
    return y - 1 >= 0


def can_go_down(maze, x):
    return len(maze) - 1 > x


def can_go_up(x):
    return x - 1 >= 0


def is_free(content):
    return content != "#"


def can_rotate(maze, x_position, y_position):
    is_free_rotate = True
    # arriba - izquierda
    if can_go_up(x_position) and can_go_left(y_position):
        is_free_rotate = is_free_rotate and (
            is_free(maze[x_position - 1][y_position - 1])
            and is_free(maze[x_position - 1][y_position])
            and is_free(maze[x_position][y_position - 1])
        )
    # arriba - derecha
    if can_go_up(x_position) and can_go_right(maze, y_position):
        is_free_rotate = is_free_rotate and (
            is_free(maze[x_position - 1][y_position + 1])
            and is_free(maze[x_position - 1][y_position])
            and is_free(maze[x_position][y_position + 1])
        )
    # abajo - derecha
    if can_go_down(maze, x_position) and can_go_right(maze, y_position):
        is_free_rotate = is_free_rotate and (
            is_free(maze[x_position + 1][y_position + 1])
            and is_free(maze[x_position + 1][y_position])
            and is_free(maze[x_position][y_position + 1])
        )
    # abajo - izquierda
    if can_go_down(maze, x_position) and can_go_left(y_position):
        is_free_rotate = is_free_rotate and (
            is_free(maze[x_position + 1][y_position - 1])
            and is_free(maze[x_position + 1][y_position])
            and is_free(maze[x_position][y_position - 1])
        )

    return is_free_rotate


def maze_bfs(maze):
    """BFS Algorithm"""
    end_x = len(maze) - 2
    end_y = len(maze[0]) - 1
    
    frontier = []
    frontier.append((START_X, START_Y, "right"))
    visited = []
    counter = 0

    while len(frontier) > 0:
        temp_frontier = []
        for node in frontier:
            if node not in visited:
                if (node[0], node[1]) == (end_x, end_y):
                    return counter + 1

                x_position = node[0]
                y_position = node[1]
                direction = node[2]
                if can_rotate(maze, x_position, y_position):
                    if can_go_right(maze, y_position):
                        temp_frontier.append((x_position, y_position + 1, "right"))
                    if can_go_left(y_position):
                        temp_frontier.append((x_position, y_position - 1, "left"))
                    if can_go_down(maze, x_position):
                        temp_frontier.append((x_position + 1, y_position, "down"))
                    if can_go_up(x_position):
                        temp_frontier.append((x_position - 1, y_position, "up"))
                else:
                    if direction == "down" and can_go_down(maze, x_position):
                        temp_frontier.append((x_position + 1, y_position, "down"))
                    if direction == "right" and can_go_right(maze, y_position):
                        temp_frontier.append((x_position, y_position + 1, "right"))
                    if direction == "up" and can_go_up(x_position):
                        temp_frontier.append((x_position - 1, y_position, "up"))
                    if direction == "left" and can_go_left(y_position):
                        temp_frontier.append((x_position, y_position - 1, "left"))
        visited.extend(frontier)
        frontier = temp_frontier
        counter += 1

    return -1
