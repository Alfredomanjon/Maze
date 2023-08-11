START_X = 0
START_Y = 1


def can_rotate(maze, x, y):
    return (
        maze[x - 1][y - 1] != "#"
        and maze[x - 1][y] != "#"
        and maze[x - 1][y - 1] != "#"
        and maze[x][y + 1] != "#"
        and maze[x][y] != "#"
        and maze[x][y - 1] != "#"
        and maze[x + 1][y - 1] != "#"
        and maze[x + 1][y] != "#"
        and maze[x + 1][y + 1] != "#"
    )


def can_go_right(maze, x):
    return len(maze[0]) - 1 < x + 1


def can_go_left(x):
    return x - 1 > 0


def can_go_down(maze, y):
    return len(maze) - 1 > y


def can_go_up(y):
    return y - 1 > 0


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
                if node == (end_x, end_y):
                    return counter + 1

                x_position = node[0]
                y_position = node[1]
                direction = node[2]
                if can_rotate(maze, x_position, y_position):
                    if can_go_right(maze, x_position):
                        temp_frontier.append((x_position + 1, y_position, "right"))
                    if can_go_left(x_position):
                        temp_frontier.append((x_position - 1, y_position, "left"))
                    if can_go_down(maze, y_position):
                        temp_frontier.append((x_position, y_position + 1, "down"))
                    if can_go_up(y_position):
                        temp_frontier.append((x_position, y_position - 1, "up"))
                else:
                    if direction == "down":
                        temp_frontier.append((x_position, y_position + 1, "down"))
                    if direction == "right":
                        temp_frontier.append((x_position + 1, y_position, "right"))
                    if direction == "up":
                        temp_frontier.append((x_position, y_position - 1, "up"))
                    if direction == "left":
                        temp_frontier.append((x_position - 1, y_position, "left"))
        visited.extend(frontier)
        frontier = temp_frontier
        counter += 1

    return -1
